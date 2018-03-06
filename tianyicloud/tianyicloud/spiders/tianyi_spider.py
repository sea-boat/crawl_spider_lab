# coding:utf-8

import scrapy
import json
import time
from json import JSONDecodeError


class TianyiSpider(scrapy.Spider):
    name = "tianyi"
    allowed_domains = ["cloud.189.cn"]
    start_urls = [
        "https://cloud.189.cn/v2/listRecycleBin.action?pageNum=2&pageSize=1000&noCache=0.2938678811261646"
    ]
    url2 = "https://cloud.189.cn/v2/deleteFile.action?noCache=0.861070738384095&fileIdList="
    TYPE = ['java', 'h', '', 'config', 'cproject', 'errlog', 'flg', 'ROOT', 'hgignore', 'gmk', 'back', 'txt', 'jasm',
            'jcod', 'icon', 'sh', 'other', 'out', 'html', 'jar', 'properties', '1', '2', '3', 'win', 'jtx', 'hgtags',
            'project', 'ksh', 'java~1~', 'xml', 'bat', 'doc', 'license', 'pdf', 'c', 'cpp', 'sln', 'dat', 'filters',
            'aps', 'rc', 'user', 'sdf', 'vcxproj', 'svn-base', 'jsp', 'css', 'class', 'js', 'bcmap', 'svg', 'eot',
            'flt', 'index', 'tld', 'woff', 'ttf', 'snap', 'ini', 'version', 'log', 'tree', 'markers', 'rss', 'xsd',
            'woff2', 'dtd', 'otf', 'psd', 'm', 'jspx', 'dia', 'xhtml', 'launch', 'dic', 'bak', 'ico', 'manifest', 'dll',
            'xsl', 'cfs', 'json', 'history', 'lst', 'cache', 'prefs', 'pom', 'zip', 'jjt', 'cc', 'py', 'jks', 'm4',
            'md', 'cfg', 'Doxyfile', 'hpp', 'db', 'exe', 'ad', 'map', 'xls', 'rtf', 'pem', 'so', 'swf', 'htm']
    cookies_k = {
        'apm_uid': '5F0A9B64F4150B4E76F0140C70CD868E',
        'apm_ua': '844F7AE4D251B2E6E152FDD13EF479F6', 'apm_ct': '20180302171607487',
        'offline_Pic_Showed': 'true', 'IS_SHOW_TREE': 'true', 'edrive_view_mode': 'icon',
        'COOKIE_WITHOUT_LOGOUT': 'COOKIE_WITHOUT_LOGOUT',
        'monitor_count': '39'}

    # override  start_requests for cookies
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], cookies=self.cookies_k, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print("deleting.................")
        try:
            json_dic = json.loads(response.text)
            # print(json_dic["data"])
            print(json_dic["recordCount"])
            print(json_dic["pageNum"])
            print(json_dic["pageSize"])
            num = len(json_dic["data"])
            i = 0
            file_id_list = ''
            while i < num:
                record = json_dic["data"][i]
                file_id = record["fileId"]
                file_type = record["fileType"]
                file_size = record["fileSize"]
                if (file_type in self.TYPE) or (file_size < 80000):
                    file_id_list += file_id
                    file_id_list += ","
                i += 1
                if i % 100 == 0:
                    file_id_list = file_id_list[0:-1]
                    print(self.url2 + file_id_list)
                    yield scrapy.Request(self.url2 + file_id_list, cookies=self.cookies_k, callback=self.parse2,
                                         dont_filter=True)
                    file_id_list = ''
            time.sleep(5)

        except JSONDecodeError:
            print("error............ ")

    def parse2(self, response):
        print("parse2......................." + response.text)
