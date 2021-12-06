# @Time: 2021/11/28 15:27
# @Author: Chen Chao
# @File: gen_train_test_dataset.py
# @Software: vscode

'''
Divide the dataset into a training set and a test set.
当数据集按类别存放在不同的文件夹中的时候用这个脚本进行划分。
'''

import os
import random
import shutil

def divide_train_test(test_percent, train_path, test_path):
    '''从每个类别的文件夹中将一部分数据分为测试集'''

    classes = ["DaoXianYiWu", "DiaoChe", "ShiGongJiXie", "TaDiao", "YanHuo"]
    for i in range(len(classes)):
        train_image_path = train_path + classes[i]
        image_list = os.listdir(train_image_path)
        total_image_num = len(image_list)
        test_num = int(total_image_num * test_percent)
        test_set = random.sample(range(total_image_num), test_num)

        for i in range(total_image_num):
            name = image_list[i][:-4]
            if i in test_set:
                jpg_src = name + '.jpg'
                xml_src = name + '.xml'
                jpg_dst = test_path + '/images'
                xml_dst = test_path + '/Annotations'

                if not os.path.exists(jpg_dst):
                    os.makedirs(jpg_dst)
                if not os.path.exists(xml_dst):
                    os.makedirs(xml_dst)
                    
                shutil.move(os.path.join(train_image_path, jpg_src), jpg_dst)
                shutil.move(os.path.join(train_image_path + '_xml', xml_src), xml_dst)

if __name__ == '__main__':
    train_percent = 0.8
    test_percent = 0.2
    train_path = 'F:/数据集/voc2coco-master/Train/'
    test_path = 'F:/数据集/voc2coco-master/test'
    
    divide_train_test(test_percent, train_path, test_path)
    print('Finished!')

















