# @time:2020/10/9 1:19
# Author:Small-J
# 该文件为热门城市行业Top10数据

from cleaning_data import data
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts


def hot_industry_data(data):
    """热门城市行业Top10数据"""
    df_data = data[data['title'] == 'Python开发工程师']
    address_datas = list(df_data['workplace'])
    address_data = [address_data.split('-')[0] for address_data in address_datas]
    # 变成DataFram类型  #
    df = pd.Series(address_data)
    df_data = df.value_counts()[:10]
    return df_data


def hot_industry_bar(df_data):
    """绘制行业Top10数据"""
    y = list(df_data)
    x = list(df_data.index)
    # 初始化配置项
    bar = Bar(init_opts=opts.InitOpts(width='720px', height='320px'))
    # 全局配置项
    bar.set_global_opts(
        datazoom_opts=opts.DataZoomOpts(is_show=True, type_='inside')
    )
    bar.add_xaxis(xaxis_data=x)
    bar.add_yaxis(series_name='热门城市的岗位数量Top10', yaxis_data=y)
    return bar


def industry_run():
    """程序入口"""
    df_data = hot_industry_data(data())
    bar = hot_industry_bar(df_data)
    return bar



