# @Time: 2021/11/28 16:32
# @Author: Chen Chao
# @File: copy_together.py
# @Software: vscode

'''Copy the files of each category together'''

from files_move import copy

if __name__ == '__main__':
    # # copy xml file
    # classes = ["DaoXianYiWu", "DiaoChe", "ShiGongJiXie", "TaDiao", "YanHuo"]
    # suffix = 'xml'
    #
    # for i in range(len(classes)):
    #     source_dir_path = 'F:/数据集/voc2coco-master/Train/' + classes[i] + '_' + suffix
    #     target_dir_path = 'F:/数据集/voc2coco-master/Train/Annotations'
    #     # move(source_dir_path, target_dir_path)
    #     copy(source_dir_path, target_dir_path, suffix='xml')


    # copy jpg file
    classes = ["DaoXianYiWu", "DiaoChe", "ShiGongJiXie", "TaDiao", "YanHuo"]
    for i in range(len(classes)):
        source_dir_path = 'F:/数据集/voc2coco-master/Train/' + classes[i]
        target_dir_path = 'F:/数据集/voc2coco-master/Train/images'
        # move(source_dir_path, target_dir_path)
        copy(source_dir_path, target_dir_path, suffix='jpg')



















