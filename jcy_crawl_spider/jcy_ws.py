from selenium import webdriver
import time

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
path = "urls_data.txt"
done_path = "done.txt"
_list = []
done_list = []
f = open(path, "r")
df = open(path, "r")
for line in f.readlines():
    _list.append(line)
for line in df.readlines():
    done_list.append(line)
f.close()
df.close()
df = open(done_path, "w")
for l in _list:
    url = l.split("|")[0]
    title = l.split("|")[1].replace("\n", "")
    if url not in done_list:
        browser.get(url)
        time.sleep(7)
        content = browser.find_elements_by_id("contentArea")
        if len(content) != 0:
            file = open("../data/wenshu/" + title + ".txt", "w", encoding="utf-8")
            file.write(content[0].text)
            file.close()
            text = url + '\n'
            df.write(text)
            df.flush()
df.close()
print("all have done!")
browser.close()
