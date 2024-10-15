# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:41:45 2024

@author: Amin
"""

import os
import shutil

def move_all_files(src_folder, dest_folder):
    # اطمینان از اینکه فولدر مقصد وجود دارد
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # پیمایش فولدر مبدا
    for root, dirs, files in os.walk(src_folder):
        # فایل‌ها را به فولدر مقصد منتقل می‌کند
        for file in files:
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_folder, file)
            shutil.move(src_file_path, dest_file_path)
        
        # فولدرها را به فولدر مقصد منتقل می‌کند
        # for dir in dirs:
        #     src_dir_path = os.path.join(root, dir)
        #     dest_dir_path = os.path.join(dest_folder, dir)
        #     shutil.move(src_dir_path, dest_dir_path)

# مسیر فولدر مبدا و مقصد
src_folder = 'C:/Users/Amin/Desktop/Face/Bollywood Actor Images'
dest_folder = 'C:/Users/Amin/Desktop/Face/test'

move_all_files(src_folder, dest_folder)
