from langchain_core.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate

template = """Think carefully, and then tag the text as instructed."""  # noqa: E501
prompt = ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])


# 定义pydantic类用以生成openai的函数描述变量
class Tagging(BaseModel):
    """Tag the piece of text with particular info."""
    sentiment: str = Field(description="sentiment of text, should be `positive`, `negative`, or `neutral`")
    language: str = Field(description="language of text (should be ISO 639-1 code)")
    category: str = Field(description="category of text, should be `politics`, `sports`, `entertainment`, 'economics', "
                                      "'science', 'technology' or `other`")
    tags: str = Field(description="tags")


# Function definition
model = ChatOpenAI()
function = [convert_to_openai_function(Tagging)]

chain = prompt | model.bind(functions=function, function_call={"name": "Tagging"}) | JsonOutputFunctionsParser()
