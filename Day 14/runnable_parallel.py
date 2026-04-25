import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StringOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch


load_dotenv()


model = ChatOpenAI(model="gpt-4o-mini") 
parser = StringOutputParser()


tweet_prompt = PromptTemplate.from_template("Generate a tweet about {topic}")
linkedin_prompt = PromptTemplate.from_template("Generate a LinkedIn post about {topic}")


parallel_chain = RunnableParallel(
    tweet=tweet_prompt | model | parser,
    linkedin=linkedin_prompt | model | parser
)

results = parallel_chain.invoke({"topic": "Generative AI"})
print(f"Tweet: {results['tweet']}")
print(f"LinkedIn: {results['linkedin']}")