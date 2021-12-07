# @Time: 2021/12/6 18:45
# @Author: Chen Chao
# @File: filter_test.py
# @Software: Pycharm

import os
import shutil
from files_move import move

test_path = r'F:\数据集\voc2coco-master\transmission_line_detection\test'
image_path = r'F:\数据集\dataset\train14000 1\train14000\JPEGImages'
xml_path = r'F:\数据集\dataset\train14000 1\train14000\Annotations'

test_image_path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\test'
test_anno_path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\test_annotations'
train_image_path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\train'
train_anno_path = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\train_annotations'

filelist1 = os.listdir(test_path)
print(len(filelist1))
filelist2 = os.listdir(image_path)
print(len(filelist2))

for filename in filelist1:
    if filename in filelist2:
        shutil.move(os.path.join(image_path, filename), test_image_path)
        shutil.move(os.path.join(xml_path, filename[:-3] + 'xml'), test_anno_path)

print('Finished!')


move(image_path, train_image_path, suffix='jpg')
move(xml_path, train_anno_path, suffix='xml')





