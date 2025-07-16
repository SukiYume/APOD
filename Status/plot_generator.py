"""
画图模块
生成各种统计图表
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud
from pyecharts.charts import Graph
from pyecharts import options as opts
from pyecharts.globals import ThemeType

try:
    import seaborn as sns
    plt.style.use('default')
    sns.set_color_codes()
    SEABORN_AVAILABLE = True
except ImportError:
    SEABORN_AVAILABLE = False
    plt.style.use('default')

from matplotlib import rcParams
rcParams['pdf.fonttype'] = 42
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['mathtext.fontset'] = 'custom'
rcParams['mathtext.cal'] = 'Arial'
rcParams['mathtext.it'] = 'Arial'
rcParams['mathtext.rm'] = 'Arial'

# 颜色配置
COLOR_LIST = [
    "#001219", "#005f73", "#0a9396", "#94d2bd", "#e9d8a6", 
    "#ee9b00", "#ca6702", "#bb3e03", "#ae2012", "#9b2226"
]


def convert_white(ax, color='white'):
    """将坐标轴转换为指定颜色"""
    ax.tick_params(axis='x', colors=color, which='both')
    ax.tick_params(axis='y', colors=color, which='both')
    ax.spines['top'].set_color(color)
    ax.spines['bottom'].set_color(color)
    ax.spines['left'].set_color(color)
    ax.spines['right'].set_color(color)
    ax.xaxis.label.set_color(color)
    ax.yaxis.label.set_color(color)


def show_values(axs, orient="v", space=.01):
    """在柱状图上显示数值"""
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height() * 0.01)
                value = '{:.0f}'.format(p.get_height())
                ax.text(_x, _y + 1, value, ha="center", color=COLOR_LIST[1], size=8)
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height() * 0.5)
                value = '{:.1f}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left", rotation=90)

    if isinstance(axs, np.ndarray):
        for _, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)


def plot_new_count(data, output_path='Figure/ReadCount.png'):
    """绘制累计阅读数量图"""
    plt.figure(figsize=(7, 3))
    ax = plt.subplot(111)
    
    plt.step(
        pd.to_datetime(data.drop_duplicates('date').date),
        np.cumsum(data.groupby('date').count().month.values), 
        color=COLOR_LIST[-1], zorder=0
    )
    plt.scatter(pd.to_datetime(data.date.values[-1]), len(data), color=COLOR_LIST[1], zorder=1)
    plt.annotate(
        text=str(len(data)), xy=(pd.to_datetime(data.date.values[-1]), len(data)),
        xytext=(pd.to_datetime(data.date.values[-1]), len(data) / 2), 
        weight='bold', color=COLOR_LIST[1], ha='center',
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color=COLOR_LIST[1])
    )
    
    plt.xlabel('Date')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(axis='x', colors=COLOR_LIST[1], which='both')
    ax.tick_params(axis='y', colors=COLOR_LIST[1], which='both')
    ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(6))
    ax.spines['bottom'].set_color(COLOR_LIST[1])
    ax.spines['left'].set_color(COLOR_LIST[1])
    ax.xaxis.label.set_color(COLOR_LIST[1])
    ax.yaxis.label.set_color(COLOR_LIST[1])

    plt.ylim(0)
    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
    plt.close()


def plot_word_cloud(counter, flag='title', output_path=None):
    """生成词云图"""
    if output_path is None:
        output_path = f'Figure/{flag.capitalize()}.png'
        
    if flag == 'title' or flag == 'keyword':
        font_path = 'data/Font/Canela-Medium-Trial.otf'
    elif flag == 'content':
        font_path = 'data/Font/FZQKBYSJW.TTF'

    wordcloud = WordCloud(
        font_path=font_path,
        background_color="rgba(255, 255, 255, 0)",
        mode="RGBA",
        prefer_horizontal=0.7,
        width=1920,
        height=1080,
        scale=2,
        margin=2,
        colormap=ListedColormap(COLOR_LIST[1:])
    ).generate_from_frequencies(counter)

    wordcloud.to_file(output_path)


def plot_word_max(counter, output_path='Figure/KeyCount.png'):
    """绘制词频前10的柱状图"""
    words_max = counter.most_common(10)
    words_max = pd.DataFrame({
        'word': [i[0] for i in words_max], 
        'count': [i[1] for i in words_max]
    })
    words_max.loc[:, 'count'] = words_max.loc[:, 'count'].astype(np.int64)
    
    plt.figure(figsize=(7, 3))
    ax = plt.subplot(111)
    
    if SEABORN_AVAILABLE:
        import seaborn as sns
        p = sns.barplot(words_max, x='word', y='count', hue='word', palette=COLOR_LIST)
    else:
        # 使用matplotlib原生条形图
        bars = plt.bar(words_max['word'], words_max['count'], 
                      color=COLOR_LIST[:len(words_max)])
        p = ax
    
    show_values(p)
    
    plt.xticks(rotation=90)
    plt.xlabel('')
    plt.yticks([])
    plt.ylabel('')
    plt.ylim(0, words_max.loc[:, 'count'].max() + 20)
    
    convert_white(ax, color=COLOR_LIST[1])
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
    plt.close()


def plot_counter_graph(counter, string_list, output_path='Figure/keyword.html'):
    """生成关键词关系图"""
    words_max = counter.most_common(50)
    words_max_count = np.array([i[1] for i in counter.most_common(50)])
    np.random.shuffle(words_max)
    
    nodes, links = [], []
    for i in range(len(words_max)):
        nodes.append({
            'id': i,
            'name': words_max[i][0],
            'symbolSize': (words_max[i][1] - words_max_count.min()) * (
                (66 - 5) / (words_max_count.max() - words_max_count.min())
            ) + 5
        })
        
        for j in range(i + 1, len(words_max)):
            for k in string_list:
                if (words_max[i][0].lower() in k) and (words_max[j][0].lower() in k):
                    links.append({
                        'source': str(i),
                        'target': str(j)
                    })
                    break
    
    c = (
        Graph(
            init_opts=opts.InitOpts(
                width="1280px", height="720px", theme=ThemeType.DARK
            )
        )
        .add(
            "",
            nodes=nodes,
            links=links,
            categories=[{'name': i} for i in range(len(nodes))],
            layout="circular",
            is_rotate_label=True,
            linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_left="2%", pos_top="20%"
            ),
        )
        .render(output_path)
    )


def plot_monthly_read(data, output_path='Figure/MonthCount.png'):
    """绘制月度阅读统计"""
    import calendar
    
    plt.figure(figsize=(6, 3))
    ax = plt.subplot(111)

    d2021 = data.loc[
        data.month.str.split('-', expand=True).loc[:, 0].astype(np.int64) == 2021
    ].reset_index(drop=True)
    d2022 = data.loc[
        data.month.str.split('-', expand=True).loc[:, 0].astype(np.int64) == 2022
    ].reset_index(drop=True)

    width = 0.36
    plt.bar(
        np.arange(12) - width / 2, 
        d2021.groupby('month').count().loc[:, 'title'].values,
        width=width, color=COLOR_LIST[-1], alpha=1, 
        edgecolor='white', lw=0.5, label='2021'
    )
    plt.bar(
        np.arange(12) + width / 2, 
        d2022.groupby('month').count().loc[:, 'title'].values,
        width=width, color=COLOR_LIST[1], alpha=1, 
        edgecolor='white', lw=0.5, label='2022'
    )

    plt.xticks(np.arange(12), list(calendar.month_abbr)[1:])
    plt.legend()

    rate = len(d2021) / 12
    plt.hlines(rate, -1, 12, ls='--', color=COLOR_LIST[-1], zorder=-1)
    plt.text(11 + 0.02, rate + 1.6, '{:.2f}'.format(rate), color='white')
    plt.text(11, rate + 2, '{:.2f}'.format(rate), color=COLOR_LIST[-1])

    rate = len(d2022) / 12
    plt.hlines(rate, -1, 12, ls='--', color=COLOR_LIST[1], zorder=-1)
    plt.text(11 + 0.02, rate - 4.4, '{:.2f}'.format(rate), color='white')
    plt.text(11, rate - 4, '{:.2f}'.format(rate), color=COLOR_LIST[1])

    plt.xlim(-1, 12)
    plt.ylim(0, 62)
    plt.ylabel('Count')

    convert_white(ax)

    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
    plt.close()


def plot_arxiv_id(data, output_path='Figure/arXivID.png'):
    """绘制arXiv ID分布"""
    plt.figure(figsize=(6, 3))
    ax = plt.subplot(111)
    
    asd = data.loc[
        data.arxiv.str.contains(r'\d{4}\.\d{4,5}')
    ].arxiv.str.extract(r'\.(\d{4,5})').loc[:, 0].apply(int).values
    
    plt.hist(asd, bins=25, color=COLOR_LIST[-1], edgecolor='white', lw=0.5)
    plt.xlabel('arXiv ID')
    plt.ylabel('Count')
    convert_white(ax)

    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
    plt.close()
