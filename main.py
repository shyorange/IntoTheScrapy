# -*- coding=utf-8 -*-
# __author__ : "shyorange"
# __date__ :  2019/1/2

"""
爬虫运行主文件
"""
import time;
import html_parser,html_downloader,html_outputer,url_manager;

# 项目入口

class SpiderMain:
    def __init__(self):
        # 将其他各个部分，作为该类的属性，便于操作
        self.url_manager = url_manager.UrlManager();
        self.downloader = html_downloader.HtmlDownloader();
        self.parser = html_parser.HtmlParser();
        self.outputer = html_outputer.HtmlOutputer();

    def crawl(self,root_url,page_count=1,time_sleep=None):
        count = 1;
        # 将起始url放入集合
        self.url_manager.add_new_url(root_url);
        # 如果集合中还有url，那么就取出该url，没有则结束
        while self.url_manager.has_new_url():
            try:
                # 获得当前正在爬取的url
                new_url = self.url_manager.get_new_url();
                print(f"正在爬取：{new_url}");
                # 获得url的源码
                html_content = self.downloader.download(new_url);
                # 获得想要的数据（该页面内的url连接，和该页面的数据）
                urls, data = self.parser.parse(html_content);
                # 将上步获得的urls放入url管理器
                self.url_manager.add_new_urls(urls);
                # 将获得的数据存入数据库
                self.outputer.collect_data(new_url,data);
                # 如果超过爬取上线，就退出
                count += 1;
                if count > page_count:
                    break;
            except Exception as e:
                print(f"爬取失败：{e}");

        # 作用暂时不明
        self.outputer.output_html();
        print("爬取结束")


if __name__ == '__main__':
    # 将百度百科挪威词条作为起始url
    ROOT_URL = "https://baike.baidu.com/item/%E6%8C%AA%E5%A8%81/167133?fr=aladdin";
    PAGE_COUNT = 5;  # 爬取的最大页数
    TIME_SLEEP = 2;  # 休眠时间

    # 启动爬虫
    spider = SpiderMain();
    spider.crawl(ROOT_URL,PAGE_COUNT,TIME_SLEEP);