import csv
import re

def custom_sort_key(index):
    # 將字符串分為字母和數字兩部分，如果是純數字，則直接轉換為數字
    match = re.match(r"([a-zA-Z]*)([0-9]*)", index)
    if match:
        prefix = match.group(1)
        num_part = match.group(2)
        if num_part.isdigit():
            return (prefix, int(num_part))
        else:
            return (prefix, 0)
    return (index, 0)

# 讀取CSV文件
input_csv_path = '/home/jason/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-main/Dataset/ava_v2.2_cow_sorted.csv'
indices = set()

with open(input_csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        index = row[0]
        indices.add(index)

# 將索引轉換為排序列表
sorted_indices = sorted(indices, key=custom_sort_key)

# 生成數據
data = []
for i in sorted_indices:
    for j in range(1, 481):
        img_number = str(j).zfill(5)
        file_name = f'{i}/img_{img_number}.jpg'
        # 將數字部分從索引中分離出來，並計算新的索引值
        match = re.match(r"([a-zA-Z]*)([0-9]+)", i)
        if match:
            prefix = match.group(1)
            num = int(match.group(2))
            new_index = f'{prefix}{num-1}'
        else:
            new_index = int(i) - 1 if i.isdigit() else i
        data.append([str(i), str(new_index), str(j-1), file_name, ''])  # 在每個子列表的最後添加空字符串

# 寫入CSV文件
output_csv_path = '/home/jason/YOWOv2/dataset/AVA_Dataset/frame_lists/train2.csv'
with open(output_csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')

    # 寫入數據
    csvwriter.writerows(data)

