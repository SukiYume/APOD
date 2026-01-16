"""
数据提取模块
处理markdown文件并提取论文数据
"""

import os
import re
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='jieba')

import numpy as np
import pandas as pd
import jieba
import jieba.posseg as pseg
from collections import Counter


def get_markdown_path(path):
    """获取所有AstroPH开头的markdown文件路径"""
    g = os.walk(path)
    markdown_path = []
    for path, _, file_list in g:
        for file_name in file_list:
            if file_name.startswith('AstroPH'):
                markdown_path = np.append(markdown_path, os.path.join(path, file_name))
    markdown_path = [re.sub(r'\\+', '/', i) for i in markdown_path]
    return markdown_path


def extract_data(markdown_path):
    """从markdown文件中提取数据"""
    data_list = []
    for md in markdown_path:
        with open(md, 'r', encoding='utf-8') as f:
            data = f.read()
        data = [i for i in data.split('## 20') if i.startswith('2')]

        for d in range(len(data)):
            if re.match(r'^\d{2}-\d{2}-\d{2}\s+$', data[d]):
                continue

            date = '20' + re.search(r'(\d{2}-\d{2}-\d{2})', data[d]).group(1)
            title = re.findall(r'\s+\d+\.\s+\[(.+)\]', data[d])
            arxiv = re.findall(r'\d+\.\s+\[.+\]\(h{1,2}ttps.+/(.+)\)', data[d])
            kw_content = re.split(r'\s+\d+\.\s+\[.+\]\(.+\)\s+', data[d])[1:]

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
    data = data.sort_values(by='date')
    data = data.reset_index(drop=True)

    count_data = pd.DataFrame({
        'Month': data.drop_duplicates('date').groupby('month').count().date.index.values,
        'Days': data.drop_duplicates('date').groupby('month').count().date.values,
        'Count': data.groupby('month').count().loc[:, 'title'].values
    })
    count_data.loc[:, 'Rate'] = count_data.loc[:, 'Count'] / count_data.loc[:, 'Days']

    return data, count_data


def get_keyword_counter(data):
    """提取关键词计数"""
    data = data.loc[data.keyword != ''].reset_index(drop=True)
    keyword_list = []
    for i in data.keyword.str.split(r',\s+').values:
        keyword_list += i
    counter = Counter(keyword_list)
    return counter


def content_count(data, flag='title'):
    """处理内容并生成词频统计"""
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
        stop_words_path = 'data/english.txt'

    elif flag == 'content':
        string_all, string_list = '', []
        for i in range(len(data)):
            string = data.content[i]
            string = re.sub(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?', '', string)
            string = re.sub(r'\<img.+?\>', '', string)
            string = re.sub(r'\<p.+?\>', '', string)
            string = re.sub(r'\</p\>', '', string)
            string = re.sub(r'`(.+?)`', r'\g<1>', string)
            string = re.sub(r'\${1,2}.+?\${1,2}', '', re.sub(r'\n', '', string))
            string_list.append(string)
            string_all += string + '\n'
        stop_words_path = 'data/stop_words.txt'

    # 加载自定义词典
    jieba.load_userdict('data/dict.txt')
    # 使用词性标注模式分词
    text = pseg.cut(string_all)
    with open(stop_words_path, encoding='utf-8') as f:
        stopwords = set(f.read().split())

    new_text = []
    for word, flag in text:
        if word not in stopwords:
            # jieba词性标注：n-名词, nr-人名, ns-地名, nt-机构名, nz-其他专名
            if flag.startswith('n'):
                new_text.append(word)

    new_text = [re.sub('fast_radio_bursts', 'fast radio bursts', i) for i in new_text]
    new_text = [re.sub('milky_way', 'milky way', i).capitalize() for i in new_text]
    counter = Counter(new_text)

    return counter, string_list
