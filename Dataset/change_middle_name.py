import os
import json

root_dir = 'choose_frames_middle (copy)'

def get_new_prefix(folder):
    if not folder.startswith('Jia'):
        return f'Jia{folder}_'
    return ''

# 遍歷根資料夾中的每個子資料夾
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    if os.path.isdir(folder_path):
        new_prefix = get_new_prefix(folder)
        
        # 更新圖片名稱
        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg'):
                old_filepath = os.path.join(folder_path, filename)
                base_filename, ext = os.path.splitext(filename)
                new_filename = f'{new_prefix}{base_filename.replace("1_", "")}{ext}'
                new_filepath = os.path.join(folder_path, new_filename)
                os.rename(old_filepath, new_filepath)
                print(f'Renamed: {old_filepath} -> {new_filepath}')
        
        # 更新 JSON 文件名稱和內容
        for json_file in os.listdir(folder_path):
            if json_file.endswith('.json'):
                json_path = os.path.join(folder_path, json_file)
                
                with open(json_path, 'r') as file:
                    data = json.load(file)
                
                # 遍歷 JSON 結構並更新圖片名稱
                def update_filenames(obj):
                    if isinstance(obj, dict):
                        for key, value in obj.items():
                            if isinstance(value, str) and value.endswith('.jpg'):
                                base_filename, ext = os.path.splitext(value)
                                new_filename = f'{new_prefix}{base_filename.replace("1_", "")}{ext}'
                                obj[key] = new_filename
                            else:
                                update_filenames(value)
                    elif isinstance(obj, list):
                        for item in obj:
                            update_filenames(item)

                update_filenames(data)

                # 保存更新後的 JSON 文件
                base_json_filename = os.path.splitext(json_file)[0]
                new_json_filename = f'{new_prefix}{base_json_filename.replace("1_", "")}.json'
                
                # 檢查 JSON 文件名稱是否以"Jia"開頭，如果是就不修改
                if not json_file.startswith('Jia'):
                    new_json_path = os.path.join(folder_path, new_json_filename)
                    
                    with open(new_json_path, 'w') as file:
                        json.dump(data, file, indent=4)
                    
                    # 刪除舊的 JSON 文件
                    os.remove(json_path)
                    print(f'Updated and saved JSON: {json_path} -> {new_json_path}')

        # 如果folder名稱不是以"Jia"開頭，就重新命名
        if not folder.startswith('Jia'):
            new_folder_name = f'Jia{folder}'
            new_folder_path = os.path.join(root_dir, new_folder_name)
            os.rename(folder_path, new_folder_path)
            print(f'Renamed folder: {folder_path} -> {new_folder_path}')
