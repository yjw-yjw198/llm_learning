import json
import os
from datetime import datetime
from Day9_llm_utils_stream import call_llm_stream
def save_history(history,folder="history"):
  """
  把对话历史保存成带时间戳的json文件
  """
  if not os.path.exists(folder):
    os.makedirs(folder)
  #用当前时间生成文件名，避免重复
  timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
  filename=f"{folder}/chat_{timestamp}.json"
  #把history写入json文件
  with open(filename,"w",encoding="utf-8") as f:
    json.dump(history,f,ensure_ascii=False,indent=2)
  print(f"\n聊天记录已保存至：{filename}")
  return filename


if __name__=="__main__":
  print("🤖 大模型聊天助手已启动（流式输出+自动保存）！")
  print("💡 输入你的问题，输入 'exit' 或 'quit' 退出程序\n")
  history=[{"role":"system","content":"你是一个乐于助人的ai助手"}]
  while True:
    user_input=input("你：")
    if user_input.lower() in ["exit","quit"]:
      save_history(history)
      print("再见")
      break
    history.append({"role":"user","content":user_input})
    answer=call_llm_stream(history)
    history.append({"role":"assistant","content":answer})
    