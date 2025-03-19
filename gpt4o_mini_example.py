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
        ("system", "You are a helpful assistant that provides useful, safe, and honest answers."),
        ("human", "{input}")
    ])
    
    # 创建简单的处理链
    chain = prompt | llm | StrOutputParser()
    
    # 运行链
    response = chain.invoke({"input": "Tell me about the Four Great Inventions of ancient China"})
    print("GPT-4o mini response:")
    print(response)
    
    # 演示聊天历史
    print("\nContinuous dialogue example:")
    from langchain_core.messages import HumanMessage, AIMessage
    
    chat_history = []
    
    # 第一轮对话
    messages = [
        ("system", "You are a history teacher with deep knowledge of Chinese history."),
        ("human", "What are some famous inventions from ancient China?")
    ]
    prompt_with_history = ChatPromptTemplate.from_messages(messages)
    chain = prompt_with_history | llm | StrOutputParser()
    response = chain.invoke({})
    print("\nQuestion: What are some famous inventions from ancient China?")
    print(f"Answer: {response}")
    
    # 更新聊天历史
    chat_history.extend([
        HumanMessage(content="What are some famous inventions from ancient China?"),
        AIMessage(content=response)
    ])
    
    # 第二轮对话 - 带上下文
    messages = [
        ("system", "You are a history teacher with deep knowledge of Chinese history."),
    ]
    # 添加聊天历史
    for message in chat_history:
        if isinstance(message, HumanMessage):
            messages.append(("human", message.content))
        elif isinstance(message, AIMessage):
            messages.append(("assistant", message.content))
    
    # 添加新问题
    messages.append(("human", "What impact did these inventions have on the world?"))
    
    prompt_with_history = ChatPromptTemplate.from_messages(messages)
    chain = prompt_with_history | llm | StrOutputParser()
    response = chain.invoke({})
    print("\nQuestion: What impact did these inventions have on the world?")
    print(f"Answer: {response}")

if __name__ == "__main__":
    main() 