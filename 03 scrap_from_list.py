# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 15:58:40 2016

@author: Vivobook
"""

import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def format_filename(lst):
    """
    Generate filename for saving each article
    """
    u_date_split = lst[0].split('-')
    f_date = u_date_split[2] + u_date_split[1] + u_date_split[0]
    f_topic = re.sub(r"[^0-9A-Z ()]", "", lst[1], flags=re.IGNORECASE)
    len_f_topic = len(f_topic)
    #windows can only accept path name shorter than 255
    if len_f_topic > 200:
        f_topic = f_topic[0:199]
        print f_topic
    return f_date + " " + f_topic + ".html"


def download_html_from_link(link):
    driver.get(link)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "showResult"))
        )
        time.sleep(1)
        return driver.page_source.encode("ascii", "ignore")
    except:
        return False


def process_each_row(row, folder_path):
    save_file_name = format_filename(row)
    save_file_path = folder_path + save_file_name
    dled_html = download_html_from_link(row[2])
    if dled_html:
        with open(save_file_path, "w") as output:
            output.write(dled_html)

# input file
scrap_list = 'D:/workspace/scrap_sg/article/article_list.csv'

# where to save the output files
folder_path = "D:/workspace/scrap_sg/article_html/"

# start driver
driver = webdriver.Firefox()

# main loop: process each row
with open(scrap_list, "r") as input_file:
    reader = csv.reader(input_file, delimiter=",", quotechar='"')
    reader.next()
    print "____________________________"
    counter = 1
    for row in reader:
        print counter
        counter = counter + 1
        print row
        process_each_row(row, folder_path)
        
# stop at
        