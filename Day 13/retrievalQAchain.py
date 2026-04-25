from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

# 🔹 Load document
loader = TextLoader("docs.txt")
documents = loader.load()

# 🔹 Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# 🔹 Embeddings + vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# 🔹 Retriever
retriever = vectorstore.as_retriever()

# 🔹 LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 🔹 Prompt
prompt = ChatPromptTemplate.from_template(
    "Answer the question based only on the context:\n\n{context}\n\nQuestion: {question}"
)

# 🔹 RAG Chain (LCEL)
chain = (
    {
        "context": retriever,
        "question": lambda x: x
    }
    | prompt
    | llm
)

# 🔹 Query
query = "What are the key takeaways from the document?"
response = chain.invoke(query)

print("Answer:", response.content)