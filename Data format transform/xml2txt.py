# @Time: 2021/11/27 23:19
# @Author: Chen Chao
# @File: xml2txt.py
# @Software: vscode

'''
Purpose: Generate the corresponding txt file for each xml file
NOTE: Please attention that we can specify the category labels and its order,
without calling the "gen_class" function to get the category and its order.
Otherwise, it may be different from what we hope.
'''

import xml.etree.cElementTree as ET
import os

# classes = ["DaoXianYiWu", "DiaoChe", "ShiGongJiXie", "TaDiao", "YanHuo"]

# Get all category labels
classes = []
def gen_classes(image_id):
    file = open('%s/Annotations/%s.xml'%(path, image_id))
    tree = ET.parse(file)
    root = tree.getroot()
    for obj in root.iter('object'):
        cls_name = obj.find('name').text
        if cls_name in classes:
            pass
        else:
            classes.append(cls_name)
            
        if cls_name == 'DiaoChe':
            print(image_id)

    return classes

# Convert the bbox of the voc dataset format to the yolo dataset format
def convert(size, bbox):
    '''
    NOTE: This function converts the (xmin, xmax, ymin, ymax) to (x_center, y_center, width, height), return the normalized values.
    '''
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (bbox[0] + bbox[1]) / 2.0
    y = (bbox[2] + bbox[3]) / 2.0
    w = bbox[1] - bbox[0]
    h = bbox[3] - bbox[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# 
def convert_annotation(image_set, image_id):
    in_file = open('%s/Annotations/%s.xml'%(path, image_id))
    out_file = open('%s/%s'%(path, image_set) + 'labels/%s.txt'%image_id, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes:    # or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        xml_bbox = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        txt_bbox = convert((w, h), xml_bbox)
        out_file.write(str(cls_id) + ' ' + ' '.join([str(coordinate) for coordinate in txt_bbox]) + '\n')
    in_file.close()
    out_file.close()

path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462'
# sets = ['train', 'val']
sets = ['train', 'test']
for image_set in sets:
    if not os.path.exists('%s/%s'%(path, image_set) + 'labels/'):
        os.makedirs('%s/%s'%(path, image_set) + 'labels/', exist_ok=True)
    image_ids = open('%s/ImageSets/Main/%s.txt'%(path,image_set)).read().strip().split()
    for image_id in image_ids:
        gen_classes(image_id)
        convert_annotation(image_set, image_id)

    print(classes)
    classes_file = open('%s/%s'%(path, image_set) + 'labels/classes.txt', 'w')
    classes_file.write("\n".join([a for a in classes]))
    classes_file.close()














