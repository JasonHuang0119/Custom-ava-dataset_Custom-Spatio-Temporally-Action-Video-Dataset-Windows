import os
import shutil
import sys

# 传参 这里传入视频多少秒
seconds = int(sys.argv[1])

# 传参 这里传入视频从哪一秒开始，这里需要设置为 0
start = int(sys.argv[2])

# 需要检测标注的时间位置
frames = range(start, seconds + 1)

# num_frames 存放对应图片的编号
num_frames = [i * 30 + 1 for i in frames]

# 遍历 ./frames
for filepath, dirnames, filenames in os.walk(r'./frames'):
    # 在 choose_frames 下创建对应的目录文件夹
    if filenames:
        temp_name = os.path.basename(filepath)
        path_temp_name = os.path.join('./choose_frames', temp_name)
        if not os.path.exists(path_temp_name):
            os.makedirs(path_temp_name)
    filenames = sorted(filenames)
    # 找到指定的图片，然后移动到 choose_frames 中对应的文件夹下
    for filename in filenames:
        if "checkpoint" in filename or "Store" in filename:
            continue
        frame_num = int(filename.split('_')[1].split('.')[0])
        if frame_num in num_frames:
            temp_num = f"{frame_num:06}"
            srcfile = os.path.join(filepath, filename)
            dstfile = os.path.join(path_temp_name, f"{temp_name}_{temp_num}.jpg")
            shutil.copy(srcfile, dstfile)
