# IntoTheScrapy
以百度百科为例。
目标：随便通过一个百科链接，获取该页面内的所有其他百科链接。以此类推。
html_downloader ---> Scrapy中的downloadmiddleware
html_output     ---> Scrapy中的pipeline
html_parser     ---> Scrapy中的parse方法
main            ---> Scrapy中的调度器
url_manager     ---> 同属Scrapy中的调度器（管理url）
