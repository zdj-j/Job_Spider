# @time:2020/10/8 23:18
# Author:Small-J

import grequests
import re
from bs4 import BeautifulSoup
import requests
import pymysql

# 该文件为前程无忧详情页数据

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Referer': 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
    'Host': 'search.51job.com',
    'Cookie': 'guid=60172f6ee7023d13eb83dd29e13b8937; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; adv=adsnew%3D0%26%7C%26adsnum%3D2004282%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.0f0000jqGlpYpEfj9lynK-vVDEa3_-UBknjKNZHv564Y0vKZl1HuJ_R-N5IL15bSOcsJosb0q_Wo1wF7Mii9F4LBsYH6hifvw5UTUvZh0TroPLYKL42KMGH5tJOnLTudJaV-clfQLAHbrn-lE-uvr8XEa5AJfP0Q9SG7oEV1K66Fex_tGJnLhWFXaTAcrvFuHX7BWo1QI_9Zp9lmohEKj_mDk-9j.DR_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_uQQr1F_zIyT8P9MqOOgujSOODlxdlPqKMWSxKSgqjlSzOFqtZOmzUlZlS5S8QqxZtVAOtIOtHOuS81wODSgL35SKsSXKMqOOgfESyOHjGLY51xVOeNH5exS88Zqq1ZgVm9udSnQr1__oodvgvnehUrPL72xZgjX1IIYJN9h9merzEuY60.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqkea11neXYtT0IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqkea11neXYtT0ThPv5HD0IgF_gv-b5HDdnW0zPH61P100UgNxpyfqnHnsnW6Lnj00UNqGujYknjTkPHf3PsKVIZK_gv-b5HDkPHnY0ZKvgv-b5H00pywW5fKWThnqn1Tdrjb%2526dt%253D1599548539%2526wd%253D%2525E5%252589%25258D%2525E7%2525A8%25258B%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2526tpl%253Dtpl_11534_22836_18980%2526l%253D1520258370%26%7C%26; slife=lowbrowser%3Dnot%26%7C%26; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B4%F3%CA%FD%BE%DD%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAPython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAPython%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%601%7C%21; m_search=keyword%3D%E5%A4%A7%E6%95%B0%E6%8D%AE%26%7C%26areacode%3D000000; partner=www_baidu_com; 51job=cenglish%3D0%26%7C%26'
}

# 数据库连接
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='data')
cursor = conn.cursor()


def get_url():
    """构建一个url列表"""
    url_list = [grequests.get(f'https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{page}.html', headers=headers) for page in range(1, 45)]
    # response_list: 返回的结果为一个请求列表
    response_list = grequests.map(url_list)
    return response_list


def detail_url(response):
    """获取详情数据"""

    html = response.text
    data_str = re.findall(r'window.__SEARCH_RESULT__ = (.*?)</script>\r\n<div class="clear"></div>\r\n',
                          html, re.S)
    data_str = ''.join(data_str).replace('\\', '').replace('[', '').replace(']', '')
    reg1 = re.compile(
        r'"job_href":"(.*?)"', re.S)
    content_list = re.findall(reg1, data_str)
    for content in content_list:
        response = requests.get(content, headers=headers)
        response.encoding = 'gbk'
        html = response.text
        try:
            bs = BeautifulSoup(html, "lxml").find("div", class_="bmsg job_msg inbox").text
            s = bs.replace("微信", "").replace("分享", "").replace("邮件", "").replace("\t", "").strip()
            job_describe = ''.join(s).strip()  # 把数据转换成字符串类型并去除空格
            pattern = re.compile('[^\u4e00-\u9fa50-9]')  # 中文的编码范围是：\u4e00到\u9fa5
            job_describe = "".join(pattern.split(job_describe)).strip()
            print(job_describe)
            sql = 'insert into ciyun(data) values (%s)'
            cursor.execute(sql, job_describe)
            conn.commit()
        except AttributeError as E:
            print('%s' % E)



def main():
    response_list = get_url()
    for response in response_list:
        detail_url(response)


if __name__ == '__main__':
    main()
