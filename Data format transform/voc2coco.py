# @Time: 2021/11/28 16:32
# @Author: Chen Chao
# @File: voc2coco.py
# @Software: vscode

'''Convert the voc dataset to coco dataset'''
# Pycharm参数： F:/数据集/voc2coco-master/test/Annotations F:/数据集/voc2coco-master/annotations/instances_test.json
# Pycharm参数： F:/数据集/voc2coco-master/Train/Annotations F:/数据集/voc2coco-master/annotations/instances_train.json

import re
import os
import json
import xml.etree.ElementTree as ET
import glob

START_BOUNDING_BOX_ID = 0
# PRE_DEFINE_CATEGORIES = None

# If necessary, pre-define category and its id
PRE_DEFINE_CATEGORIES = {"DaoXianYiWu": 0, "DiaoChe": 1, "ShiGongJiXie": 2, "TaDiao": 3, "YanHuo":4}


def get(root, name):
    vars = root.findall(name)
    return vars


def get_and_check(root, name, length):
    '''
    Args:
        root: xml.etree.ElementTree.ElementTree object
        name: filename tag
        length: default 1

    Returns: filename
    '''
    vars = root.findall(name)
    if len(vars) == 0:
        raise ValueError("Can not find %s in %s." % (name, root.tag))
    if length > 0 and len(vars) != length:
        raise ValueError(
            "The size of %s is supposed to be %d, but is %d."
            % (name, length, len(vars))
        )
    if length == 1:
        vars = vars[0]
    return vars


def get_filename_as_int(filename):
    # 这个函数的前提是filename的文件名(除掉后缀)仅包含数字
    try:
        filename = filename.replace("\\", "/")
        filename = os.path.splitext(os.path.basename(filename))[0]
        return int(filename)
    except:
        raise ValueError("Filename %s is supposed to be an integer." % (filename))


def get_categories(xml_files):
    """Generate category name to id mapping from a list of xml files.
    
    Arguments:
        xml_files {list} -- A list of xml file paths.
    
    Returns:
        dict -- category name to id mapping.
    """
    classes_names = []
    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall("object"):
            classes_names.append(member[0].text)

    classes_names = list(set(classes_names))

    classes_names.sort()
    return {name: i for i, name in enumerate(classes_names)}


def convert(xml_files, json_file):
    '''
    Convert Pascal VOC annotation to COCO format.
    Args:
        xml_files: xml format file path.
        json_file: output to a json file.

    Returns: None

    '''
    json_dict = {"images": [], "type": "instances", "annotations": [], "categories": []}
    if PRE_DEFINE_CATEGORIES is not None:
        categories = PRE_DEFINE_CATEGORIES
    else:
        categories = get_categories(xml_files)

    bnd_id = START_BOUNDING_BOX_ID
    for xml_file in xml_files:
        print(xml_file)

        tree = ET.parse(xml_file)
        root = tree.getroot()
        # filename = get(root, "filename")[0].text
        # filename_num = re.match('[a-zA-Z]*(\d*).jpg', filename).group(1)
        # filename_num = int(filename_num)


        # path = get(root, "path")
        #
        # if len(path) == 1:
        #     # 返回文件名
        #     filename = os.path.basename(path[0].text)
        # elif len(path) == 0:
        #     # 没有path路径的时候走这一分支
        #     filename = get_and_check(root, "filename", 1).text
        # else:
        #     raise ValueError("%d paths found in %s" % (len(path), xml_file))


        # The filename must be a number
        # image_id = get_filename_as_int(filename)
        # image_id = filename_num    # 当图片的数字不连续时，会不会有什么影响？

        filename = os.path.basename(xml_file)[:-3] + 'jpg'
        image_id = int(os.path.basename(xml_file)[:-4])
        size = get_and_check(root, "size", 1)
        width = int(get_and_check(size, "width", 1).text)
        height = int(get_and_check(size, "height", 1).text)
        image = {
            "file_name": filename,
            "height": height,
            "width": width,
            "id": image_id,
        }
        json_dict["images"].append(image)

        for obj in get(root, "object"):    # 这边做一个测试，看看是不是一张图片存在多个object的时候不会影响？
            category = get_and_check(obj, "name", 1).text
            if category not in categories:
                new_id = len(categories)
                categories[category] = new_id

            category_id = categories[category]
            bndbox = get_and_check(obj, "bndbox", 1)

            xmin = int(float(get_and_check(bndbox, "xmin", 1).text)) - 1
            ymin = int(float(get_and_check(bndbox, "ymin", 1).text)) - 1
            xmax = int(float(get_and_check(bndbox, "xmax", 1).text))
            ymax = int(float(get_and_check(bndbox, "ymax", 1).text))
            assert xmax > xmin
            assert ymax > ymin
            o_width = abs(xmax - xmin)
            o_height = abs(ymax - ymin)
            ann = {
                "area": o_width * o_height,
                "iscrowd": 0,
                "image_id": image_id,
                "bbox": [xmin, ymin, o_width, o_height],
                "category_id": category_id,
                "id": bnd_id,
                "ignore": 0,
                "segmentation": [],
            }
            json_dict["annotations"].append(ann)
            bnd_id = bnd_id + 1

    for cate, cid in categories.items():
        cat = {"supercategory": "none", "id": cid, "name": cate}
        json_dict["categories"].append(cat)

    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    json_fp = open(json_file, "w")
    json_str = json.dumps(json_dict)
    json_fp.write(json_str)
    json_fp.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert Pascal VOC annotation to COCO format."
    )
    parser.add_argument("--xml-dir", default='F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/test_annotations', help="Directory path to xml files.", type=str)
    parser.add_argument("--json-file", default='F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/instances_test30462.json', help="Output COCO format json file.", type=str)
    args = parser.parse_args()
    xml_files = glob.glob(os.path.join(args.xml_dir, "*.xml"))  # 返回以.xml结尾的目录及文件列表

    # If you want to do train/test split, you can pass a subset of xml files to convert function.
    # 如果要进行训练/测试拆分，可以传递 xml 文件的子集来转换函数
    print("Number of xml files: {}".format(len(xml_files)))
    convert(xml_files, args.json_file)
    print("Success: {}".format(args.json_file))



















