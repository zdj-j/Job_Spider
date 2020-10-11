# @time:2020/10/9 1:53
# Author:Small-J

from HotIndustry_Bar import industry_run    # 热门行业Top10
from HotCity_Bar import hot_city_run        # 热门城市Top10
from Education_Pie import education_run     # Python数据清洗工程师学历饼图
from geo_charts import get_charts_run       # 地图
from welfared_word_counts import welfared_word_run  # 招聘福利词云图

# 组合多图
from pyecharts.charts import Grid, Page

# industry_run().render()
# hot_city_run().render()
# education_run().render()
# get_charts_run().render()
# welfared_word_run().render()


def save_resize_html():
    """组合图"""
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        industry_run(),
        hot_city_run(),
        education_run(),
        get_charts_run(),
        welfared_word_run()
    )
    # page.render('./html/resize_render.html')
    # str : 默认为save_resize_html : 生成的原html文件,该/html/resize_render.html为组合好的文件
    # cfg_file : 第二步下载的配置文件
    # dest : 新html文件路径resize_render.html, 可修改文件
    # str : 为原文件  cfg_file: json格式的文件 dest为新生成的文件
    page.save_resize_html('./html/resize_render.html', cfg_file='./json/chart_config.json', dest='./html/Bi_render.html')

    return page


def run():
    save_resize_html()


if __name__ == '__main__':
    run()