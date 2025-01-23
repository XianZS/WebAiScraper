# -*- coding: UTF-8 -*-
"""
    @Project : WebAiScraper 
    @File    : parse.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/23 20:03 
    @NowThing: ai 本地执行 不需要令牌
"""

# 导入OllamaLLM类，用于与Ollama模型进行交互
from langchain_ollama import OllamaLLM
# 导入ChatPromptTemplate类，用于创建聊天提示模板
from langchain_core.prompts import ChatPromptTemplate

# 定义一个模板字符串，用于生成提示信息
template = (
    # 任务描述：从给定的文本内容中提取特定信息
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    # 详细说明：请仔细遵循以下指令
    "Please follow these instructions carefully: \n\n"
    # 指令1：仅提取与提供的描述直接匹配的信息
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    # 指令2：不要在响应中包含任何额外的文本、评论或解释
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    # 指令3：如果没有与描述匹配的信息，返回一个空字符串（''）
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    # 指令4：输出应仅包含明确请求的数据，不包含其他文本
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# 创建一个OllamaLLM实例，指定使用的模型为llama3
model = OllamaLLM(model="llama3")


def parse_with_ollama(dom_chunks, parse_description):
    """
    使用Ollama模型解析DOM内容。
    :param dom_chunks: 包含DOM内容的列表。
    :param parse_description: 解析描述。
    :return: 解析结果的字符串。
    """
    # 使用模板创建一个聊天提示
    prompt = ChatPromptTemplate.from_template(template)
    # 将提示和模型组合成一个链
    chain = prompt | model

    # 初始化一个空列表，用于存储解析结果
    parsed_results = []

    # 遍历DOM内容块
    for i, chunk in enumerate(dom_chunks, start=1):
        # 使用链处理每个块，并传入DOM内容和解析描述
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        # 打印当前处理的批次信息
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        # 将解析结果添加到列表中
        parsed_results.append(response)

    # 将解析结果列表连接成一个字符串，并返回
    return "\n".join(parsed_results)
