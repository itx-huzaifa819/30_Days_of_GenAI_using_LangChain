import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StringOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel


load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")
parser = StringOutputParser()


joke_prompt = PromptTemplate.from_template("Tell me a short joke about {topic}")


explanation_prompt = PromptTemplate.from_template("Explain why this joke is funny: {joke}")


joke_chain = joke_prompt | model | parser


final_chain = joke_chain | RunnableParallel(
    original_joke = RunnablePassthrough(), 
    explanation = {"joke": RunnablePassthrough()} | explanation_prompt | model | parser
)

topic_input = {"topic": "machine learning"}
result = final_chain.invoke(topic_input)

print("--- ORIGINAL JOKE ---")
print(result['original_joke'])

print("\n--- EXPLANATION ---")
print(result['explanation'])