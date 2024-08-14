import csv
import re
from collections import Counter

# 指定輸入和輸出文件路徑  #這個路徑要修改成自己的
input_file_path = './train_without_personID.csv'
output_file_path = './ava_v2.2_cow_sorted.csv'

# 正規表達式來提取字母和數字部分
def extract_alpha_numeric(value):
    letters = re.findall(r'\D+', value)[0] if re.findall(r'\D+', value) else ''
    digits = int(re.findall(r'\d+', value)[0]) if re.findall(r'\d+', value) else 0
    return letters, digits

# 打開輸入文件並讀取內容
with open(input_file_path, 'r') as input_file:
    # 使用csv.reader讀取CSV文件
    reader = csv.reader(input_file)
    # 過濾掉空行
    reader = [row for row in reader if len(row) > 1]  # 確保至少有兩個欄位

    # 將數據按照第一列和第二列進行排序
    sorted_data = sorted(reader, key=lambda x: (extract_alpha_numeric(x[0]), int(x[1])))

# 打開輸出文件並寫入處理後的內容
with open(output_file_path, 'w', newline='') as output_file:
    # 使用csv.writer寫入CSV文件
    writer = csv.writer(output_file)
    # 遍歷排序後的數據並寫入輸出文件
    for row in sorted_data:
        # 在每一行末尾添加",1"
        row.append('1')
        # 寫入輸出文件
        writer.writerow(row)

print(f'處理完成，已將結果寫入到 {output_file_path}')

