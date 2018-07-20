# coding: UTF-8
import random
_NUM_VALIDATION = 1000   # 验证集的数量
_RANDOM_SEED = 0        # 随机种子
list_path = 'list.txt'  # 文件列表
train_list_path = 'list_train.txt'  # 生成的训练数据文件
val_list_path = 'list_val.txt'      # 生成的验证数据文件

fd = open(list_path)
lines = fd.readlines()              # 读取所有的行
fd.close()
random.seed(_RANDOM_SEED)           # 设置随机种子
random.shuffle(lines)               # 随机调整顺序
fd = open(train_list_path, 'w')     # 写入验证集
for line in lines[_NUM_VALIDATION:]:
    fd.write(line)
fd.close()
fd = open(val_list_path, 'w')       # 写入测试集
for line in lines[:_NUM_VALIDATION]:
    fd.write(line)
fd.close()
