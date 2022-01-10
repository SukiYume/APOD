import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

import pkuseg, pprint, re
from matplotlib import gridspec
from collections import Counter
from wordcloud import WordCloud
from matplotlib.font_manager import FontProperties

from pyecharts.charts import Graph
from pyecharts import options as opts
from pyecharts.globals import ThemeType

from extractdata import get_markdown_path, extract_data

def x2_func(x, a, b, c):
    return a * x** b + c

def plot_arXiv_count():
    data = pd.read_csv('get_monthly_submissions.csv')
    popt, _ = curve_fit(x2_func, np.arange(len(data))[:-1], data.submissions[:-1])
    
    plt.figure(figsize=(10, 4))
    plt.step(np.arange(len(data)), data.submissions, color='royalblue', alpha=0.8)
    plt.plot(np.arange(len(data)), x2_func(np.arange(len(data)), *popt), color='royalblue', lw=20, alpha=0.2)
    plt.xticks(6 + 12*np.arange(0, 35, 5), 1992+np.arange(0, 35, 5))
    plt.ylabel('Paper Submissions')
    path = 'arXivCount-{:.2f}-{}.png'.format(popt[1], '1991714')
    # plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.show()
    
def plot_apod_status(data, count_data):
    
    ############ 计数统计 ############
    plt.figure(figsize=(7, 5))
    plt.subplots_adjust(wspace=0, hspace=0)
    gs = gridspec.GridSpec(5, 1)
    
    plt.subplot(gs[0:2, :])
    plt.bar(data.drop_duplicates('date').groupby('month').count().date.index.values, 
            data.drop_duplicates('date').groupby('month').count().date.values, color='royalblue', alpha=0.5)
    plt.ylabel('Days')
    
    ax = plt.subplot(gs[2:, :])
    plt.bar(data.groupby('month').count().loc[:, 'title'].index.values, 
            data.groupby('month').count().loc[:, 'title'].values, color='r', alpha=0.5)
    plt.xticks(data.groupby('month').count().loc[:, 'title'].index.values,
               data.groupby('month').count().loc[:, 'title'].index.values, rotation=90)
    plt.hlines(count_data.Count.mean(), 0, 12, ls='--', color='r')
    plt.text(11.5, count_data.Count.mean()*1.05, '{:.2f}'.format(count_data.Count.mean()), color='r')
    plt.ylabel('Count', color='r')
    
    ax = ax.twinx()
    ax.bar(data.groupby('month').count().loc[:, 'title'].index.values, 
            data.groupby('month').count().loc[:, 'title'].values / data.drop_duplicates('date').groupby('month').count().date.values, 
            color='royalblue', alpha=0.5)
    ax.set_ylim(0, 5)
    plt.ylabel('Rate', color='royalblue')
    plt.hlines(count_data.Rate.mean(), 0, 12, ls='--', color='royalblue')
    plt.text(11.5, count_data.Rate.mean()*1.1, '{:.2f}'.format(count_data.Rate.mean()), color='royalblue')
    # plt.savefig('ReadCount.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    ############ arXiv ID ############
    asd = data.loc[data.arxiv.str.contains(r'\d{4}\.\d{4,5}')].arxiv.str.split('.', expand=True).loc[:, 1].apply(int).values
    sns.displot(asd, kde=True, bins=20, color='royalblue', edgecolor='white', height=3, aspect=8/4)
    plt.xlabel('arXiv ID')
    # plt.savefig('arXivID.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_new_count(data):
    
    ################# 阅读数统计 #################
    plt.figure(figsize=(7, 3))
    ax = plt.subplot(111)
    plt.step(pd.to_datetime(data.drop_duplicates('date').date), np.cumsum(data.groupby('date').count().month.values),
            color='royalblue', zorder=0)
    plt.scatter(pd.to_datetime(data.date.values[-1]), len(data), color='r', zorder=1)
    plt.annotate(text=str(len(data)), xy=(pd.to_datetime(data.date.values[-1]), len(data)), 
                 xytext=(pd.to_datetime(data.date.values[-8]), len(data) / 2), weight='bold', color='r',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'))
    plt.xlabel('Date')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.yticks([])
    plt.ylim(0)
    plt.savefig('ReadCount.png', dpi=300, bbox_inches='tight')
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

def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                value = '{:.0f}'.format(p.get_height())
                ax.text(_x, _y+1, value, ha="center", color='gray', size=8) 
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

def plot_word_cloud_counter(counter, flag='title'):
    
    if flag == 'title':
        font_path, colormap, fname = 'cambria.ttc', 'crest', None
    elif flag=='content':
        font_path, colormap, fname = 'simsun.ttc', 'RdYlBu', 'C:/Windows/Fonts/simhei.ttf'
    
    ######### 词云 #########
    wordcloud = WordCloud(
        font_path = font_path,
        background_color = 'white',
        prefer_horizontal = 0.7,
        width = 1920,
        height = 1080,
        scale = 2,
        margin = 2,
        colormap = colormap # 'Spectral'
    ).generate_from_frequencies(counter)
    
    wordcloud.to_file('{}.png'.format(flag.capitalize()))
    # plt.imshow(wordcloud)
    # plt.axis('off')
    # plt.close()
    
    ######### 词频 #########
    # keywds = [i[0] for i in counter.most_common(50)]
    # height = [i[1] for i in counter.most_common(50)]
    # plt.figure(figsize=(10, 4))
    # p = sns.barplot(keywds, height, palette='RdYlBu')
    # show_values(p)
    # font = FontProperties(fname=fname, size=9)
    # plt.xticks(rotation=90, fontproperties=font)
    # # plt.savefig('ContentKeyCount', dpi=300, bbox_inches='tight')
    # plt.show()
    
def plot_counter_graph(counter, string_list, flag='title'):
    
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
        Graph(init_opts=opts.InitOpts(width="1920px", height="1080px", theme=ThemeType.VINTAGE))
        .add(
            "",
            nodes=nodes,
            links=links,
            layout="circular",
            is_rotate_label=True,
            linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
        )
        .render("{}.html".format(flag))
    )
    
if __name__ == '__main__':
    path = '../'
    markdown_path = get_markdown_path(path)
    data, count_data = extract_data(markdown_path)
    plot_new_count(data)
#    plot_apod_status(data, count_data)

    counter, string_list = content_count(data, 'title')
    plot_word_cloud_counter(counter, 'title')
#    plot_counter_graph(counter, string_list, flag='title')
    
    counter, string_list = content_count(data, 'content')
    plot_word_cloud_counter(counter, 'content')
#    plot_counter_graph(counter, string_list, flag='content')