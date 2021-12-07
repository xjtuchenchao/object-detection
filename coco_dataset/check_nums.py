# @Time: 2021/12/7 10:02
# @Author: Chen Chao
# @File: check_nums.py
# @Software: Pycharm

import pycocotools
from pycocotools.coco import COCO

# ann_train_file = r'F:\dataset\annotations_trainval2017\annotations\instances_train2017.json'
# ann_train_file = r'F:\数据集\voc2coco-master\transmission_line_detection\annotations\instances_test.json'
ann_train_file = r'F:\数据集\voc2coco-master\dataset\coco_custom\transmission_30462\instances_test30462.json'
coco_train = COCO(ann_train_file)
print(len(coco_train.dataset['categories']))
print(len(coco_train.dataset['images']))
print(len(coco_train.dataset['annotations']))








