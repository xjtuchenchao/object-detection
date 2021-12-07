# @Time: 2021/12/6 21:36
# @Author: Chen Chao
# @File: total_rename.py
# @Software: Pycharm

import os

# xml_path = 'F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/train_annotations'
# image_path = 'F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/train'
xml_path = 'F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/test_annotations'
image_path = 'F:/数据集/voc2coco-master/dataset/coco_custom/transmission_30462/test'

def renumber_xml(xml_path, img_path):
    xml_list = os.listdir(xml_path)
    img_list = os.listdir(img_path)
    print(len(xml_list))
    print(len(img_list))
    # xml_list.sort(key=lambda x: int(x.split('.')[0]))

    i = 1
    xml_total_num = len(xml_list)
    img_total_num = len(img_list)

    for item in xml_list:
        if item.endswith('.xml'):
            src1 = os.path.join(os.path.abspath(xml_path),item)
            dst1 = os.path.join(os.path.abspath(xml_path),str(i) + '.xml')
            src2 = os.path.join(os.path.abspath(img_path), item[:-3] +'jpg')
            dst2 = os.path.join(os.path.abspath(img_path), str(i) + '.jpg')

            os.rename(src1, dst1)
            print('Converting %s to %s ...' % (src1, dst1))
            os.rename(src2, dst2)
            print('Converting %s to %s ...' % (src2, dst2))
            i += 1

    print('Total %d to rename & converted %d xmls' % (xml_total_num, i - 1))
    print('Total %d to rename & converted %d jpgs' % (img_total_num, i - 1))


def renumber_img(image_path):
    image_list = os.listdir(image_path)
    print(len(image_list))
    # image_list.sort(key=lambda x: int(x.split('.')[0]))

    i = 1
    total_num = len(image_list)
    for item in image_list:
        if item.endswith('.jpg'):
            src = os.path.join(os.path.abspath(image_path), item)
            dst = os.path.join(os.path.abspath(image_path), str(i) + '.jpg')
            try:
                os.rename(src, dst)
                print('Converting %s to %s ...' % (src, dst))
                i += 1
            except:
                continue
    print('Total %d to rename & converted %d jpgs' % (total_num, i - 1))

if __name__ == '__main__':
    renumber_xml(xml_path, image_path)
