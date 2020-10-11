# @time:2020/10/9 0:53
# Author:Small-J
# 该文件为数据清洗之后的结果

import pymysql
import pandas as pd


def mysql_connect():
    """数据连接"""
    connect = pymysql.connect('localhost', 'root', 'root', 'data')
    cursor = connect.cursor()
    cursor.execute('select * from search_data')
    content = cursor.fetchall()
    return content


def clean_data(content):
    """数据清洗"""
    df = pd.DataFrame(data=content, columns=['title', 'company_name', 'salary', 'date_of_issue', 'company_type', 'welfare',
                                          'workplace', 'experience', 'education', 'recruit_number', 'company_number',
                                          'industry', 'detail_url', 'company_url'])

    # print("去重之前的记录数", df.shape)  # 去重之前的记录数 (19500, 14)
    # 记录去重
    df.drop_duplicates(subset=["title", "company_name", "workplace"], inplace=True)
    # 去重之后的记录数
    # print("去重之后的记录数", df.shape)  # 去重之后的记录数 (18783, 14)
    return df


def data():
    """返回清洗后的数据"""
    content = mysql_connect()
    data = clean_data(content)
    return data