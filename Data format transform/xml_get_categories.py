# @Time: 2021/12/6 20:20
# @Author: Chen Chao
# @File: xml_get_categories.py
# @Software: Pycharm

import re
import os
import json
import xml.etree.ElementTree as ET
import glob

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

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert Pascal VOC annotation to COCO format."
    )
    parser.add_argument("--xml-dir", default='F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/train_annotations', help="Directory path to xml files.", type=str)
    parser.add_argument("--json-file", default='F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/instances_train30462.json', help="Output COCO format json file.", type=str)
    args = parser.parse_args()
    xml_files = glob.glob(os.path.join(args.xml_dir, "*.xml"))  # 返回以.xml结尾的目录及文件列表

    # If you want to do train/test split, you can pass a subset of xml files to convert function.
    # 如果要进行训练/测试拆分，可以传递 xml 文件的子集来转换函数
    print("Number of xml files: {}".format(len(xml_files)))
    categories = get_categories(xml_files)
    print(categories)