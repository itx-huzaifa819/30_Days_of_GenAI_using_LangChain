import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document


docs = [
    Document(page_content="LangChain is a framework for developing LLM applications."),
    Document(page_content="Chroma is a vector database used for storing embeddings."),
]

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(docs, embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k": 1})


query = "What is Chroma used for?"
result = retriever.invoke(query)


for doc in result:
    print(doc.page_content)