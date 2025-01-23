# 导入streamlit库，用于创建Web应用程序
import streamlit as st
# 从scrape模块中导入scrape_website、extract_body_content、clean_body_content和split_dom_content函数
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama

# 设置页面标题为 "Ai Web Scraper"
st.title("Ai Web Scraper")
# 创建一个文本输入框，提示用户输入一个Web URL
url = st.text_input("Please Enter A Web URL:")
# 如果用户点击了"Scrape Site"按钮
if st.button("Scrape Site"):
    # 在页面上显示"Scraping Site"
    st.write("Scraping Site")
    # 调用scrape_website函数，传入用户输入的URL，获取网页源代码
    result = scrape_website(url)
    # 调用extract_body_content函数，传入网页源代码，获取网页主体内容
    body_content = extract_body_content(result)
    # 调用clean_body_content函数，传入网页主体内容，清理主体内容
    cleaned_content = clean_body_content(body_content)
    # 将清理后的内容存储在session_state中，以便在页面刷新时保留数据
    st.session_state.dom_content = cleaned_content
    # 创建一个可展开的区域，显示"View Dom Content"
    with st.expander("View Dom Content"):
        # 创建一个文本区域，显示清理后的内容，高度为300像素
        st.text_area("Dom Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Description what you want to parse")
    if st.button("Parse Description"):
        if parse_description:
            st.write(parse_description)
            dom_chunks = split_dom_content(parse_description)
