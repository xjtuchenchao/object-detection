# @Time: 2021/11/28 14:14
# @Author: Chen Chao
# @File: files_move.py
# @Software: vscode

'''Move/copy files from one folder to another folder'''

import os
import shutil

def move(source_dir_path, target_dir_path, suffix='xml', recursion=False):
    '''
    Move files from one folder to another folder. If recursion is True, the files in the folder will also move to the target directory.
    '''
    if not os.path.exists(target_dir_path):
        os.makedirs(target_dir_path)

    if os.path.isdir(source_dir_path) and os.path.isdir(target_dir_path):
        filelist = os.listdir(source_dir_path)
        for file in filelist:
            path = os.path.join(source_dir_path, file)
            if os.path.isdir(path) and recursion:
                move(path, target_dir_path)    # Move the files in the folder to the target directory.
            
            if file[-3:] == suffix:
                if not os.path.exists(os.path.join(target_dir_path, file)):
                    shutil.move(path, target_dir_path)
            else:
                # print(f'It is not a {suffix} file')
                pass
    
    print('Finished!')    

def copy(source_dir_path, target_dir_path, suffix='xml', recursion=False):
    if not os.path.exists(target_dir_path):
        os.makedirs(target_dir_path)

    if os.path.isdir(source_dir_path) and os.path.isdir(target_dir_path):
        filelist = os.listdir(source_dir_path)
        for file in filelist:
            path = os.path.join(source_dir_path, file)
            if os.path.isdir(path) and recursion:
                move(path, target_dir_path)
            
            if file[-3:] == suffix:
                shutil.copy(path, target_dir_path)
            else:
                # print(f'It is not a {suffix} file')
                pass
    
    print('Finished!')

if __name__ == '__main__':
    classes = ["DaoXianYiWu", "DiaoChe", "ShiGongJiXie", "TaDiao", "YanHuo"]
    suffix = 'xml'

    for i in range(len(classes)):
        source_dir_path = 'F:/数据集/voc2coco-master/Train/' + classes[i]
        target_dir_path = 'F:/数据集/voc2coco-master/Train/' + classes[i] + '_' + suffix
        move(source_dir_path, target_dir_path, suffix='xml')
        # copy(source_dir_path, target_dir_path, suffix='xml')




