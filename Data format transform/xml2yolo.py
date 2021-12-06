from genericpath import exists
from xml.etree.ElementTree import parse
import xml.etree.cElementTree as ET
import os
import argparse

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

def convert_annotation(xml_file, save_path):
    in_file = open(xml_file)
    out_file = open(os.path.join(save_path, xml_file[:-3] + 'txt'), 'w')
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

def parse_args():
    parser = argparse.ArgumentParser(description='convert xml file in one folder to txt file')
    parser.add_argument(
        '--dir-path', 
        type=str, 
        default='F:/数据集/voc2coco-master/Train/Annotations', 
        help='the folder path where the xml files are'
        )
    parser.add_argument(
        '--save-path', 
        type=str, 
        default='F:/数据集/voc2coco-master/Train/labels', 
        help='the path to save the txt file'
        )
    args = parser.parse_args()

    return args

if __name__ == '__main__':

    args = parse_args()

    classes = ["DaoXianYiWu", "DiaoChe", "ShiGongJiXie", "TaDiao", "YanHuo"]

    if not os.path.exists(args.save_path):
        os.makedirs(args.save_path, exist_ok=True)
    filelist = os.listdir(args.dir_path)
    for filename in filelist:
        convert_annotation(os.path.join(args.dir_path, filename), args.save_path)
    
    print('Finished!')