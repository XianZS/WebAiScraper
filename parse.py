# -*- coding: UTF-8 -*-
"""
    @Project : WebAiScraper 
    @File    : parse.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/23 20:03 
    @NowThing: ai 本地执行 不需要令牌
"""

# 导入 OllamaLLM 类，用于与 Ollama 模型进行交互
from langchain_ollama import OllamaLLM
# 导入 ChatPromptTemplate 类，用于创建聊天提示模板
from langchain_core.prompts import ChatPromptTemplate

# 定义一个模板字符串，用于生成提示信息
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# 创建一个 OllamaLLM 实例，指定使用的模型为 "llama3.1"
model = OllamaLLM(model="llama3.1")


def parse_with_ollama(dom_chunks, parse_description):
    """
    使用 OllamaLLM 模型从给定的文本内容中提取特定信息。

    参数:
    dom_chunks (list): 包含文本内容的列表，每个元素是一个文本块。
    parse_description (str): 描述要提取的信息的字符串。

    返回:
    str: 提取的信息，每个文本块的结果用换行符分隔。
    """
    # 使用模板创建一个 ChatPromptTemplate 实例
    prompt = ChatPromptTemplate.from_template(template)
    # 将提示模板和模型组合成一个链
    chain = prompt | model

    # 初始化一个空列表，用于存储解析结果
    parsed_results = []

    # 遍历每个文本块
    for i, chunk in enumerate(dom_chunks, start=1):
        # 使用链调用模型，传入文本块和描述信息
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        # 打印当前处理的批次信息
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        # 将解析结果添加到列表中
        parsed_results.append(response)

    # 将解析结果列表转换为字符串，每个结果用换行符分隔
    return "\n".join(parsed_results)
