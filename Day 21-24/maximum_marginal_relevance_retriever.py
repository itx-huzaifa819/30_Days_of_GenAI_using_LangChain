from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

docs = [
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="LangChain helps developers create LLM-powered apps."),
    Document(page_content="Embeddings convert text into numerical vectors."),
]

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={'k': 2, 'lambda_mult': 0.5}
)

query = "What is LangChain?"
results = retriever.invoke(query)

for doc in results:
    print(doc.page_content)