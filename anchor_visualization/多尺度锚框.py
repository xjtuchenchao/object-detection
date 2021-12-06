# @Time: 2021/12/2 16:30
# @Author: Chen Chao
# @File: 多尺度锚框.py
# @Software: Pycharm

import torch
import matplotlib.pyplot as plt
from d2l import torch as d2l

img = d2l.plt.imread('DiaoChe00265.jpg')
h, w = img.shape[:2]    # HWC
print(h,w)

# 在特征图（fmap）上生成锚框（anchors），每个单位（像素？）作为锚框的中心
def display_anchors(fmap_w, fmap_h, size):
    d2l.set_figsize()
    fmap = torch.zeros((1, 10, fmap_h, fmap_w))
    anchors = d2l.multibox_prior(
        fmap, sizes=size, ratios=[1, 2, 0.5]
    )
    bbox_scale = torch.tensor((w, h, w, h))
    d2l.show_bboxes(d2l.plt.imshow(img).axes, anchors[0] * bbox_scale)

display_anchors(fmap_w=2, fmap_h=2, size=[0.15])



