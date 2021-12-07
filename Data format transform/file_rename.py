# @Time: 2021/12/6 20:50
# @Author: Chen Chao
# @File: file_rename.py
# @Software: Pycharm

import os

xml_path = 'F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/train_annotations'
image_path = 'F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/train'
# image_path = r'F:\数据集\目标检测从零到实现\Data format transform'

def renumber_img(image_path):
    image_list = os.listdir(image_path)
    image_list = [image for image in image_list if image.endswith('jpg')]
    print(len(image_list))

    total_num = len(image_list)
    for item in image_list:
        if item.startswith('jx_'):
            src = os.path.join(os.path.abspath(image_path), item)
            item2 = 'jx_' + str(int(item[3:8]) + 16463)
            dst = os.path.join(os.path.abspath(image_path), item2 + '.jpg')
            try:
                os.rename(src, dst)
                print('Converting %s to %s ...' % (src, dst))
            except:
                continue
    print('Total %d to rename & converted %d jpgs' % (total_num, total_num))

def renumber_xml(xml_path):
    xml_list = os.listdir(xml_path)
    xml_list = [xml for xml in xml_list if xml.endswith('xml')]
    print(len(xml_list))

    total_num = len(xml_list)
    for item in xml_list:
        if item.startswith('jx_'):
            src = os.path.join(os.path.abspath(xml_path), item)
            item2 = 'jx_' + str(int(item[3:8]) + 16463)
            dst = os.path.join(os.path.abspath(xml_path), item2 + '.xml')
            try:
                os.rename(src, dst)
                print('Converting %s to %s ...' % (src, dst))
            except:
                continue
    print('Total %d to rename & converted %d xmls' % (total_num, total_num))
if __name__ == '__main__':
    renumber_img(image_path)
    renumber_xml(xml_path)