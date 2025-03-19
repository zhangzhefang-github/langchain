import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 加载环境变量
load_dotenv()

# 检查API密钥是否设置
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("错误: OPENAI_API_KEY 环境变量未设置")
    exit(1)

def chat_with_gpt4o():
    try:
        # 初始化模型
        model = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            openai_api_key=api_key  # 显式传递API密钥
        )
        
        # 初始化消息历史
        messages = [
            SystemMessage(content="You are a helpful assistant who responds in Chinese.")
        ]
        
        print("\n==== GPT-4o mini 中文对话 ====")
        print("输入'退出'或'exit'结束对话")
        
        while True:
            # 获取用户输入
            user_input = input("\n用户: ")
            
            # 检查是否退出
            if user_input.lower() in ['退出', 'exit']:
                print("\n对话结束。谢谢使用！")
                break
            
            # 添加用户消息到历史
            messages.append(HumanMessage(content=user_input))
            
            # 调用模型
            print("GPT-4o mini 思考中...")
            response = model.invoke(messages)
            
            # 添加AI响应到历史
            messages.append(AIMessage(content=response.content))
            
            # 打印响应
            print(f"\nGPT-4o mini: {response.content}")
            
    except Exception as e:
        print(f"\n发生错误: {e}")

if __name__ == "__main__":
    chat_with_gpt4o() 