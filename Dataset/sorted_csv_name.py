import csv
import re

# 指定输入和输出文件路径   #這個路徑要修改成自己的
input_file_path = './train_without_personID.csv'
output_file_path = './ava_v2.2_cow_sorted.csv'

# 打开输入文件并读取内容
with open(input_file_path, 'r') as input_file:
    # 使用csv.reader读取CSV文件
    reader = csv.reader(input_file)
    # 将数据按照第一列进行排序
    sorted_data = sorted(reader, key=lambda x: (
    re.findall(r'\D+', x[0])[0] if re.findall(r'\D+', x[0]) else '',  # 確保有字串部分，否則返回空字串
    int(re.findall(r'\d+', x[0])[0]) if re.findall(r'\d+', x[0]) else 0,  # 確保有數字部分，否則返回 0
    int(x[1]) if x[1].isdigit() else 0))  # 確保第二列是有效的數字，否則返回 0

# 打开输出文件并写入处理后的内容
with open(output_file_path, 'w', newline='') as output_file:
    # 使用csv.writer写入CSV文件
    writer = csv.writer(output_file)
    # 遍历排序后的数据并写入输出文件
    for row in sorted_data:
        # 在每一行末尾添加",1"
        row.append('1')
        # 写入输出文件
        writer.writerow(row)

print(f'处理完成，已将结果写入到 {output_file_path}')

