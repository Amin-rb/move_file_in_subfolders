# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:16:29 2024

@author: Amin
"""

import os
import shutil

input_folder = "C:/Users/Amin/Desktop/Face/women"
output_folder = "C:/Users/Amin/Desktop/Face/women_new_wednesday"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(input_folder)

image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg','.gif'))]

for index, filename in enumerate(image_files, start=1):  # start=86773
    old_path = os.path.join(input_folder, filename)
    
    new_filename = f"{index}{os.path.splitext(filename)[1]}"
    new_path = os.path.join(output_folder, new_filename)
    
    shutil.copy(old_path, new_path)

print("تمام فایل‌ها تغییر نام داده شده و در فولدر جدید ذخیره شدند.")

