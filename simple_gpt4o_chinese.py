import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# 加载环境变量
load_dotenv()

# 检查API密钥是否设置
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("错误: OPENAI_API_KEY 环境变量未设置")
    exit(1)

try:
    # 初始化模型
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        openai_api_key=api_key  # 显式传递API密钥
    )
    
    # 创建消息
    messages = [
        SystemMessage(content="You are a helpful assistant who responds in Chinese."),
        HumanMessage(content="请介绍一下中国古代的四大发明。")
    ]
    
    # 调用模型
    print("正在调用 GPT-4o mini...")
    response = model.invoke(messages)
    
    # 打印响应
    print("\nGPT-4o mini 回复:")
    print(response.content)
    
except Exception as e:
    print(f"\n发生错误: {e}")
    
    # 如果出现Unicode错误,尝试使用英文系统提示
    if "UnicodeEncodeError" in str(e):
        print("\n尝试使用英文系统提示...")
        try:
            messages = [
                SystemMessage(content="You are a helpful assistant who responds in Chinese."),
                HumanMessage(content="请介绍一下中国古代的四大发明。")
            ]
            response = model.invoke(messages)
            print("\nGPT-4o mini 回复:")
            print(response.content)
        except Exception as e2:
            print(f"\n再次发生错误: {e2}") 