from gemini_functions_agent.agent import agent_executor

__all__ = ["agent_executor"]

# 导入模块
import os
# 设置代理
proxy = 'http://127.0.0.1:7890'
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy