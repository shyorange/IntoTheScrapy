# -*- coding=utf-8 -*-
# __author__ : "shyorange"
# __date__ :  2019/1/2
"""
仅仅用于测试的文件
"""
from html_downloader import HtmlDownloader

# 测试下载器
def test_download():
    downloader = HtmlDownloader();
    print(downloader.download("https://baike.baidu.com/item/%E6%8C%AA%E5%A8%81/167133?fr=aladdin"));


if __name__ == '__main__':
    test_download();