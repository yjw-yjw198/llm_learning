from llm_utils import call_llm_with_history

# ===== 主程序 =====
if __name__ == "__main__":
    print("🤖 大模型聊天助手已启动（带记忆）！")
    print("💡 输入你的问题，输入 'exit' 或 'quit' 退出程序\n")
    
    # 初始化对话历史
    history = [{"role": "system", "content": "你是一个乐于助人的AI助手。"}]
    
    while True:
        user_input = input("你: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("👋 再见！")
            break
        
        # 把用户的问题加入历史
        history.append({"role": "user", "content": user_input})
        
        print("🤔 思考中...")
        answer = call_llm_with_history(history)
        print(f"🤖: {answer}\n")
        
        # 把模型的回答加入历史
        history.append({"role": "assistant", "content": answer})