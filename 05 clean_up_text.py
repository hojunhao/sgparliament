# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 00:42:08 2016

@author: Vivobook
"""
# remove unwanted articles
import os
import re


folder_path = "D:/workspace/scrap_sg/article_text/"

# change current directory to folder path
os.chdir(folder_path)

# list files in current directory
dirs = os.listdir(".")
dirs_remove = [d for d in dirs if re.search("ADJOURNMENT", d)]

for file in dirs_remove:
    os.remove(file)
