import os
import requests
import json
API_KEY="sk-klfdfneucqrvzdpkoueemqtltofgujrlmvouknlzlmnxpvzm"
BASE_URL="https://api.siliconflow.cn/v1/chat/completions"
MODEL="deepseek-ai/DeepSeek-V4-Flash"
def call_llm(prompt):
  """
  调用大模型API，返回回答内容
  """
  headers={
    "Authorization":f"Bearer {API_KEY}",
    "Content_Type":"application/json"
  }
  data={
    "model":MODEL,
    "messages":[
      {"role":"user","content":prompt}
    ],
    "max_tokens":512,
    "temperature":0.7
  }
  try:
    response=requests.post(BASE_URL,headers=headers,json=data,timeout=30)
    response.raise_for_status()
    result=response.json()
    content=result["choices"][0]["message"]["content"]
    return content
  except requests.exceptions.RequestException as e:
    return f"网络请求失败：{e}"
  except (KeyError,IndexError,json.JSONDecodeError)as e:
    return f"解析响应失败：{e}"
#如果直接运行文件会执行，但如果从外边导入不会执行
if __name__=="__main__":
  print("开始调用大模型……")
  question="你是什么模型"
  print(f"问题：{question}")
  print("等待回复……")
  answer=call_llm(question)
  print(f"回答：{answer}")
