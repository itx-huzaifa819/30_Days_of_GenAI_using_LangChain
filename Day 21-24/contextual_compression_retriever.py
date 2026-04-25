import os
from langchain_core.documents import Document
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers import LLMChainExtractor

docs = [
    Document(page_content="The Grand Canyon is a famous natural site in Arizona. Photosynthesis is how plants convert light into energy. Many tourists visit the canyon every year."),
    Document(page_content="Photosynthesis requires sunlight, water, and carbon dioxide to produce glucose. It is vital for life on Earth."),
    Document(page_content="Medieval Europe was characterized by knights and castles. Basketball is a sport played with a ball and a hoop.")
]

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
base_retriever = vectorstore.as_retriever()

llm = OpenAI(temperature=0)
compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, 
    base_retriever=base_retriever
)


query = "What is photosynthesis?"
compressed_docs = compression_retriever.invoke(query)


for doc in compressed_docs:
    print(f"--- Compressed Document ---\n{doc.page_content}\n")