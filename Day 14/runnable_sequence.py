import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StringOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch


load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini") 
parser = StringOutputParser()


prompt = PromptTemplate.from_template("Write a short joke about {topic}")


# Method 1: Using RunnableSequence class
chain = RunnableSequence(prompt, model, parser)

# Method 2: Using Pipe (|) Operator (LCEL - LangChain Expression Language)
chain_lcel = prompt | model | parser

result = chain_lcel.invoke({"topic": "Artificial Intelligence"})
print(result)