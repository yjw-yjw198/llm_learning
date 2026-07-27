from Day9_llm_utils_stream import call_llm_stream
if __name__=="__main__":
  print("🤖 大模型聊天助手已启动（流式输出）！")
  print("💡 输入你的问题，输入 'exit' 或 'quit' 退出程序\n")
  history=[{"role":"system","content":"你是一个乐于助人的ai助手"}]
  while True:
    user_input=input("你：")
    if user_input.lower() in ["exit","quit"]:
      print("再见")
      break
    history.append({"role":"user","content":user_input})
    answer=call_llm_stream(history)
    history.append({"role":"assistant","content":answer})
    