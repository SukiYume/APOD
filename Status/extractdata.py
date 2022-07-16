import os, re
import numpy as np
import pandas as pd

def get_markdown_path(path):
    
    g = os.walk(path)
    markdown_path = []
    for path, _, file_list in g:
        for file_name in file_list:
            if file_name.startswith('AstroPH'):
                markdown_path = np.append(markdown_path, os.path.join(path, file_name))
    markdown_path = [re.sub(r'\\+', '/', i) for i in markdown_path]
    
    return markdown_path

def extract_data(markdown_path):

    data_list = []
    for md in markdown_path:
#        print(md)
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
    
    count_data = pd.DataFrame({'Month': data.drop_duplicates('date').groupby('month').count().date.index.values,
                               'Days': data.drop_duplicates('date').groupby('month').count().date.values,
                               'Count': data.groupby('month').count().loc[:, 'title'].values})
    count_data.loc[:, 'Rate'] = count_data.loc[:, 'Count'] / count_data.loc[:, 'Days']
    
    return data, count_data
