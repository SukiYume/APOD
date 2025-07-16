"""
主函数模块
控制程序流程，决定生成哪些图表
"""

import os
from data_extractor import get_markdown_path, extract_data, get_keyword_counter, content_count
from plot_generator import plot_new_count, plot_word_cloud, plot_word_max, plot_counter_graph


def ensure_figure_dir():
    """确保Figure目录存在"""
    if not os.path.exists('Figure'):
        os.makedirs('Figure')


def generate_default_plots(data_path='../'):
    """
    生成默认的四个图表：
    - Content.png: 内容词云
    - KeyCount.png: 关键词频率柱状图  
    - Keyword.png: 关键词词云
    - ReadCount.png: 累计阅读数量
    """
    # 确保输出目录存在
    ensure_figure_dir()
    
    print("正在提取数据...")
    markdown_path = get_markdown_path(data_path)
    data, count_data = extract_data(markdown_path)
    
    print("正在生成 ReadCount.png...")
    plot_new_count(data, 'Figure/ReadCount.png')
    
    print("正在生成 Keyword.png...")
    keyword_counter = get_keyword_counter(data)
    plot_word_cloud(keyword_counter, 'keyword', 'Figure/Keyword.png')
    
    print("正在生成 KeyCount.png...")
    plot_word_max(keyword_counter, 'Figure/KeyCount.png')
    
    print("正在生成 Content.png...")
    content_counter, string_list = content_count(data, 'content')
    plot_word_cloud(content_counter, 'content', 'Figure/Content.png')
    
    print("所有图表生成完成！")
    return data, count_data


def generate_all_plots(data_path='../'):
    """
    生成所有可用的图表
    """
    # 确保输出目录存在
    ensure_figure_dir()
    
    print("正在提取数据...")
    markdown_path = get_markdown_path(data_path)
    data, count_data = extract_data(markdown_path)
    
    # 生成默认图表
    print("正在生成默认图表...")
    generate_default_plots(data_path)
    
    # 生成额外图表
    print("正在生成关键词关系图...")
    keyword_counter = get_keyword_counter(data)
    keyword_counter_50, keyword_string_list = content_count(data, 'title')
    plot_counter_graph(keyword_counter, keyword_string_list, 'Figure/keyword.html')
    
    print("正在生成标题词云...")
    title_counter, title_string_list = content_count(data, 'title')
    plot_word_cloud(title_counter, 'title', 'Figure/Title.png')
    
    print("所有图表生成完成！")
    return data, count_data


def main():
    """主函数"""
    print("开始生成图表...")
    
    # 默认生成四个主要图表
    data, count_data = generate_default_plots()
    
    # 如果需要生成所有图表，可以调用：
    # data, count_data = generate_all_plots()
    
    print(f"数据统计：共处理了 {len(data)} 条记录")
    print("图表已保存到 Figure/ 目录")


if __name__ == '__main__':
    main()
