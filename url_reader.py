from selenium import webdriver
from lxml import etree
import urllib.request
import time
import csv
import pandas as pd
from bs4 import BeautifulSoup

def openurl(url,selector):
    driver.get(url)
    time.sleep(5)
    #text = selector.xpath(".//div[@class='rich_media_content ']")[0].xpath('string(.)')
    #text = driver.find_elements_by_class_name('rich_media_content ')
    #print(text)
#    driver.close()


#driver = webdriver.Chrome()
rows = ['text','1','2','3','4','5','6','7']
oldcolumn = []
#page = driver.page_source

with open('test_articles.csv','r+', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    
    oldrow = [r for r in reader]
    #column1 = [row[1]for row in reader]
    #for i in range(1,len(column1)):
        #file = urllib.request.urlopen(oldrow[i][1])
        #data = file.read()
        #selector =  etree.HTML(page)
        #openurl(oldrow[i][1],selector)
    with open('text.csv','w',newline = '') as f:
        writer = csv.writer(f)
        for j in range(0,len(oldrow)):
            #oldcolumn = [row[j]for row in reader]
            print(oldrow[j])
            oldrow[j].append(rows[j])
            writer.writerow(oldrow[j])
    #row.append()

f.close()
csvfile.close()
