# -*- coding=utf-8 -*-
# __author__ : "shyorange"
# __date__ :  2019/1/2
"""
"""

class HtmlOutputer:
    def __init__(self):
        self.datas = [];

    def collect_data(self,url,data):
       self.datas.append((url,data));

    def output_html(self):
        with open("output.html","w",encoding="utf-8") as f:
            f.write(f"<html><body><table style='border=1;'><thead><tr><td>百度百科链接</td><td>简介</td></tr><thead><tbody>");
            for data in self.datas:
                f.write("<tr>");
                f.write("<td>");
                f.write(data[0]);
                f.write("</td>");
                f.write("<td>");
                f.write(data[1][0]);
                f.write("</td>");
                f.write("<td>");
                f.write(data[1][1]);
                f.write("</td>");
                f.write("</tr>");
            f.write("</tbody></table></body></html>");