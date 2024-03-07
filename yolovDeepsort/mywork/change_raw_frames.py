
import os
import shutil

# 设置源文件夹和目标文件夹的路径
source_dir = "../../Dataset/frames"
target_dir = "../../Dataset/rawframes"

# 遍历源文件夹中的所有子文件夹和文件
for root, dirs, files in os.walk(source_dir, topdown=False):
    for name in files:
        # 忽略一些特定的文件
        if 'checkpoint' in name or "Store" in name:
            continue
        
        # 获取原始文件夹的名称
        folder_name = os.path.basename(root)
        # 创建目标子文件夹（如果不存在）
        target_subdir = os.path.join(target_dir, folder_name)
        if not os.path.exists(target_subdir):
            os.makedirs(target_subdir)
        
        # 构建源文件和目标文件的完整路径
        oldNamePath = os.path.join(root, name)
        tempName1 = name.split('_')[1]
        tempName2 = tempName1.split('.')[0]
        tempName3 = str(int(tempName2)).zfill(5)
        newName =  'img_' + tempName3 + '.jpg'
        newNamePath = os.path.join(target_subdir, newName)

        # 复制文件
        shutil.copy2(oldNamePath, newNamePath)