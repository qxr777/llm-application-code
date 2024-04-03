from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

# 创建LLM
llm = ChatOpenAI()

# 创建输出解析器
output_parser = StrOutputParser()

# 创建Prompt
outline_prompt = ChatPromptTemplate.from_template("针对博客主题'''{topic}'''，设计中文写作大纲。")
content_prompt = ChatPromptTemplate.from_template(
    "按照博客大纲'''{outline}'''的设计，进行中文正文的撰写，字数300字左右。")
positive_comment_prompt = ChatPromptTemplate.from_template("针对博客内容'''{content}'''编写10条积极正面的中文评论。")
negative_comment_prompt = ChatPromptTemplate.from_template("针对博客内容'''{content}'''编写5条消极负面的中文评论。")
tagging_prompt = ChatPromptTemplate.from_template("对于博客正文内容'''{content}'''进行智能中文标签。")


class TopicInput(BaseModel):
    topic: str


_inputs = RunnablePassthrough().with_types(input_type=TopicInput)

# 创建组合Chain
outline_chain = _inputs | outline_prompt | llm | output_parser | {"outline": RunnablePassthrough()}
content_chain = content_prompt | llm | output_parser | {"content": RunnablePassthrough()}
positive_comment_chain = positive_comment_prompt | llm | output_parser
negative_comment_chain = negative_comment_prompt | llm | output_parser
tagging_chain = tagging_prompt | llm | output_parser
map_chain = RunnableParallel(positive_comment=positive_comment_chain, negative_comment=negative_comment_chain,
                             tags=tagging_chain, content=itemgetter("content"))
chain = (
        outline_chain
        | content_chain
        | map_chain
        | {
            # "outline": itemgetter("outline"),
            "content": itemgetter("content"),
            "positive_comment": itemgetter("positive_comment"),
            "negative_comment": itemgetter("negative_comment"),
            "tags": itemgetter("tags"),
        }
)

# 打印chain的计算图
chain.get_graph().print_ascii()
