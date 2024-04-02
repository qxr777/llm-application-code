import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from rag_conversation import chain as rag_conversation_chain
from extraction_openai_functions import chain as extraction_openai_functions_chain
from openai_functions_agent import agent_executor as openai_functions_agent_chain
from gemini_functions_agent import agent_executor as gemini_functions_agent_chain
from simple_chain import chain as simple_chain_chain
from dag_chain import chain as dag_chain_chain
from simple_tool_agent import agent_executor as simple_tool_agent_chain
from tagging_chain import chain as tagging_chain_chain
from openai_functions_tool_retrieval_agent import agent_executor as openai_functions_tool_retrieval_agent_chain
from blogging_ai_chain import chain as blogging_ai_chain_chain

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
# add_routes(app, NotImplemented)
add_routes(app, rag_conversation_chain, path="/rag-conversation")
add_routes(app, extraction_openai_functions_chain, path="/extraction-openai-functions")
add_routes(app, openai_functions_agent_chain, path="/openai-functions-agent")
add_routes(app, gemini_functions_agent_chain, path="/gemini-functions-agent")
add_routes(app, simple_chain_chain, path="/simple-chain")
add_routes(app, dag_chain_chain, path="/dag-chain")
add_routes(app, simple_tool_agent_chain, path="/simple-tool-agent")
add_routes(app, tagging_chain_chain, path="/tagging-chain")
add_routes(app, openai_functions_tool_retrieval_agent_chain, path="/openai-functions-tool-retrieval-agent")
add_routes(app, blogging_ai_chain_chain, path="/blogging-ai-chain")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
