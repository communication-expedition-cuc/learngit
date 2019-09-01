# coding: utf-8
from selenium import webdriver
import time
import unicodecsv

"""
note: 需要使用selenium，chrome版本需要与chromedriver版本对应。具体见https://chromedriver.storage.googleapis.com/
"""

def login(username, password):
    #打开微信公众号登录页面
    driver.get('https://mp.weixin.qq.com/')
    driver.maximize_window()
    time.sleep(3)
    # 自动填充帐号密码
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[1]/div[1]/div/span/input").clear()
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[1]/div[1]/div/span/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[1]/div[2]/div/span/input").clear()
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[1]/div[2]/div/span/input").send_keys(password)

    time.sleep(1)
    #自动点击登录按钮进行登录
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[4]/a").click()
    # 拿手机扫二维码
    time.sleep(15)


def get_url_title(html):
    lst = []
    for item in driver.find_elements_by_class_name('weui-desktop-mass__item'):
        state = item.find_element_by_xpath(".//span[@class='js_status_txt weui-desktop-dropdown-helper']").text
        if state == '发送完毕':
            temp_dict = {
                'date': item.find_element_by_xpath(".//em[@class='weui-desktop-mass__time']").text,
                'url': item.find_element_by_tag_name('a').get_attribute('href'),
                'title': item.find_element_by_xpath(".//a[@class='weui-desktop-mass-appmsg__title']/span").text,
                'read_num': item.find_element_by_xpath(".//span[@class='weui-desktop-mass-media__data__inner']").text,
                'reading': item.find_element_by_xpath(".//div[@class='weui-desktop-mass-media__data appmsg-haokan']/span").text,
            }
            lst.append(temp_dict)
    return lst



#用webdriver启动谷歌浏览器，记得修改路径哈
driver = webdriver.Chrome()

#这个需要通过管理员扫码，可以用自己或朋友的微信公众号试试看
nickname = '中国传媒大学'# 公众号名称，想查谁都行
username = 'Lara1999@qq.com'# 账号
password = 'Lara1999' # 密码

login(username, password)
page_num = int(driver.find_elements_by_class_name('weui-desktop-pagination__num')[-1].text.split('/')[-1].lstrip())

# 点击下一页
url_title_lst = get_url_title(driver.page_source)

for _ in range(1, page_num):
    try:
        #if _ == 1:
        print("第一页")
        pagination = driver.find_elements_by_class_name('weui-desktop-pagination')
        print("第二页")
        pagination.find_elements_by_tag_name('a').click()
        #else:
            #print("翻页")
            #driver.find_element_by_xpath(".//a[@class='weui-desktop-btn weui-desktop-btn_default weui-desktop-btn_mini']")[2].click()
        print("---------")
        time.sleep(6)#如果这里数值太小很可能会导致操作频繁不能抓取
        url_title_lst += get_url_title(driver.page_source)
    except:
        print("第{}页失败".format(_))
        break

#print(url_title_lst)
#将结果写入csv文件
with open('test_articles.csv',"wb+") as f:
    writer = unicodecsv.writer(f)
    writer.writerow(['date','url','title','read_num','reading'])
    for item in url_title_lst:
        writer.writerow([item['date'],item['url'],item['title'],item['read_num'],item['reading']])
f.close()

