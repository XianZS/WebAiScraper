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

# 检查 st.session_state 中是否存在 "dom_content" 键
if "dom_content" in st.session_state:
    # 创建一个文本区域，提示用户输入解析描述
    parse_description = st.text_area("Description what you want to parse")
    # 如果用户点击了 "Parse Description" 按钮
    if st.button("Parse Description"):
        # 检查用户是否输入了解析描述
        if parse_description:
            # 在页面上显示用户输入的解析描述
            st.write(parse_description)
            # 调用 split_dom_content 函数，将 DOM 内容分割成多个块
            dom_chunks = split_dom_content(st.session_state.dom_content)
            # 调用 parse_with_ollama 函数，传入 DOM 内容块和解析描述，执行解析操作
            result = parse_with_ollama(dom_chunks, parse_description)
            # 在页面上显示解析结果
            st.write(result)
