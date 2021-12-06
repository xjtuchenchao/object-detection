import xml.etree.cElementTree as ET
import os

def modify_one_xml(xml_path, classes):
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
        else:
            pass
    tree.write(xml_path)
classes = ["huoyan", "negative", "DiaoChe", "daoxian", "YanHuo", "ShiGongJiXie","TaDiao", "DaoXianYiWu"]
path = 'F:/数据集/dataset/train14000 1/train14000/Annotations'
filelist = os.listdir(path)
xml_name_list = [filename for filename in filelist if filename[-3:] == 'xml']
print(len(xml_name_list))
for xml_name in xml_name_list:
    modify_one_xml(os.path.join(path, xml_name))

print('Finished!')