# @time:2020/10/9 2:18
# Author:Small-J
# 该文件为Python开发工程师学历数据

from cleaning_data import data
import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts


def education_data(data):
    """获取Python开发工程师学历数据"""
    df_data = data[data['title'] == 'Python开发工程师']
    education_list = list(df_data['education'])
    education = [education.split('-')[0] for education in education_list]
    education = [i.replace('无需经验', '高中').replace(' ', '高中').replace('2年经验', '硕士').replace('3', '硕士') for i in education]
    df = pd.Series(education).value_counts()
    return df


def education_pie(df_data):
    """绘制饼状图"""
    # 为什么要进行数据转换呢？因为饼图需要数据是对应的列表数据对应列表数据类型
    x_data = list(df_data.index)
    y_data = list(df_data)
    data = [data for data in zip(x_data, y_data)]

    # 绘制饼图
    pie = Pie()
    pie.add(series_name='学历占比', data_pair=data)
    return pie


def education_run():
    """主程序入口"""
    df_data = education_data(data())
    pie = education_pie(df_data)
    return pie
