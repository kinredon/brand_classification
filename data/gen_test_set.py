# coding: UTF-8
import os
import random
# 类别名称对应类别号
# class_names_to_ids = {'daisy': 0, 'dandelion': 1, 'roses': 2, 'sunflowers': 3, 'tulips': 4}
data_dir = 'vehicle/'     # 图片目录
output_path = 'test.txt'        # 输出文件
_NUM_VALIDATION = 1000   # 验证集的数量
_RANDOM_SEED = 0        # 随机种子

class_names_to_ids = {}
class_names = os.listdir(data_dir)
f = open('labels.txt', 'w')
count = 0
for i in range(0, len(class_names)):
    if os.path.isdir(data_dir + class_names[i]):
        class_names_to_ids[class_names[i]] = count
        count = count + 1
        f.write(class_names[i] + '\n')
f.close()

count = 0
fd = open(output_path, 'w')     # 文件句柄
# 将图片地址与类别一一对应，并写入文件中
for class_name in class_names_to_ids.keys():
    if os.path.isdir(data_dir + class_name):
        images_list = os.listdir(data_dir + class_name)
        random.seed(_RANDOM_SEED)           # 设置随机种子
        random.shuffle(images_list)               # 随机调整顺序
        for image_name in images_list:
            if image_name.split('.')[-1] in ['jpeg', 'png', 'jpg']:
                fd.write('{}/{} {}\n'.format(class_name, image_name, class_names_to_ids[class_name]))
                count = count + 1
                if count == 50:
                    break
    count = 0
fd.close()
