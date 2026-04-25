import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StringOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")
parser = StringOutputParser()

#Path 1
complaint_prompt = PromptTemplate.from_template(
    "You are a customer support agent. Respond politely to this complaint: {input}"
)

#Path 2
praise_prompt = PromptTemplate.from_template(
    "You are a social media manager. Thank the user for this feedback: {input}"
)

default_prompt = PromptTemplate.from_template(
    "Respond to this message: {input}"
)

classification_chain = (
    PromptTemplate.from_template(
        "Classify the following text as either 'complaint' or 'praise'. "
        "Output only the word. Text: {input}"
    )
    | model
    | parser
)

branch = RunnableBranch(
    (lambda x: "complaint" in x["topic"].lower(), complaint_prompt | model | parser),
    (lambda x: "praise" in x["topic"].lower(), praise_prompt | model | parser),
    default_prompt | model | parser
)

#Final Chain

full_chain = (
    {"topic": classification_chain, "input": RunnablePassthrough()}
    | branch
)

# Case 1: Complaint
print("--- TEST 1: Complaint ---")
print(full_chain.invoke({"input": "I am very unhappy with the slow delivery speed."}))

# Case 2: Praise
print("\n--- TEST 2: Praise ---")
print(full_chain.invoke({"input": "I love your product, it has changed my life!"}))