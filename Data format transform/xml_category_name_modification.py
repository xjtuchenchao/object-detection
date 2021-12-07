# @Time: 2021/11/30 11:04
# @Author: Chen Chao
# @File: xml_category_name_modification.py
# @Software: vscode

'''Modify the category name of the xml file to a specific name'''


import xml.etree.cElementTree as ET
import os

def modify_one_xml(xml_path):
    file = open(xml_path)
    tree = ET.parse(file)
    root = tree.getroot()
    for obj in root.iter('object'):
        cls_name = obj.find('name')
        if cls_name.text == 'diaoche':
            cls_name.text = "DiaoChe"
        elif cls_name.text == 'shigongjixie':
            cls_name.text = "ShiGongJiXie"
        elif cls_name.text == 'daoxianyiwu':
            cls_name.text = "DaoXianYiWu"
        elif cls_name.text == 'tadiao':
            cls_name.text = "TaDiao"
        elif cls_name.text == 'yanhuo':
            cls_name.text = "YanHuo"
        elif cls_name.text == 'huoyan':
            cls_name.text = "YanHuo"
        else:
            pass
    tree.write(xml_path)

path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\train_annotations'
filelist = os.listdir(path)
xml_name_list = [filename for filename in filelist if filename[-3:] == 'xml']
print(len(xml_name_list))
for xml_name in xml_name_list:
    modify_one_xml(os.path.join(path, xml_name))

print('Finished!')





























