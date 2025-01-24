# -*- coding: UTF-8 -*-
"""
    @Project : WebAiScraper 
    @File    : scrape.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/23 17:24 
    @NowThing: 爬取网页 - 方程式
"""
# 导入selenium库中的webdriver模块，用于控制浏览器
import selenium.webdriver as webdriver
# 导入selenium库中的Service模块，用于启动浏览器驱动
from selenium.webdriver.chrome.service import Service
# 导入BeautifulSoup库，用于解析HTML内容
from bs4 import BeautifulSoup
# 导入time库，用于添加延迟
import time


def scrape_website(website):
    """
    使用Selenium和Chrome浏览器驱动爬取指定网页的HTML内容。

    参数:
    website (str): 要爬取的网页URL。

    返回:
    str: 爬取到的网页HTML内容。
    """
    print("Launching chrome browser ... ")
    # 指定Chrome浏览器驱动的路径
    chrome_driver_path = "./chromedriver.exe"
    # 创建Chrome浏览器选项对象
    options = webdriver.ChromeOptions()
    # 创建Chrome浏览器驱动对象，指定驱动路径和选项
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    try:
        # 使用浏览器驱动打开指定网页
        driver.get(website)
        print("Successfully opened chrome browser ... ")
        # 获取网页的HTML内容
        html = driver.page_source
        # 处理逻辑
        # 睡眠逻辑处理
        time.sleep(10)
        return html
    finally:
        # 关闭浏览器驱动
        driver.quit()


def extract_body_content(html_content) -> str:
    """
    从HTML内容中提取<body>标签内的内容。

    参数:
    html_content (str): 包含HTML内容的字符串。

    返回:
    str: <body>标签内的内容，如果不存在则返回空字符串。
    """
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(html_content, 'html.parser')
    # 查找<body>标签
    body_content = soup.body
    if body_content:
        # 将<body>标签内的内容转换为字符串并返回
        return str(body_content)
    return ""


def clean_body_content(body_content):
    """
    清理HTML内容，移除<script>和<style>标签及其内容，并去除空行和首尾空格。

    参数:
    body_content (str): 包含HTML内容的字符串。

    返回:
    str: 清理后的HTML内容。
    """
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(body_content, 'html.parser')

    # 遍历所有的script和style标签
    for script_or_style in soup(["script", "style"]):
        # 移除这些标签及其内容
        script_or_style.extract()
    # 获取HTML内容中的文本，并使用换行符作为分隔符
    cleaned_content = soup.get_text(separator="\n")

    # 移除文本中的空行和首尾空格
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content


def split_dom_content(dom_content, max_length=6000) -> list:
    """
    将DOM内容分割成多个块，每个块的最大长度为max_length。

    参数:
    dom_content (str): 要分割的DOM内容。
    max_length (int): 每个块的最大长度，默认为6000。

    返回:
    list: 分割后的DOM内容块列表。
    """
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]
