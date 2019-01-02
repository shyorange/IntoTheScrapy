# -*- coding=utf-8 -*-
# __author__ : "shyorange"
# __date__ :  2019/1/2
"""
url管理器（管理所有的url）
"""

class UrlManager:

    def __init__(self):
        self.new_urls = set(); # 未爬取的url集合
        self.old_urls = set(); # 已爬取的url集合

    def add_new_url(self,url):
        """
        添加url
        :param url:
        :return:
        """
        pass;

    def get_new_url(self):
        """
        获得当前爬取的url
        :return:
        """
        pass;

    def has_new_url(self):
        """
        判断集合中是否还有url
        :return:
        """
        pass;

    def add_new_urls(self,urls):
        """
        添加进一个页面内的多个url
        :param urls:列表形式
        :return:
        """
        pass;