from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# 🔹 Load Chat Model (correct for GPT models)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 🔹 Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

# 🔹 Create chain using LCEL (modern way)
chain = prompt | llm

# 🔹 Run
topic = input("Enter a topic: ")
response = chain.invoke({"topic": topic})

print("Generated Blog Title:", response.content)