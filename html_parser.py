# -*- coding=utf-8 -*-
# __author__ : "shyorange"
# __date__ :  2019/1/2
"""
解析器（解析网页结构）
"""
from lxml import etree;

class HtmlParser:
    def __init__(self):
        pass;

    def parse(self,content):
        """
        解析传入的网页
        :param content: 网页内容 {str}
        :return:new_hrefs {list} , data {list}
        """
        assert content is not None, "传入的content为空，请检查";
        dom = etree.HTML(content);

        pattern_title = '//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()';  # 百科的标题
        pattern_summary = '//div[@class="lemma-summary"]/div//text()'; # 百科的简介
        pattern_href = '//div[@class="main-content"]//a[@target="_blank"]/@href'; #该百科页面内的所有a标签连接

        title = dom.xpath(pattern_title)[0];
        summary = dom.xpath(pattern_summary);
        hrefs = dom.xpath(pattern_href);

        new_hrefs = ["https://baike.baidu.com"+href for href in hrefs];

        return new_hrefs,[title,"".join(summary)]
