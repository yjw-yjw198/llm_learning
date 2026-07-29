import requests
import json
API_KEY = "sk-rxonpwpdvjaobxwmbnbieyxsbppwfxlhokgzoarehdgchkmy"   # 换成你自己的
BASE_URL = "https://api.siliconflow.cn/v1/chat/completions"
MODEL = "deepseek-ai/DeepSeek-V4-Flash"

def call_llm_stream(messages,max_tokens=512,temperature=0.7):
  """
  流式调用大模型api，一边生成一边打印
  """
  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  data = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": True   # ← 这个参数开启流式输出
    }
  try:
    response = requests.post(BASE_URL, headers=headers, json=data, stream=True, timeout=200)
    response.raise_for_status()
    full_content=""
    print("🤖:",end="")
    for line in response.iter_lines():
      if line:
        decoded_line=line.decode("utf-8")
        if decoded_line.startswith("data: "):
          json_str=decoded_line[6:]
          if json_str=="[DONE]":
            break
          try:
            chunk=json.loads(json_str)
            if "choices"in chunk and len(chunk["choices"])>0:
              delta=chunk["choices"][0].get("delta",{})
              content=delta.get("content","")
              if content:
                print(content,end="",flush=True)
                full_content+=content
          except json.JSONDecodeError:
            continue
    print("\n")
    return full_content

  except requests.exceptions.RequestException as e:
    return f"网络请求失败：{e}"
  except Exception as e:
    return f"解析响应失败：{e}"
  