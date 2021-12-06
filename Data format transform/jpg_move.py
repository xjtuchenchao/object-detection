from files_move import copy,move
import os

# copy('F:/数据集/voc2coco-master/test/images', 'F:/数据集/dataset/train14000 1/train14000/JPEGImages', suffix='jpg')

classes = ["DaoXianYiWu", "DiaoChe", "ShiGongJiXie", "TaDiao", "YanHuo"]
for i in range(len(classes)):
    move(os.path.join('F:/数据集/dataset/train14000 1/all_catgories', classes[i]), 'F:/数据集/dataset/train14000 1/train', suffix='jpg')
    move(os.path.join('F:/数据集/dataset/train14000 1/all_catgories', classes[i]), 'F:/数据集/dataset/train14000 1/train_annotations', suffix='xml')
    print(f'{classes[i]} Finished!')