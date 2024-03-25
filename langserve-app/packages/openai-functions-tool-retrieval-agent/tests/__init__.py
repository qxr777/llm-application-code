from openai_functions_tool_retrieval_agent.agent import agent_executor

print(agent_executor.invoke({"input": "今天法国的天气怎么样?", "chat_history": []}))