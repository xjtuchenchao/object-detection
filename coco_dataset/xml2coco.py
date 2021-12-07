import glob
import os
import xml.etree.ElementTree as ET
import json


START_BOUNDING_BOX_ID = 0
PRE_DEFINE_CATEGORIES = {"DaoXianYiWu": 0, "DiaoChe": 1, "ShiGongJiXie": 2, "TaDiao": 3, "YanHuo":4}

def get_categories(xml_files):
    '''
    Generte category name to id mapping from a list of xml files.
    Args:
        xml_files[list]: A list of xml file paths.
    Return: dict -- category name to id mapping.
    '''
    classes_names = []
    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for item in root.findall("object"):
            classes_names.append(item.find('name').text)
    classes_names = list(set(classes_names))
    classes_names.sort()
    return {name : i for i, name in enumerate(classes_names)}

def get_and_check(root, tag, length):
    '''
    Args:
        root: xml.etree.ElementTree.ElementTree object
        tag: xml file tag name. eg:"size","width"
        length: default 1
    Return: filename
    '''
    vars = root.findall(tag)
    if len(vars) == 0:
        raise ValueError(f"Can not find {tag} in {root.tag}")
    if length > 0 and len(vars) != length:
        raise ValueError(
            f"The size of {tag} is supposed to be {length}, but is {len(vars)}."
        )
    if length == 1:
        vars = vars[0]
    return vars

def get(root, tag):
    vars = root.findall(tag)
    return vars

def convert(xml_files, json_file):
    '''
    Convert xml annotations to COCO format.
    Args:
        xml_file: xml format file path.
        json_file: output to a json file.
    Return: None
    '''
    json_dict = {
        "images":[],
        "type":"instances",
        "annotations":[],
        "categories":[]
    }
    if PRE_DEFINE_CATEGORIES is not None:
        categories = PRE_DEFINE_CATEGORIES
    else:
        categories = get_categories(xml_files)
    
    bbox_id = START_BOUNDING_BOX_ID
    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        filename = os.path.basename(xml_file)[:-3] + 'jpg'    # 这里假设我们的文件是以数字命名的，比如："1.jpg","2.jpg","1.xml","2.xml"
        image_id = int(os.path.basename(xml_file)[:-4])
        size = get_and_check(root, "size", 1)
        width = int(get_and_check(size, 'width', 1).text)
        height = int(get_and_check(size, 'height', 1).text)
        image = {
            "file_name":filename,
            "height":height,
            "width":width,
            "id":image_id
        }
        json_dict["images"].append(image)

        for obj in get(root, 'object'):
            category = get_and_check(obj, 'name', 1).text
            if category not in categories:
                new_id = len(categories)
                categories[category] = new_id
            
            category_id = categories[category]
            bndbox = get_and_check(obj, 'bndbox', 1)

            xmin = int(float(get_and_check(bndbox, 'xmin', 1).text)) - 1
            ymin = int(float(get_and_check(bndbox, 'ymin', 1).text)) - 1
            xmax = int(float(get_and_check(bndbox, 'xmax', 1).text))
            ymax = int(float(get_and_check(bndbox, 'ymax', 1).text))
            assert xmax > xmin
            assert ymax > ymin
            o_width = abs(xmax - xmin)
            o_height = abs(ymax - ymin)
            ann = {
                "area":o_width * o_height,
                "iscrowd":0,
                "image_id":image_id,
                "bbox":[xmin, ymin, o_width, o_height],
                "category_id":category_id,
                "id":bbox_id,    # 这个表示object的id
                "ignore":0,
                "segmentation":[]
            }
            json_dict["annotations"].append(ann)
            bbox_id += 1

    for cate, cid in categories.items():
        cat = {
            "supercategory":"none",
            "id":cid,
            "name":cate
        }
        json_dict['categories'].append(cat)
    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    json_fp = open(json_file, 'w')
    json_str = json.dumps(json_dict)
    json_fp.write(json_str)
    json_fp.close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Convert xml annotations to COCO format!')
    parser.add_argument(
        "--xml-dir", 
        default='F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/test_annotations',
        type=str,
        help='Directory path to xml files.'
        )
    parser.add_argument(
        "--json-file",
        default='F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/instances_test30462.json',
        type=str,
        help='Output COCO format json file.'
        )
    args = parser.parse_args()
    xml_files = glob.glob(os.path.join(args.xml_dir, "*.xml"))    # 返回以.xml结尾的目录及文件列表
    print(f"Number of xml files:{len(xml_files)}")
    convert(xml_files, args.json_file)
    print(f"Success:{args.json_file}")

