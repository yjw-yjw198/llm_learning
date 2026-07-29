import json
import csv
import time
from datetime import datetime
from Day9_llm_utils_stream import call_llm_stream
def load_questions(filepath):
  """
  读取questions.txt，每行作为一个问题
  返回问题列表
  """
  with open(filepath,"r",encoding="utf-8")as f:
    #去掉每行首尾的空白字符，并过滤掉空行
    questions=[line.strip() for line in f if line.strip()]
  return questions

def batch_process(questions,delay=1):
  """
  批量处理问题列表，逐一调用大模型
  delay：每个问题之间的间隔（秒），防止请求过快被限流
  """
  results=[]
  for idx,question in enumerate(questions,1):
    print(f"\n[{idx}/{len(questions)}] 正在处理：{question}")
    messages=[{"role":"user","content":question}]
    answer =call_llm_stream(messages)
    results.append(
      {
        "id":idx,
        "question":question,
        "answer":answer
      }
    )
    if idx<len(questions):
      time.sleep(delay)
  return results    

def save_results(results):
  """
  把结果保存为csv文件（同时保留一份json备份）
  """
  timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
  csv_filename=f"batch_results_{timestamp}.csv"
  json_filename=f"batch_results_{timestamp}.json"
  #保存csv文件
  with open(csv_filename,"w",encoding="utf-8-sig",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=["id","question","answer"])
    writer.writeheader()
    writer.writerows(results)
  print(f"\n CSV结果已经保存：{json_filename}")
  #保存json（备份）
  with open(json_filename,"w",encoding="utf-8") as f:
    json.dump(results,f,ensure_ascii=False,indent=2)
  print(f"json 备份已经保存：{json_filename}")


if __name__=="__main__":
  print("批量处理启动！")
  print("读取question.txt……")

  questions=load_questions("questions.txt")
  print(f"共读取{len(questions)}个问题\n")
  if not questions:
    print("questions.txt为空，请先添加问题")
  else:
    results=batch_process(questions)
    save_results(results)
    print("\n 批量处理完成！")