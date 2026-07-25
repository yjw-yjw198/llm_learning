print("列表基础")
list=[1,2,3]
print("c风格列表",list)
mixed=[1,"你好",3.14,True]
print("混装列表",mixed)
list.append(4)
print("c风格列表",list)
print("切片",list[1:3])
print("字典基础")
response={
  "status":"success",
  "code":200,
  "data":{
    "model":"gpt-3.5",
    "answer":"你好我是大模型"
  }
}
print("完整字典",response)
print("状态码：",response["code"])
print("模型名称：",response["data"]["model"])
print("回答内容：",response["data"]["answer"])
for key,value in response.items():
    print(f"键：{key}->值：{value}")

print("列表推导式:左边分类右边筛选")
# 这是一组模拟的大模型多轮对话记录（列表里包着字典）
chat_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello! How can I help you today?"},
    {"role": "user", "content": "Tell me about BUAA"},
    {"role": "assistant", "content": "Beihang University is a top aerospace engineering school in China."}
]
list1=[msg for msg in chat_history if msg["role"]!="system"]
print(list1)
list2=["长句" if len(msg["content"])>5 else "短句" for msg in chat_history]
print(list2)
list3=["长句" if len(msg["content"])>5 else "短句" for msg in chat_history if msg["role"]!="system"]
print(list3)

# 模拟大模型API返回的3个候选回答，每个回答包含评分和内容
api_response = {
    "status": "success",
    "candidates": [
        {"id": 1, "content": "北航的AI学院很强", "score": 9.5, "tags": ["学术", "正面"]},
        {"id": 2, "content": "课程有点难", "score": 7.0, "tags": ["学术", "中立"]},
        {"id": 3, "content": "食堂不错", "score": 6.5, "tags": ["生活", "正面"]}
    ]
}

list4=[msg["content"] for msg in api_response["candidates"] if msg["score"]>8.0]
print(list4)
list5=["推荐"if msg["score"]>8.0 else "可考虑" for msg in api_response["candidates"]]
print(list5)
list6=[
    f"好评：{msg['content']}" if msg["score"]>8.0 else f"中评：{msg['content']}" 
    for msg in api_response["candidates"] 
    if msg["tags"][1]=="正面"
]
print(list6)