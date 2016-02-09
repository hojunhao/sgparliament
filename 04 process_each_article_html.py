# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 17:31:03 2016

@author: Vivobook
"""
import os
import re
from lxml import html
import sys
import progressbar


def htm2tree(html_file):
    with open(html_file, "r") as input:
        raw_html = "".join(input.readlines())
    tree = html.fromstring(raw_html)
    return tree


def tree2text(tree):
    para = tree.xpath('//div[@id="showTopic"]/div/descendant::*/text()')
    para = [p.replace("\n", " ") for p in para]
    text_only = "\n".join(para)
    return text_only


def save_text(text, save_file_path):
    with open(save_file_path, "wb") as output:
        output.writelines(text_only)
    pass


def remove_title_block(text, filename):
    result = re.match("Parliament No:", text)
    if result:
        # get topic from filename
        topic_match = filename[9:150].replace("(", ".").split(".")[0]
        # need to remove all text till second topic
        pattern = "^Parliament No:.*?" + \
                  topic_match + \
                  ".*?(?=" + topic_match + ")"
        return re.sub(pattern, "",
                      text_only,
                      flags=re.DOTALL | re.IGNORECASE)
    else:
        return text

# target directory
folder_path = "D:/workspace/scrap_sg/article_12_13/"
save_folder = "D:/workspace/scrap_sg/article_text/"

dirs = os.listdir(folder_path)
max_counter = len(dirs)

# initiate progress bar
bar = progressbar.ProgressBar(maxval=len(dirs),
                              widgets=[progressbar.Bar('=', '[', ']'),
                                       ' ',
                                       progressbar.Percentage()])

bar.start()

counter = 0
for d in dirs:
    sys.stdout.write('\r')
    bar.update(counter+1)
    filename = folder_path + d
    tree = htm2tree(filename)
    text_only = tree2text(tree)
    text_only = remove_title_block(text_only, d)
    save_path_name = save_folder + d.split(".")[0]+".txt"
    save_text(text_only, save_path_name)
    counter += 1


bar.finish()


# reasonable portion match
d = dirs[6]
filename = folder_path + d

tree = htm2tree(filename)
text_only = tree2text(tree)
text_only

topic_match = d[9:150].replace("(", ".").split(".")[0]
topic_match

# remove meta data
result = re.match("Parliament No:", text_only)
if result:
    pattern = "^Parliament No:.*?" + "(?=" + topic_match + ")"
    text_only_cleaned = re.sub(pattern, "", text_only, flags= re.DOTALL|re.IGNORECASE)    
    print "test"



result.group(0)
len(text_only)
len(text_only_cleaned)



















