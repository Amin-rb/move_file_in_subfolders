# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:41:45 2024

@author: Amin
"""

import os
import shutil

def move_all_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_folder, file)
            shutil.move(src_file_path, dest_file_path)
        
        # for dir in dirs:
        #     src_dir_path = os.path.join(root, dir)
        #     dest_dir_path = os.path.join(dest_folder, dir)
        #     shutil.move(src_dir_path, dest_dir_path)

src_folder = ''
dest_folder = ''

move_all_files(src_folder, dest_folder)
