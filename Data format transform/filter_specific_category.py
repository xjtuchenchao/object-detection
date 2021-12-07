import xml.etree.cElementTree as ET
import os
import shutil

def filter_one_xml(xml_path, xml_name, img_save_path, xml_save_path):
    xml_path = os.path.join(xml_path, xml_name)
    image_path = os.path.join(img_path, xml_name[:-3] + 'jpg')
    file = open(xml_path)
    tree = ET.parse(file)
    root = tree.getroot()

    log = False
    for obj in root.iter('object'):
        cls_name = obj.find('name').text
        if cls_name == 'negative' or cls_name == 'daoxian':
            log = True

    file.close()
    if log:
        shutil.move(image_path, img_save_path)
        shutil.move(xml_path, xml_save_path)



xml_path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\train_annotations'
img_path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\train'
img_save_path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\negative_daoxian'
xml_save_path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\negative_daoxian_xml'
filelist = os.listdir(xml_path)
xml_name_list = [filename for filename in filelist if filename[-3:] == 'xml']
print(len(xml_name_list))
for xml_name in xml_name_list:
    filter_one_xml(xml_path, xml_name, img_save_path, xml_save_path)

print('Finished!')