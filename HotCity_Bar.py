# @time:2020/10/9 1:55
# Author:Small-J
# 该文件为热门行业Top10

from cleaning_data import data
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


def hot_city_data(data):
    """热门行业Top10数据"""
    df_data = data[data['title'] == 'Python开发工程师']
    workplace_data = list(df_data['industry'])
    workplace_data = [workplace.split('-')[0] for workplace in workplace_data]
    # 变成DataFrame类型
    df = pd.Series(workplace_data)
    df_data = df.value_counts()[:10]
    # x轴数据
    industry_x = list(df_data.index)
    # y轴数据
    industry_y = list(df_data)
    return industry_x, industry_y


def hot_city_bar(df_data):
    """绘制热门行业Top10"""
    x = df_data[0]
    y = df_data[1]

    bar = Bar(init_opts=opts.InitOpts(width='720px', height='320px', theme=ThemeType.LIGHT))

    bar.add_xaxis(xaxis_data=x[::-1])
    bar.add_yaxis(series_name='热门行业的用人需求Top10', yaxis_data=y[::-1])
    bar.set_global_opts(
        # reversal_axis : 是否反向坐标轴
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(),),
        # range_start : 开始值  百分之零到百分百
        # range_end : 结束值
        datazoom_opts=opts.DataZoomOpts(is_show=True, range_start=0, range_end=100),
        # tooltip_opts=opts.ToolBoxFeatureOpts()
        toolbox_opts=opts.ToolboxOpts(is_show=True)
    )
    bar.reversal_axis()
    return bar


def hot_city_run():
    """程序入口"""
    df_data = hot_city_data(data())
    bar = hot_city_bar(df_data)
    return bar


