from selenium import webdriver
import time

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
path = "urls_data.txt"
start_urls = ['http://www.ajxxgk.jcy.gov.cn/html/zjxflws/%d.html' % i for i in range(2, 10)]
# url1 = "http://www.ajxxgk.jcy.gov.cn/html/zjxflws/index.html"
url_list = []
for url in start_urls:
    browser.get(url)
    time.sleep(5)
    # browser.execute_script("document.getElementsByClassName('ctitle')[0].children[1].click();")
    urls = browser.find_elements_by_xpath("//div[contains(@class,'ajh')]//a")
    time.sleep(5)

    for ur in urls:
        href = ur.get_attribute('href')
        title = ur.get_attribute('title')
        url_list.append(href + "|" + title)
text = '\n'.join(url_list)
f = open(path, "w")
f.write(text)
f.close()
browser.close()
