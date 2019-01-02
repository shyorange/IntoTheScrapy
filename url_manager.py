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
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url);

    def get_new_url(self):
        """
        获得当前爬取的url
        :return:
        """
        new_url = self.new_urls.pop();
        self.old_urls.add(new_url);
        return new_url;

    def has_new_url(self):
        """
        判断集合中是否还有url
        :return:
        """
        return len(self.new_urls);

    # 批量添加连接
    def add_new_urls(self,urls):
        """
        添加进一个页面内的多个url
        :param urls:{list}
        :return:
        """
        assert urls is not None,"传入的urls为空。"
        for url in urls:
            self.add_new_url(url);