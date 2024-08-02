# LangChain API key: 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

import os

os.environ["LANGCHAIN_TRACING_V2"] = "True"
os.environ["LANGCHAIN_API_KEY"] = "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"

os.environ["OPENAI_API_KEY"] 

from langchain_openai import ChatOpenAI #need openai api key for this

llm = ChatOpenAI()
llm.invoke("Hello, world!")