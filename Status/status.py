import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

################# 遍历目录中的md文件 #################
import os, re
g = os.walk('../')

markdown_path = []
for path, _, file_list in g:
    for file_name in file_list:
        if file_name.startswith('AstroPH'):
            markdown_path = np.append(markdown_path, os.path.join(path, file_name))
markdown_path = [re.sub(r'\\+', '/', i) for i in markdown_path]

################# 拆分文件内容 #################
data_list = []
for md in markdown_path:
#    print(md)
    with open(md, 'r', encoding='utf-8') as f:
        data = f.read()
    data = [i for i in data.split('## 20') if i.startswith('2')]
    for d in range(len(data)):
        if re.match(r'^\d{2}-\d{2}-\d{2}\s+$', data[d]):
            continue
        date = '20' + re.search(r'(\d{2}-\d{2}-\d{2})', data[d]).group(1)
        title = re.findall(r'\s+\d\.\s+\[(.+)\]', data[d])
        arxiv = re.findall(r'\d\.\s+\[.+\]\(h{1,2}ttps.+/(.+)\)', data[d])
        kw_content = re.split(r'\s+\d\.\s+\[.+\]\(.+\)\s+', data[d])[1:]
        keyword, content = [], []
        for kc in kw_content:
            kw = re.search(r'^>\s+([A-Za-z0-9_ \,]+)', kc)
            if kw: 
                keyword.append(kw.group(1))
                content.append(re.search(r'^>\s+[A-Za-z0-9_ \,]+\s+(.+)\s*', kc).group(1))
            else:
                keyword.append('')
                content.append(kc)
        if len(title) == len(arxiv) == len(content) == 0:
            title, arxiv, keyword, content = [''], [''], [''], [re.search(r'\d{2}-\d{2}-\d{2}\s+(.+)\s+', data[d]).group(1)]
        data_format = pd.DataFrame({
            'month': re.search(r'(\d{4}-\d{2})', date).group(1),
            'date': date,
            'arxiv': arxiv,
            'title': title,
            'keyword': keyword,
            'content': content
        }, columns=['month', 'date', 'arxiv', 'title', 'keyword', 'content'])
        data_list.append(data_format)
data = pd.concat(data_list)
noupdate = data.loc[data.content.str.contains('停更')]
data = data.loc[~data.content.str.contains('停更')]
data = data.reset_index(drop=True)

count_data = pd.DataFrame({'Month': data.drop_duplicates('date').groupby('month').count().date.index.values,
                           'Days': data.drop_duplicates('date').groupby('month').count().date.values,
                           'Count': data.groupby('month').count().loc[:, 'title'].values})
count_data.loc[:, 'Rate'] = count_data.loc[:, 'Count'] / count_data.loc[:, 'Days']

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

################# 内容分词统计 #################
import pkuseg, pprint
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator

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

seg = pkuseg.pkuseg(user_dict='dict.txt', postag=True)
text = seg.cut(string_all)
with open('stop_words.txt', encoding='utf-8') as f:
    stopwords = f.read()
new_text = []
for w in text:
    if w[0] not in stopwords:
        if 'n' in w[1]:
            new_text.append(w[0])
counter = Counter(new_text)
# pprint.pprint(counter.most_common(100))

wordcloud = WordCloud(
    font_path = 'simsun.ttc',
    background_color = 'white',
    prefer_horizontal = 0.7,
    width = 1920,
    height = 1080,
    scale = 2,
    margin = 2,
    colormap = 'RdYlBu' # 'Spectral'
).generate_from_frequencies(counter)

wordcloud.to_file('Content.png')

################# 标题分词统计 #################
title_string = '\n'.join(data.title.values).lower()
title_string = re.sub(r'fast radio bursts', 'fast radio burst', title_string)
title_string = re.sub(r'fast radio burst', 'fast_radio_bursts', title_string)
title_string = re.sub(r'milky way', 'milky_way', title_string)
title_string = re.sub(r'frbs', 'frb', title_string)
title_string = re.sub(r'frb', 'fast_radio_bursts', title_string)
title_string = re.sub(r'stars', 'star', title_string)
title_string = re.sub(r'clusters', 'cluster', title_string)

seg = pkuseg.pkuseg(user_dict='dict.txt', postag=True)
text = seg.cut(title_string)
with open('english.txt', encoding='utf-8') as f:
    stopwords = f.read()
new_text = []
for w in text:
    if w[0] not in stopwords:
#        if 'n' in w[1]:
            new_text.append(w[0])
new_text = [re.sub('fast_radio_bursts', 'fast radio bursts', i) for i in new_text]
new_text = [re.sub('milky_way', 'milky way', i).capitalize() for i in new_text]
counter = Counter(new_text)

wordcloud = WordCloud(
    font_path = 'cambria.ttc',
    background_color = 'white',
    prefer_horizontal = 0.7,
    width = 1920,
    height = 1080,
    scale = 2,
    margin = 2,
    stopwords = stopwords,
    colormap = 'crest'
).generate_from_frequencies(counter)

wordcloud.to_file('Title.png')