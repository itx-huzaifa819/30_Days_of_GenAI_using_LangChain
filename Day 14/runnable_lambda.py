import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StringOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")
parser = StringOutputParser()

def count_words(text: str):
    """Text ke total words count karne ke liye"""
    return len(text.split())

def uppercase_text(text: str):
    """Text ko uppercase karne ke liye"""
    return text.upper()

essay_prompt = PromptTemplate.from_template("Write exactly two sentences about {topic}")


chain = (
    essay_prompt 
    | model 
    | parser 
    | RunnableParallel(
        original_text = RunnablePassthrough(),
        
        word_count = RunnableLambda(count_words),
        shouting_version = RunnableLambda(uppercase_text)
    )
)

topic = {"topic": "Black Holes"}
result = chain.invoke(topic)


print(f"--- LLM Generated Text ---\n{result['original_text']}\n")
print(f"--- Custom Logic Outputs ---")
print(f"Word Count: {result['word_count']}")
print(f"Uppercase: {result['shouting_version']}")