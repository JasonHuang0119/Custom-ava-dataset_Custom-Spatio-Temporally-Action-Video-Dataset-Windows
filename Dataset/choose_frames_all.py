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
    filenames = sorted(filenames)
    temp_name = os.path.basename(filepath)  # 使用 os.path.basename 获取最后一级的目录名
    for filename in filenames:
        if "checkpoint" in filename or "Store" in filename:
            continue
        frame_num = int(filename.split('_')[1].split('.')[0])
        if frame_num in num_frames:
            temp_num = f"{frame_num:06}"  # 使用 f-string 格式化数字，填充为 6 位
            srcfile = os.path.join(filepath, filename)  # 使用 os.path.join 拼接路径
            dstfile = os.path.join('./choose_frames_all', f"{temp_name}_{temp_num}.jpg")
            shutil.copy(srcfile, dstfile)
