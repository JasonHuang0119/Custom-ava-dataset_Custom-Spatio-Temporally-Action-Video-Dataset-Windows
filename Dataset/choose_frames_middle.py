import os
import shutil
import sys

# 遍历 ./choose_frames
for filepath, dirnames, filenames in os.walk(r'./choose_frames'):
    if len(filenames) == 0:
        continue

    # 在 choose_frames 下创建对应的目录文件夹
    temp_name = os.path.basename(filepath)
    path_temp_name = os.path.join('./choose_frames_middle', temp_name)
    if not os.path.exists(path_temp_name):
        os.makedirs(path_temp_name)
        print(path_temp_name)
    filenames = sorted(filenames)

    # 找到指定的图片，然后移动到 choose_frames 中对应的文件夹下
    for filename in filenames:
        if "checkpoint" in filename or "Store" in filename:
            continue
        temp_num = filename.split('_')[1].split('.')[0]
        temp_num = int(temp_num)

        if (temp_num - 1) / 30 <= 1 or (temp_num - 1) / 30 >= len(filenames) - 2:
            continue
        temp_num = str(temp_num).zfill(6)
        temp_num = temp_name + "_" + temp_num + ".jpg"

        srcfile = os.path.join(filepath, temp_num)
        dstpath = os.path.join(path_temp_name, temp_num)

        # 如果目标文件已存在，则删除
        if os.path.exists(dstpath):
            os.remove(dstpath)

        # 复制文件
        shutil.copy(srcfile, dstpath)
