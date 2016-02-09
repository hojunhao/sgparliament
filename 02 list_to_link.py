# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 14:28:39 2016

@author: Vivobook
"""

import urllib
import re
import csv
from lxml import html


def parse_each_from_lst(el, re_split):
    """
    Pre-format each raw item in lst
    """
    el = el[31:-1]
    el = re_split.split(el)
    return el


def remove_comma_blank(l):
    """
    Take a raw list and output a list with comma and blanks items removed
    """
    output = []
    for i in l:
        if i != "" and i != ",":
            output.append(i)
    return output


def parse_to_parm_dict(l):
    """
    Take a formatted list, return an dictionary of parameter from listing page
    """
    parms = {}
    parms['currentPubID'] = l[0]
    parms['currentTopicID'] = l[1]
    parms['topicKey'] = l[2]
    topic = l[3]
    date = l[4]
    return [date, topic, parms]


def encode_url_w_parms(url, parms):
    """
    Take main url and parms and encode them as valid link
    """
    url_parms = urllib.urlencode(parms)
    return url + "?" + url_parms


# for each el in lst parse output as list [date, topic, link]
def parse_each_el_in_lst(el, re_split, q_url):
    el = parse_each_from_lst(el, re_split)
    el = remove_comma_blank(el)
    date, topic, parms = parse_to_parm_dict(el)
    link = encode_url_w_parms(q_url, parms)
    return [date, topic, link]


def html_to_lst(html_file):
    """
    Take a listing html file and return articles details
    """
    with open(html_file, "r") as input_file:
        h = input_file.read()
    tree = html.fromstring(h)
    return tree.xpath("//div/a/@onclick")


def append_parsed_to_article_listing(article_list_path,
                                     lst, split_by, q_url):
    with open(article_list_path, "ab") as f_art_list:
        writer = csv.writer(f_art_list)
        for el in lst:
            try:
                writer.writerow(parse_each_el_in_lst(el, split_by, q_url))
            except:
                print "----------------ERROR-------------------"
                print el
                print "----------------------------------------"

# Loop through 450 files download
folder_path = "D:/workspace/scrap_sg/listing/"

# variables for for loop below
split_by = re.compile(r"(?<!\\)'")
q_url = 'http://sprs.parl.gov.sg/search/topic.jsp'
save_folder = "D:/workspace/scrap_sg/article/"
article_list_file = "article_list.csv"
article_list_path = save_folder + article_list_file

# clear all article listing, write header
with open(article_list_path, "wb") as f_art_list:
    writer = csv.writer(f_art_list)
    writer.writerow(["DATE", "TOPIC", "LINK"])

for i in range(1, 451):
    # select input listing file
    file_path = folder_path+"Page" + str(i) + ".html"
    print file_path
    # parse html to links details
    lst = html_to_lst(file_path)
    append_parsed_to_article_listing(article_list_path,
                                     lst,
                                     split_by,
                                     q_url)

# returned 3 errors
# manually checked that those are invalid links



















































#driver = webdriver.Firefox()
#driver.get(q_url_parms)
#
#element = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.CLASS_NAME, "hansardContent"))
#    )
#    
#pg_source = driver.page_source.encode("ascii", "ignore")
#file_path = article_path + "1"
#with open(file_path, "w") as output:
#        output.write(driver.page_source.encode("ascii", "ignore"))
#r.text
#print(r.url)
