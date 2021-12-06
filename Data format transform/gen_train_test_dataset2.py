# @Time: 2021/11/30 17:12
# @Author: Chen Chao
# @File: gen_train_test_dataset2.py
# @Software: vscode

'''
Divide the dataset into a training set and a test set.
当数据集图image和xml放在一个文件夹中的时候用这个脚本进行划分。
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
                jpg_dst = test_path + '/image'
                xml_dst = test_path + '/Annotations'

                if not os.path.exists(jpg_dst):
                    os.makedirs(jpg_dst)
                if not os.path.exists(xml_dst):
                    os.makedirs(xml_dst)
                    
                shutil.move(os.path.join(train_image_path, jpg_src), jpg_dst)
                shutil.move(os.path.join(train_image_path, xml_src), xml_dst)

if __name__ == '__main__':
    train_percent = 0.8
    test_percent = 0.2
    train_path = 'F:/数据集/dataset/train14000 1/all_catgories/'
    test_path = 'F:/数据集/dataset/train14000 1/test'
    
    divide_train_test(test_percent, train_path, test_path)
    print('Finished!')