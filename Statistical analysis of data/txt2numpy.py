import numpy as np
import os
import pandas as pd

path = r'F:\数据集\dataset\train14000 1\train14000\trainlabels'
exclusion = 'classes.txt'

def txt2numpy(path, exclusion):
    filelist = os.listdir(path)

    labels = []
    for filename in filelist:
        if filename[-3:] == 'txt' and filename != exclusion:
            filepath = os.path.join(path, filename)
            label = np.loadtxt(filepath)
            if len(label.shape) == 1:
                label = label[np.newaxis, :]
            label = list(label)
            labels.extend(label)
    labels = np.asarray(labels)
    return labels

labels = txt2numpy(path, exclusion)
print(labels[:,0])
print(labels[:, 1:].transpose())

c, b = labels[:, 0], labels[:, 1:].transpose()  # classes, boxes
nc = int(c.max() + 1)  # number of classes
x = pd.DataFrame(b.transpose(), columns=['x', 'y', 'width', 'height'])
print(x)