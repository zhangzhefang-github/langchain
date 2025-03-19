from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# 加载环境变量（确保有.env文件包含OPENAI_API_KEY）
load_dotenv()

def main():
    # 检查API密钥是否设置
    if not os.getenv("OPENAI_API_KEY"):
        print("请设置OPENAI_API_KEY环境变量或在.env文件中添加")
        return
    
    # 初始化GPT-4o mini模型
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # 使用GPT-4o mini模型
        temperature=0.7
    )
    
    # 创建提示模板
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个智能助手，能够提供有用、安全和诚实的回答。"),
        ("human", "{input}")
    ])
    
    # 创建简单的处理链
    chain = prompt | llm | StrOutputParser()
    
    # 运行链
    response = chain.invoke({"input": "介绍一下中国的四大发明"})
    print("GPT-4o mini 回答:")
    print(response)
    
    # 演示聊天历史
    print("\n连续对话示例:")
    from langchain_core.messages import HumanMessage, AIMessage
    
    chat_history = []
    
    # 第一轮对话
    messages = [
        ("system", "你是一个专业的历史老师，对中国历史有深入了解。"),
        ("human", "中国古代有哪些著名的发明?")
    ]
    prompt_with_history = ChatPromptTemplate.from_messages(messages)
    chain = prompt_with_history | llm | StrOutputParser()
    response = chain.invoke({})
    print("\n问题: 中国古代有哪些著名的发明?")
    print(f"回答: {response}")
    
    # 更新聊天历史
    chat_history.extend([
        HumanMessage(content="中国古代有哪些著名的发明?"),
        AIMessage(content=response)
    ])
    
    # 第二轮对话 - 带上下文
    messages = [
        ("system", "你是一个专业的历史老师，对中国历史有深入了解。"),
    ]
    # 添加聊天历史
    for message in chat_history:
        if isinstance(message, HumanMessage):
            messages.append(("human", message.content))
        elif isinstance(message, AIMessage):
            messages.append(("assistant", message.content))
    
    # 添加新问题
    messages.append(("human", "这些发明对世界产生了什么影响?"))
    
    prompt_with_history = ChatPromptTemplate.from_messages(messages)
    chain = prompt_with_history | llm | StrOutputParser()
    response = chain.invoke({})
    print("\n问题: 这些发明对世界产生了什么影响?")
    print(f"回答: {response}")

if __name__ == "__main__":
    main() 