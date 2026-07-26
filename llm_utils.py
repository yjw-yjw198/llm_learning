import requests
import json

# ===== 配置区域（以后改 API Key 只改这里） =====
API_KEY = "sk-klfdfneucqrvzdpkoueemqtltofgujrlmvouknlzlmnxpvzm"   # 换成你自己的
BASE_URL = "https://api.siliconflow.cn/v1/chat/completions"
MODEL = "deepseek-ai/DeepSeek-V4-Flash"
# =============================================


def call_llm_with_history(messages, max_tokens=512, temperature=0.7):
    """
    调用大模型 API，传入完整的对话历史
    messages: 列表，格式为 [{"role": "user", "content": "..."}, ...]
    max_tokens: 回答的最大长度
    temperature: 0~1，越高越随机
    返回: 模型回答的字符串
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    try:
        response = requests.post(BASE_URL, headers=headers, json=data, timeout=200)
        response.raise_for_status()
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        return content
    except requests.exceptions.RequestException as e:
        return f"网络请求失败：{e}"
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        return f"解析响应失败：{e}"