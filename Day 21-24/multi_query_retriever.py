import os
from langchain_core.documents import Document # Crucial import
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import MultiQueryRetriever


documents = [
    Document(page_content="To improve energy levels, prioritize 7-9 hours of sleep and stay hydrated throughout the day."),
    Document(page_content="Maintaining balance involves a mix of regular physical exercise and mindfulness practices like meditation."),
    Document(page_content="A balanced diet rich in whole foods, proteins, and healthy fats provides sustained energy for the body."),
    Document(page_content="The solar system consists of eight planets orbiting the sun.") # Random doc to test retrieval
]


vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())


llm = ChatOpenAI(model="gpt-3.5-turbo")


retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(), 
    llm=llm
)

query = "How to improve energy levels and maintain balance"
results = retriever.invoke(query)

print(f"--- Results for: {query} ---")
for doc in results:
    print(f"- {doc.page_content}")