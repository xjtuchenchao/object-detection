# @Time: 2021/11/29 11:00
# @Author: Chen Chao
# @File: filter_specific_category.py
# @Software: Pycharm

import xml.etree.cElementTree as ET
import os
import shutil

def filter_specific_category(xml_path, category, image_dir_path, new_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    in_file = open(xml_path)
    tree = ET.parse(in_file)
    root = tree.getroot()
    for obj in root.iter('object'):    # 需要用循环的原因是有可能存在多个object
        cls = obj.find('name').text
        if cls == category:
            filename = root.find('filename').text
            shutil.copy(os.path.join(image_dir_path, filename), new_path)

    in_file.close()

path = 'F:/数据集/voc2coco-master/Train/DaoXianYiWu_xml'    # 这里实际上是xml所在的文件夹路径
image_dir_path = 'F:/数据集/voc2coco-master/Train/DaoXianYiWu'
new_path = 'F:/数据集/DaoXianYiWu2'
category = 'DaoXianYiWu'
filelist = os.listdir(path)
xml_path_list = [i for i in filelist if i[-3:] == 'xml']
print(len(xml_path_list))
for xml_name in xml_path_list:
    xml_path = os.path.join(path, xml_name)
    filter_specific_category(xml_path, category, image_dir_path, new_path)












