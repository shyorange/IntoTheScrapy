# -*- coding=utf-8 -*-
# __author__ : "shyorange"
# __date__ :  2019/1/2
"""
网页下载器（获得网页源码）
"""
import requests;

class HtmlDownloader:

    def __init__(self):
        self.headers = {
            "Host" : "baike.baidu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer" : "https://baike.baidu.com/"
        };

    def download(self,url):
        """
        根据传入的url，获得网页源码
        :param url:
        :return:
        """
        # if 语句判断URL是否为空
        # if not url:
        #     raise ValueError("传入的url能不能为 “None”");

        # 断言判断url是否为空
        assert url is not None, "download()的url参数不能为None";

        response = requests.get(url,headers=self.headers);

        # 判断响应是否成功
        if response.status_code != 200:
            raise Exception(f"获取网页失败：{url}，code：{response.status_code}");

        return response.content.decode("utf-8");
