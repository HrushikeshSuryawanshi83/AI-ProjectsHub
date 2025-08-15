from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()  # Load GEMINI_API_KEY from .env file

# Example custom tool
@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

def main():
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    tools = [add_numbers]  # Register your tools here

    agent_executor = create_react_agent(model, tools)

    print("Welcome To this chatbot .type 'quit' to exit ok")
    print("Ask me questions")

    while True:
        user_input=input("\n you: ").strip()

        if user_input=="quit":
           break

        print("\n Assistant: ",end="")

        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=(user_input))]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content,end="")

        print()     
if __name__ == "__main__":
    main()     
    
    # result = agent_executor.invoke({
    #     "messages": [HumanMessage(content="How i Should introduce?")]
    # })
    # print(result["messages"][-1].content)

# if __name__ == "__main__":
#     main()
