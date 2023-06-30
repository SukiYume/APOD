import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
from matplotlib import gridspec
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patheffects as path_effects
from scipy.optimize import curve_fit
plt.style.use('default')
sns.set_color_codes()

from matplotlib import rcParams
rcParams['pdf.fonttype'] = 42
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['mathtext.fontset'] = 'custom'
rcParams['mathtext.cal'] = 'Arial'
rcParams['mathtext.it'] = 'Arial'
rcParams['mathtext.rm'] = 'Arial'

import pkuseg, re, calendar
from collections import Counter
from wordcloud import WordCloud

from pyecharts.charts import Graph
from pyecharts import options as opts
from pyecharts.globals import ThemeType

from extractdata import get_markdown_path, extract_data

color_list = [
    "#001219", "#005f73", "#0a9396", "#94d2bd", "#e9d8a6", "#ee9b00", "#ca6702", "#bb3e03", "#ae2012", "#9b2226"
]

def x2_func(x, a, b, c):
    return a * x** b + c

def convert_white(ax, color='white'):
    ax.tick_params(axis='x', colors=color, which='both')
    ax.tick_params(axis='y', colors=color, which='both')
    ax.spines['top'].set_color(color)
    ax.spines['bottom'].set_color(color)
    ax.spines['left'].set_color(color)
    ax.spines['right'].set_color(color)
    ax.xaxis.label.set_color(color)
    ax.yaxis.label.set_color(color)

def plot_arXiv_count():
    data = pd.read_csv('get_monthly_submissions.csv') # https://arxiv.org/stats/monthly_submissions
    popt, _ = curve_fit(x2_func, np.arange(len(data))[:-1], data.submissions[:-1])

    plt.figure(figsize=(6, 3))
    ax = plt.subplot(111)
    plt.step(np.arange(len(data)), data.submissions, color='white', lw=0.5)
    plt.fill_between(np.arange(len(data)), 0, data.submissions, facecolor=color_list[-1], step='pre', alpha=1)
    plt.xticks(6 + 12*np.arange(0, 35, 5), 1992+np.arange(0, 35, 5))
    plt.ylabel('Paper Submissions')
    plt.xlabel('Year')
    plt.xlim(6, 378)
    plt.ylim(0)
    convert_white(ax)

    plt.savefig('Figure/arxiv', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

def plot_arxiv_id(data):
    plt.figure(figsize=(6, 3))
    ax = plt.subplot(111)
    asd = data.loc[data.arxiv.str.contains(r'\d{4}\.\d{4,5}')].arxiv.str.extract(r'\.(\d{4,5})').loc[:, 0].apply(int).values
    plt.hist(asd, bins=25, color=color_list[-1], edgecolor='white', lw=0.5)
    plt.xlabel('arXiv ID')
    plt.ylabel('Count')
    convert_white(ax)

    plt.savefig('Figure/arXivID.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

def plot_monthly_read(data):

    plt.figure(figsize=(6, 3))
    ax = plt.subplot(111)

    d2021 = data.loc[data.month.str.split('-', expand=True).loc[:, 0].astype(np.int64)==2021].reset_index(drop=True)
    d2022 = data.loc[data.month.str.split('-', expand=True).loc[:, 0].astype(np.int64)==2022].reset_index(drop=True)

    width = 0.36
    plt.bar(
        np.arange(12)-width/2, d2021.groupby('month').count().loc[:, 'title'].values,
        width=width, color=color_list[-1], alpha=1, edgecolor='white', lw=0.5, label='2021'
    )
    plt.bar(
        np.arange(12)+width/2, d2022.groupby('month').count().loc[:, 'title'].values, 
        width=width, color=color_list[1], alpha=1, edgecolor='white', lw=0.5, label='2022'
    )

    plt.xticks(np.arange(12), list(calendar.month_abbr)[1:])
    plt.legend()

    rate = len(d2021) / 12
    plt.hlines(rate, -1, 12, ls='--', color=color_list[-1], zorder=-1)
    plt.text(11+0.02, rate + 1.6, '{:.2f}'.format(rate), color='white')
    plt.text(11, rate + 2, '{:.2f}'.format(rate), color=color_list[-1]) # path_effects=[path_effects.withStroke(foreground='white',     linewidth=0.5)]

    rate = len(d2022) / 12
    plt.hlines(rate, -1, 12, ls='--', color=color_list[1], zorder=-1)
    plt.text(11+0.02, rate - 4.4, '{:.2f}'.format(rate), color='white')
    plt.text(11, rate - 4, '{:.2f}'.format(rate), color=color_list[1]) # path_effects=[path_effects.withStroke(foreground='white',  linewidth=0.5)]

    plt.xlim(-1, 12)
    plt.ylim(0, 62)
    plt.ylabel('Count')

    convert_white(ax)

    plt.savefig('Figure/MonthCount.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

def plot_new_count(data):
    plt.figure(figsize=(7, 3))
    ax = plt.subplot(111)
    plt.step(
        pd.to_datetime(data.drop_duplicates('date').date),
        np.cumsum(data.groupby('date').count().month.values), color=color_list[-1], zorder=0
    )
    plt.scatter(pd.to_datetime(data.date.values[-1]), len(data), color=color_list[1], zorder=1)
    plt.annotate(
        text=str(len(data)), xy=(pd.to_datetime(data.date.values[-1]), len(data)),
        xytext=(pd.to_datetime(data.date.values[-1]), len(data) / 2), weight='bold', color=color_list[1], ha='center',
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color=color_list[1])
    )
    plt.xlabel('Date')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(axis='x', colors=color_list[1], which='both')
    ax.tick_params(axis='y', colors=color_list[1], which='both')
    ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(6))
    ax.spines['bottom'].set_color(color_list[1])
    ax.spines['left'].set_color(color_list[1])
    ax.xaxis.label.set_color(color_list[1])
    ax.yaxis.label.set_color(color_list[1])

    plt.ylim(0)
    plt.savefig('Figure/ReadCount.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

def content_count(data, flag='title'):

    if flag == 'title':
        string_all = '\n'.join(data.title.values).lower()
        string_all = re.sub(r'fast radio bursts', 'fast radio burst', string_all)
        string_all = re.sub(r'fast radio burst', 'fast_radio_bursts', string_all)
        string_all = re.sub(r'milky way', 'milky_way', string_all)
        string_all = re.sub(r'frbs', 'frb', string_all)
        string_all = re.sub(r'frb', 'fast_radio_bursts', string_all)
        string_all = re.sub(r'stars', 'star', string_all)
        string_all = re.sub(r'clusters', 'cluster', string_all)

        string_list = re.sub('fast_radio_bursts', 'fast radio bursts', string_all)
        string_list = re.sub('milky_way', 'milky way', string_list)
        string_list = string_list.split('\n')
        stop_words_path = 'english.txt'

    elif flag=='content':
        string_all, string_list = '', []
        for i in range(len(data)):
            string = data.content[i]
            string = re.sub(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?', '', string)
            string = re.sub(r'\<img.+?\>', '', string)
            string = re.sub(r'\<p.+?\>', '', string)
            string = re.sub(r'\</p\>', '', string)
            string = re.sub(r'`(.+?)`', '\g<1>', string)
            string = re.sub(r'\${1,2}.+?\${1,2}', '', re.sub(r'\n', '', string))
            string_list.append(string)
            string_all += string + '\n'
        stop_words_path = 'stop_words.txt'

    seg = pkuseg.pkuseg(user_dict='dict.txt', postag=True)
    text = seg.cut(string_all)
    with open(stop_words_path, encoding='utf-8') as f:
        stopwords = f.read()
    new_text = []
    for w in text:
        if w[0] not in stopwords:
            if 'n' in w[1]:
                new_text.append(w[0])
    new_text = [re.sub('fast_radio_bursts', 'fast radio bursts', i) for i in new_text]
    new_text = [re.sub('milky_way', 'milky way', i).capitalize() for i in new_text]
    counter = Counter(new_text)

    return counter, string_list

def get_keyword_counter(data):
    data = data.loc[data.keyword!=''].reset_index(drop=True)
    keyword_list = []
    for i in data.keyword.str.split(',\s+').values:
        keyword_list += i
    counter = Counter(keyword_list)
    return counter

def plot_word_cloud(counter, flag='title'):

    if flag == 'title' or flag == 'keyword':
        font_path = 'Font/Canela-Medium-Trial.otf'
    elif flag=='content':
        font_path = 'Font/FZQKBYSJW.TTF'

    ######### 词云 #########
    wordcloud = WordCloud(
        font_path = font_path,
        background_color = "rgba(255, 255, 255, 0)",
        mode="RGBA",
        prefer_horizontal = 0.7,
        width = 1920,
        height = 1080,
        scale = 2,
        margin = 2,
        colormap = ListedColormap(color_list[1:]) # 'Spectral'
    ).generate_from_frequencies(counter)

    wordcloud.to_file('Figure/{}.png'.format(flag.capitalize()))

def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                value = '{:.0f}'.format(p.get_height())
                ax.text(_x, _y+1, value, ha="center", color=color_list[1], size=8)
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                value = '{:.1f}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left", rotation=90)

    if isinstance(axs, np.ndarray):
        for _, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)

def plot_word_max(counter):
    words_max = counter.most_common(20)
    words_max = pd.DataFrame({'word': [i[0] for i in words_max], 'count': [i[1] for i in words_max]})
    words_max.loc[:, 'count'] = words_max.loc[:, 'count'].astype(np.int64)
    plt.figure(figsize=(7, 3))
    ax = plt.subplot(111)
    p = sns.barplot(words_max, x='word', y='count', palette=sns.color_palette(color_list[1:]))
    show_values(p)
    # font = FontProperties(fname=fname, size=9)
    plt.xticks(rotation=90)
    plt.xlabel('')
    plt.yticks([])
    plt.ylabel('')
    plt.ylim(0, words_max.loc[:, 'count'].max()+20)
    convert_white(ax, color=color_list[1])
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.savefig('Figure/KeyCount', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

def plot_counter_graph(counter, string_list):

    words_max = counter.most_common(50)
    words_max_count = np.array([i[1] for i in counter.most_common(50)])
    np.random.shuffle(words_max)
    nodes, links = [], []
    for i in range(len(words_max)):
        nodes.append({
            'id': i,
            'name': words_max[i][0],
            'symbolSize': (words_max[i][1] - words_max_count.min()) *((66-5) / (words_max_count.max()-words_max_count.min())) + 5
        })
        for j in range(i+1, len(words_max)):
            for k in string_list:
                if (words_max[i][0].lower() in k) and (words_max[j][0].lower() in k):
                    links.append({
                        'source': str(i),
                        'target': str(j)
                    })
                    break
    c = (
       Graph(init_opts=opts.InitOpts(width="1280px", height="720px", theme=ThemeType.DARK))
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
           legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
       )
       .render("Figure/keyword.html")
    )

if __name__ == '__main__':
    path = '../'
    markdown_path = get_markdown_path(path)
    data, count_data = extract_data(markdown_path)
    plot_new_count(data)
#    plot_apod_status(data, count_data)
#    plot_monthly_read(data)

    counter = get_keyword_counter(data)
    plot_word_cloud(counter, 'keyword')
    plot_word_max(counter)

    counter, string_list = content_count(data, 'content')
    plot_word_cloud(counter, 'content')
#    plot_counter_graph(counter, string_list, flag='content')

#    counter, string_list = content_count(data, 'title')
#    plot_word_cloud(counter, 'title')
#    plot_counter_graph(counter, string_list, flag='title')