# @Time: 2021/11/29 19:00
# @Author: Chen Chao
# @File: separate_each_category.py
# @Software: vscode

'''Copy the files of each category together'''

from files_move import copy

import xml.etree.cElementTree as ET
import os
import shutil

def separate_specific_category(xml_name, category, image_dir_path, new_path):
    
    xml_path = os.path.join(path, xml_name)

    if not os.path.exists(new_path):
        os.makedirs(new_path, exist_ok=True)

    in_file = open(xml_path)
    tree = ET.parse(in_file)
    root = tree.getroot()
    for obj in root.iter('object'):    # 需要用循环的原因是有可能存在多个object
        cls = obj.find('name').text
        if cls == category:
            filename = xml_name[:-3] + 'jpg'
            shutil.copy(os.path.join(image_dir_path, filename), new_path)
            shutil.copy(xml_path, new_path)
    # print(f'{category} finished!')
    in_file.close()

# classes = ["diaoche", "shigongjixie", "daoxianyiwu", "tadiao", "yanhuo", "huoyan", "negative", "DiaoChe", "daoxian", "YanHuo", "ShiGongJiXie","TaDiao", "DaoXianYiWu"]
classes = ["negative", "DiaoChe", "daoxian", "YanHuo", "ShiGongJiXie","TaDiao", "DaoXianYiWu"]

path = 'F:/数据集/dataset/train14000 1/train14000/Annotations'    # 这里实际上是xml所在的文件夹路径
image_dir_path = 'F:/数据集/dataset/train14000 1/train14000/JPEGImages'
save_path = 'F:/数据集/dataset/train14000 1/all_catgories/'
filelist = os.listdir(path)
xml_path_list = [filename for filename in filelist if filename[-3:] == 'xml']
print(len(xml_path_list))
for xml_name in xml_path_list:
    for category in classes:
        new_path = save_path + category
        separate_specific_category(xml_name, category, image_dir_path, new_path)

print('Finished!')