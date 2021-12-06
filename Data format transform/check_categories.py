import xml.etree.cElementTree as ET
import os


classes = []
def gen_classes(image_id):
    file = open('%s/Annotations/%s.xml'%(path, image_id))
    tree = ET.parse(file)
    root = tree.getroot()
    for obj in root.iter('object'):
        cls_name = obj.find('name').text
        if cls_name in classes:
            pass
        else:
            classes.append(cls_name)
    return classes

path = 'F:/数据集/dataset/train14000 1/train14000'
# sets = ['train', 'val']
sets = ['train']
for image_set in sets:
    if not os.path.exists('%s/%s'%(path, image_set) + 'labels/'):
        os.makedirs('%s/%s'%(path, image_set) + 'labels/', exist_ok=True)
    image_ids = open('%s/ImageSets/Main/%s.txt'%(path,image_set)).read().strip().split()
    for image_id in image_ids:
        gen_classes(image_id)
        
    print(classes)
