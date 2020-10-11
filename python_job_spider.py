# @time:2020/10/8 18:17
# Author:Small-J

# 该文件为前程无忧异步爬虫

import grequests
import re
import pymysql


# 请求头
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
    url_list = [
        grequests.get(f'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{page}.html', headers=headers)
        for page in range(200, 400)]
    # response_list: 返回的结果为一个请求列表
    response_list = grequests.map(url_list)
    return response_list


def parsing_data(response):
    """解析数据"""
    """
    字段说明:
    {'detail_url': 详情url, 'title': 岗位名称, 'company_url': '公司url',
    'company_name': '公司名称', 'salary': '工资', 'date_of_issue': '更新时间',
    'company_type': '公司类型', 'welfare': '福利', 'workplace':'工作地点',
    'experience': '经验', 'education':'学历', 'recruit_number': '招人数'
    'company_number' : '公司人数', 'industry': '行业'

    }
    """
    html = response.text
    data_str = re.findall(r'window.__SEARCH_RESULT__ = (.*?)</script>\r\n<div class="clear"></div>\r\n',
                          html, re.S)
    data_str = ''.join(data_str).replace('\\', '').replace('[', '').replace(']', '')
    reg1 = re.compile(
        r'"job_href":"(.*?)","job_name":"(.*?)".*?"company_href":"(.*?)","company_name":"(.*?)","providesalary_text":"(.*?)".*?"updatedate":"(.*?)".*?,"companytype_text":"(.*?)".*?"jobwelf":"(.*?)".*?"attribute_text":"(.*?)","companysize_text":"(.*?)","companyind_text":"(.*?)"',
        re.S)
    content_list = re.findall(reg1, data_str)
    item = {}
    for content in content_list:
        item['detail_url'] = content[0]
        item['title'] = content[1]
        item['company_url'] = content[2]
        item['company_name'] = content[3]
        item['salary'] = content[4]
        item['date_of_issue'] = content[5]
        item['company_type'] = content[6]
        item['welfare'] = content[7]
        item['workplace'] = content[8].split(',')[0].replace('"', '')
        item['experience'] = [content[8].split(',')[1] if len(content[8].split(',')) == 4 else ''][0].replace('"', '')
        field = content[8].split(',')
        education = []
        if len(field) == 4:
            education.append(field[2])
        elif len(field) == 3:
            education.append(field[1])
        elif len(field) == 2:
            education.append(' ')

        item['education'] = education[0].replace('"', '')
        item['recruit_number'] = field[-1].replace('"', '')
        item['company_number'] = content[9]
        item['industry'] = content[10]
        yield item


def write_mysql(data_object):
    sql = 'insert into search_data(detail_url, title, company_url, company_name, salary, date_of_issue, company_type, welfare, workplace, experience, education, recruit_number, company_number, industry) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    for data in data_object:
        print(data)
        args = (data['detail_url'], data['title'], data['company_url'], data['company_name'], data['salary'],
                data['date_of_issue'], data['company_type'], data['welfare'], data['workplace'], data['experience'],
                data['education'], data['recruit_number'], data['company_number'], data['industry'])
        cursor.execute(sql, args)
        conn.commit()


def main():
    """主程序入口"""
    response_list = get_url()
    for response in response_list:
        data_object = parsing_data(response)
        write_mysql(data_object)


if __name__ == '__main__':
    main()
