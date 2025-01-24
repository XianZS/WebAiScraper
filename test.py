# -*- coding: UTF-8 -*-
"""
    @Project : WebAiScraper 
    @File    : test.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/24 11:52 
    @NowThing: 
"""
import ollama
# 普通输出（请先按照准备工作中的要求安装模型）
back = ollama.chat(model="llama3.1",messages=[{"role": "user","content": "生成一句简短的话"}],
					stream = False, # 是否流式输出
					)
print(back)
#流式输出
back = ollama.chat(model="你的模型名称",messages=[{"role": "user","content": "生成一句简短的话"}],
                   stream = True, # 是否流式输出
                   )
for i in back:
    print(back,end = "")
