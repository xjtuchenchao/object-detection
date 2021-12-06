from xml.dom.minidom import parse
import os  
import os.path 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

square=0
numbers=np.zeros(13)
size0=np.zeros(4)
size1=np.zeros(10)
size2=np.zeros(10)
object_size=np.zeros(13)

path="C:\\Users\\Luo\\Desktop\\dataset"
files=os.listdir(path)  #得到文件夹下所有文件名称 

#计算方框大小分布函数
def count_size(n,size):
    if area<1000*n:
        size[0]+=1
    elif area<2000*n:
        size[1]+=1
    elif area<3000*n:
        size[2]+=1
    elif area<4000*n:
        size[3]+=1
    elif area<5000*n:
        size[4]+=1
    elif area<6000*n:
        size[5]+=1
    elif area<7000*n:
        size[6]+=1
    elif area<8000*n:
        size[7]+=1
    elif area<9000*n:
        size[8]+=1
    elif area<10000*n:
        size[9]+=1

#计算各对象有关数值的函数
def count_object(n,i):
    if name.childNodes[0].data=='杆塔':
        n[0]+=i
    elif name.childNodes[0].data=='支撑件':
        n[1]+=i
    elif name.childNodes[0].data=='支撑杆':
        n[1]+=i
    elif name.childNodes[0].data=='绝缘子':
        n[2]+=i
    elif name.childNodes[0].data=='烟雾':
        n[3]+=i
    elif name.childNodes[0].data=='挖掘机':
        n[4]+=i
    elif name.childNodes[0].data=='铲车':
        n[5]+=i
    elif name.childNodes[0].data=='吊车':
        n[6]+=i
    elif name.childNodes[0].data=='塔吊':
        n[7]+=i
    elif name.childNodes[0].data=='混凝土搅拌机':
        n[8]+=i
    elif name.childNodes[0].data=='风筝':
        n[9]+=i
    elif name.childNodes[0].data=='塑料':
        n[10]+=i
    elif name.childNodes[0].data=='压路机':
        n[11]+=i
    elif name.childNodes[0].data=='火山':
        n[12]+=i

for xmlFile in files: #遍历文件夹
    DOMTree=parse(os.path.join(path,xmlFile)) #拼接地址，将每个具体的.xml文件带入
    type(DOMTree)
    list=DOMTree.documentElement
    
    object=list.getElementsByTagName('object')#获取xml文件里所有object节点的集合
    square=square+len(object)#计算方框数量

    for list in object:
        name=list.getElementsByTagName('name')[0]
        #计算方框大小
        xmin=list.getElementsByTagName('xmin')[0]
        xmax=list.getElementsByTagName('xmax')[0]
        ymin=list.getElementsByTagName('ymin')[0]
        ymax=list.getElementsByTagName('ymax')[0]
        area=(int(xmax.childNodes[0].data)-int(xmin.childNodes[0].data))*(int(ymax.childNodes[0].data)-int(ymin.childNodes[0].data))
        #计算各对象数量
        count_object(numbers,1)

        #方框大小分布
        if area<100000:
            size0[0]+=1
        elif area<200000:
            size0[1]+=1
        elif area<300000:
            size0[2]+=1
        elif area>300000:
            size0[3]+=1
        count_size(10,size1)
        count_size(1,size2)

        #各对象方框大小
        count_object(object_size,area)

object_size=object_size/numbers

print('方框数量为%d个'%square)        
print('杆塔有%d个'%numbers[0])
print('支撑件有%d个'%numbers[1])
print('绝缘子有%d个'%numbers[2])
print('烟雾有%d个'%numbers[3])
print('挖掘机有%d个'%numbers[4])
print('铲车有%d个'%numbers[5])
print('吊车有%d个'%numbers[6])
print('塔吊有%d个'%numbers[7])
print('混凝土搅拌机有%d个'%numbers[8])
print('风筝有%d个'%numbers[9])
print('塑料有%d个'%numbers[10])
print('压路机有%d个'%numbers[11])
print('火山有%d个'%numbers[12])

#作图
plt.rcParams["font.sans-serif"]="KaiTi" #字体
plt.rcParams["axes.unicode_minus"]=False  #防止方块化

#方框大小分布扇形图
label=["10w以内","10w到20w","20w到30w","30w以上"]
colors1=['violet','teal','palegreen','tomato']
explode1=np.ones_like(size0)/100
plt.pie(size0,
        labels = label,
        autopct = '%.0f%%',
        colors=colors1,
        explode=explode1,
        shadow = False, #无阴影设置
        startangle =90, #逆时针起始角度设置
        pctdistance = 0.6) #数值距圆心半径倍数距离)
plt.title('方框大小分布（单位：像素）')
plt.show()

#方框大小分布条形图1
x1=['0','10000','20000','30000','40000','50000','60000','70000','80000','90000']
plt.bar(x1, #x轴数据
         size1,  #y轴数据
         align ='edge', #设置条形的中心位置在边缘，center为边缘
         color='steelblue', # 颜色
         width = 1)
plt.grid(True)
plt.title('10w像素以内方框大小分布')
plt.show()

#方框大小分布条形图2
x2=['0','1000','2000','3000','4000','5000','6000','7000','8000','9000']
plt.bar(x2, #x轴数据
         size2,  #y轴数据
         align ='edge', #设置条形的中心位置在中间，edge为边缘
         color='steelblue', # 颜色
         width = 1)
plt.grid(True)
plt.title('1w像素以内方框大小分布')
plt.show()

#对象个数扇形图
names=['杆塔','支撑件','绝缘子','烟雾','挖掘机','铲车','吊车','塔吊','混凝土搅拌机','风筝','塑料','压路机','火山']
#去除个数为0的部分
numbers=numbers.tolist()#将numpy转换为list
object_size=object_size.tolist()
for i in range(12):
    if numbers[i]==0:
        names.remove(names[i])
        numbers.remove(numbers[i]) 
        object_size.remove(object_size[i]) 
numbers=np.array(numbers)#将list转换为numpy
object_size=np.array(object_size)

# plt.pie(number,labels = names,autopct = '%.0f%%')
colors2 = ['tomato','sandybrown','gold','olivedrab','palegreen','turquoise','teal','violet','deepskyblue','lightslategrey','royalblue','mediumslateblue','cyan']
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(9, 10))#在画布上画2*2个图，我们的扇形图将会是第一个图，为了简洁，我们不显示另外三个分图。
# ax1, ax2, ax3, ax4 = axes.flatten()#flatten()将ax由2*2的Axes组展平成1*4的Axes组
# fig.subplots_adjust(hspace=.5, wspace=.3)#调整分图距离，我们的图片里只是截取了第一个分徒（扇形图）
explode2=np.ones_like(numbers)/100
patches,text1,text2 = plt.pie(numbers,
                      explode=explode2,
                      labels=names,
                      colors=colors2,
                      labeldistance = 1.05,#图例距圆心半径倍距离
                      autopct = '%3.1f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.9) #数值距圆心半径倍数距离
plt.axis('equal')
plt.legend()
plt.title("各对象数量统计",fontdict={'fontsize':28,'color':'black'})
plt.show()

#各个对象方框大小平均值散点图
colors3 = ['tomato','sandybrown','gold','olivedrab','palegreen','turquoise','violet','deepskyblue','royalblue','mediumslateblue','cyan']
size4=np.zeros_like(object_size)
for i in range(len(object_size)):
    if (object_size[i]*numbers[i]/10000)<100:
        size4[i]=100
    else:
        size4[i]=object_size[i]*numbers[i]/10000
plt.scatter(numbers,object_size,c=colors3,s=size4)
for i in range(len(numbers)):
    plt.annotate(names[i], xy = (numbers[i], object_size[i]), xytext = (numbers[i], object_size[i])) # 这里xy是需要标记的坐标，xytext是对应的标签坐标
plt.ylabel('方框平均大小',fontdict={'fontsize':18,'color':'black'})
plt.xlabel('对象个数',fontdict={'fontsize':18,'color':'black'})
plt.show()

# #作条形图
# #排序
# numbers=numbers.tolist()#将numpy转换为list
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j] <numbers[j+1]:
#             numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
#             names[j],names[j+1]=names[j+1],names[j]

# plt.bar(names, #x轴数据
#         numbers,  #y轴数据
#         align ='center', #设置条形的中心位置在中间，edge为边缘
#         color=colors2, # 颜色
#         alpha = 0.8,   # 透明度  越小颜色越淡
#         width = 0.6)
# #坐标轴和标题名称
# plt.ylabel("数量",fontdict={'fontsize':18,'color':'black'})
# plt.xlabel("名称",fontdict={'fontsize':16,'color':'black'})
# plt.title("各对象数量统计",fontdict={'fontsize':18,'color':'black'})
# for x,y in enumerate(numbers):
#     plt.text(x,y,'%s' %round(y,1),ha='center',fontdict={'fontsize':12,'color':'black'})
# plt.grid(True)
# plt.show()

