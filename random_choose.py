import os
import random
import shutil

def copy_random_files(src_dir, dst_dir, num_files):
    # 获取源文件夹中的所有文件
    files = os.listdir(src_dir)
    
    # 只保留文件，过滤掉文件夹
    files = [f for f in files if os.path.isfile(os.path.join(src_dir, f))]

    # 如果要复制的文件数量大于现有文件数量，则调整数量
    num_files = min(num_files, len(files))
    
    # 随机选择文件
    selected_files = random.sample(files, num_files)
    
    # 创建目标文件夹（如果不存在）
    os.makedirs(dst_dir, exist_ok=True)
    
    # 复制选定的文件
    for file_name in selected_files:
        src_file = os.path.join(src_dir, file_name)
        dst_file = os.path.join(dst_dir, file_name)
        shutil.move(src_file, dst_file)
        print(f"Moved {src_file} to {dst_file}")

# 示例使用
src_directory = "newdata/final_data5/data_test/concert"  # 源文件夹路径
dst_directory = "newdata/final_data5/data_train/concert"  # 目标文件夹路径
number_of_files_to_copy = 613  # 要随机复制的文件数量

copy_random_files(src_directory, dst_directory, number_of_files_to_copy)