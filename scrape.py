# -*- coding: UTF-8 -*-
"""
    @Project : WebAiScraper 
    @File    : scrape.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/23 17:24 
    @NowThing: 爬取网页 - 方程式
"""
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time


def scrape_website(website):
    print("Launching chrome browser ... ")
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    try:
        driver.get(website)
        print("Successfully opened chrome browser ... ")
        html = driver.page_source
        # 处理逻辑
        # 睡眠逻辑处理
        time.sleep(10)
        return html
    finally:
        driver.quit()


def extract_body_content(html_content) -> str:
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
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
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]