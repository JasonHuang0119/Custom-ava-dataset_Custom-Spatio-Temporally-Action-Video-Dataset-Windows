from via3_tool import Via3Json
import pickle
import csv
from collections import defaultdict
import os
import cv2
import sys

# 传参 ./avaMin_dense_proposals_train.pkl
avaMin_dense_proposals_path = sys.argv[1]

# 传参 ../videoData/choose_frames/
json_path = sys.argv[2]

with open(avaMin_dense_proposals_path, 'rb') as f:
    info = pickle.load(f, encoding='iso-8859-1')

attributes_dict = {
    '1': dict(aname='cow', type=2, options={
        '0': 'Lying', '1': 'Lying ruminating', '2': 'Walking', 
        '3': 'Playing', '4': 'Approaching', '5': 'Repelling', '6': 'Chasing mounting',
        '7': 'Feeding', '8': 'Standing ruminating', '9': 'Idling'
    }, default_option_id="", anchor_id='FILE1_Z0_XY1'),
}

# 获取每个视频下视频帧的数量
len_x = defaultdict(int)
for i in info:
    dirname = i.split(',')[0]
    len_x[dirname] += 1

for dirname in len_x:
    print(f"dirname: {dirname}, len_x: {len_x[dirname]}")
    
    # 为每一个视频文件创建一个via的json文件
    temp_json_path = os.path.join(json_path, dirname, f'{dirname}_proposal.json')
    
    # 获取视频有多少个帧
    num_images = 0
    img_H, img_W = 0, 0
    for root, _, files in os.walk(os.path.join(json_path, dirname)):
        if "ipynb_checkpoints" in root:
            continue
        for file in files:
            if file.endswith('.jpg'):
                num_images += 1
                if num_images == 1:
                    temp_img_path = os.path.join(root, file)
                    img = cv2.imread(temp_img_path)
                    if img is not None:
                        img_H, img_W = img.shape[:2]
    
    print(f"num_images for {dirname}: {num_images}")
    
    via3 = Via3Json(temp_json_path, mode='dump')
    vid_list = list(map(str, range(1, num_images + 1)))
    via3.dumpPrejects(vid_list)
    via3.dumpConfigs()
    via3.dumpAttributes(attributes_dict)
    
    files_dict, metadatas_dict = {}, {}
    image_id = 0
    
    for i in info:
        if i.split(',')[0] != dirname:
            continue
        
        image_id += 1
        if image_id > num_images:
            print(f"警告：image_id ({image_id}) 已超過 num_images ({num_images})")
            break
        
        files_img_num = int(i.split(',')[1])
        files_dict[str(image_id)] = dict(fname=f"{dirname}_{str(files_img_num*30+1).zfill(6)}.jpg", type=2)
        
        for vid, result in enumerate(info[i], 1):
            xyxy = result
            x1, y1 = img_W * xyxy[0], img_H * xyxy[1]
            x2, y2 = img_W * xyxy[2], img_H * xyxy[3]
            w, h = x2 - x1, y2 - y1
            
            metadata_dict = dict(
                vid=str(image_id),
                xy=[2, float(x1), float(y1), float(w), float(h)],
                av={'1': '0'}
            )
            metadatas_dict[f'image{image_id}_{vid}'] = metadata_dict
        
        via3.dumpFiles(files_dict)
        via3.dumpMetedatas(metadatas_dict)
        
        print(f"處理完成 {image_id} / {num_images}")
    
    # 处理视频末尾的空帧
    while image_id < num_images:
        image_id += 1
        files_dict[str(image_id)] = dict(fname=f"{dirname}_{str((image_id*30+1)).zfill(6)}.jpg", type=2)
        via3.dumpFiles(files_dict)
    
    # 保存视图信息
    views_dict = {vid: defaultdict(list) for vid in vid_list}
    for i, vid in enumerate(vid_list, 1):
        views_dict[vid]['fid_list'].append(str(i))
    via3.dumpViews(views_dict)
    
    # 保存 JSON 文件
    via3.dempJsonSave()
    print(f"{dirname} 處理完成並保存")

print("所有視頻處理完成")

