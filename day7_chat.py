import requests
import json
import os
API_KEY="sk-klfdfneucqrvzdpkoueemqtltofgujrlmvouknlzlmnxpvzm"
BASE_URL="https://api.siliconflow.cn/v1/chat/completions"
MODEL="deepseek-ai/DeepSeek-V4-Flash"
def call_llm(prompt):
  """
  调用大模型api，返回回答内容
  """
  headers={
    "Authorization":f"Bearer {API_KEY}",
    "Content-Type":"application/json"
  }
  data={
    "model":MODEL,
    "messages":prompt,
    "max_tokens":512,
    "temperature":0.7
  }
  try:
    response=requests.post(BASE_URL,headers=headers,json=data,timeout=200)
    response.raise_for_status()
    result=response.json()
    content=result["choices"][0]["message"]["content"]
    return content
  except requests.exceptions.RequestException as e:
    return f"网络请求失败：{e}"
  except (KeyError,IndexError,json.JSONDecodeError)as e:
    return f"解析响应失败：{e}"

if __name__=="__main__":
  print("大模型助手已经启动(带记忆)：")
  print("输入你的问题：")
  history=[{"role":"system","content":"你是一个乐于助人的ai助手"}]
  while True:
    user_input=input("你：")
    if user_input.lower() in ["exit","quit"]:
      print("goodbye!")
      break
    else:
      history.append({"role":"user","content":user_input})
      print("思考中……")
      answer=call_llm(history)
      print(f"回答{answer}")
      history.append({"role":"assistant","content":answer})