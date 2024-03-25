from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

# 创建LLM
llm = ChatOpenAI()
# llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-pro")

# 创建Prompt
prompt = ChatPromptTemplate.from_template("{question}")

# 创建输出解析器
output_parser = StrOutputParser()


class QuestionInput(BaseModel):
    question: str


_inputs = RunnablePassthrough().with_types(input_type=QuestionInput)

# 创建Chain
chain = _inputs | prompt | llm | output_parser
