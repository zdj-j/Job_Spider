# @time:2020/10/9 10:40
# Author:Small-J
# 该文件为招聘岗位福利词云图

from cleaning_data import data
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud


def welfared_data(data):
    """处理招聘岗位福利的数据"""
    df_data = data[data['title'] == 'Python开发工程师']
    welfare = df_data['welfare']
    welfare = ''.join(welfare)
    welfare_list = [i for i in welfare.split(' ')]
    welfare_data = pd.Series(welfare_list).value_counts()

    # 系列数据项，[(word1, count1), (word2, count2)] --> 绘制词云图需要的数据
    word1 = list(welfare_data.index)
    count1 = list(welfare_data.values)
    word1 = [str(i) for i in word1]
    count1 = [int(i) for i in count1]
    word_data = [i for i in zip(word1, count1)]
    return word_data


def welfared_word_counts(word_data):
    """绘制词云图"""
    c = (
        WordCloud().add(series_name="Python开发工程师福利图", data_pair=word_data, word_size_range=[12, 66]).set_global_opts(title_opts=opts.TitleOpts(title="Python开发工程师福利图", title_textstyle_opts=opts.TextStyleOpts(font_size=30)), tooltip_opts=opts.TooltipOpts(is_show=True),
    ))
    return c


def welfared_word_run():
    word_data = welfared_data(data())
    word_cloud = welfared_word_counts(word_data)
    return word_cloud
