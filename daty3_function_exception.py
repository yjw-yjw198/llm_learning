try:
  result=10/0
except ZeroDivisionError:
  print("除数不能为0")

try:
  file=open("D:/abc.txt","r")
  content=file.read()
except FileNotFoundError:
  print("文件不存在，请检查路径")
except Exception as e:
  print(f"发生了其他错误{e}")
else:
  print("文件读取成功,内容为",content)
finally:
  print("清理资源")
  file.close()


try:
  data={"name":"北航","age":"120"}
  value=data["age"]
except KeyError:
  print("键不存在!")
except Exception as e:
  print(f"发生了其他错误：{e}")
else:
  print(value)

def check_age(age):
  if age<0:
    raise ValueError("年龄不能为负数")
  return age
try:
  check_age(5)
except ValueError as e:
  print(f"输入错误：{e}")
else:
  print(check_age(5))

def extrat_content(response_data):
  try:
    content=response_data["choices"][0]["message"]["content"]
    return content
  except(KeyError,IndexError):
    return None

mock_corret_response={
  "choices":[
    {"index":0,"message":{"role":"assistant","content":"北航ai很强"}}
  ]
}
print("解析结果：",extrat_content(mock_corret_response))


print("————————异常处理实战————————————")
import random
import time
def mock_llm_cal(prompt):
  print(f"正在调用大模型，提示词{prompt}")
  time.sleep(0.5)
  if random.random()<0.3:
    raise ConnectionError("网络连接超时，请检查网络！")
  else:
    return {"status":"success","data":f"大模型回答：关于'{prompt}'的问题，建议你多写代码"}

for i in range(5):
  print(f"\n---第{i+1}次调用---")
  try:
    response=mock_llm_cal("如何学好北航ai")
    print("成功获取到数据：",response["data"])
  except ConnectionError as e:
    print(f"网络错误捕获：{e}")
    print("提示：请稍后重试或重新检查网络设置")
  except Exception as e:
    print(f"未知错误捕获：{e}")
  else:
    print("本次调用完美结束！")
  finally:
    print("日志记录：本次调用流程结束")

print()
print("综合实战：批量处理候选答案")
batch_data = [
    {"id": 1, "content": "北航AI很强", "score": 9.5},
    {"id": 2, "content": "课程有点难", "score": 7.0},
    {"id": 3, "error": "missing_content"},  # 这条数据格式错误，缺少content
    {"id": 4, "content": "食堂不错", "score": 6.5}
]
def safe_extra_high_score(data_list,threshold=8.0):
  result=[]
  for item in data_list:
    try:
      if item.get("score",0)>= threshold:
        result.append(item["content"])
    except(KeyError,TypeError):
      print(f"警告：跳过格式错误的数据->{item}")
      continue
  return result

result=safe_extra_high_score(batch_data)
print("安全提取结果：",result)


def validate_score(score):
    if not isinstance(score, (int, float)):
        raise TypeError("分数必须是数字！")
    if score < 0 or score > 100:
        raise ValueError("分数必须在0到100之间！")
    print("分数合法")

# 测试调用
test_scores = ["九十分", -10, 85]

for s in test_scores:
    try:
        validate_score(s)
    except TypeError as e:
        print(f"类型错误：{e}")
    except ValueError as e:
        print(f"数值错误：{e}")
    else:
        print("校验通过，没有异常")
    finally:
        print("--- 本次检查结束 ---\n")