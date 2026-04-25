from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

# 🔹 Load document
loader = TextLoader("docs.txt")
documents = loader.load()

# 🔹 Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# 🔹 Create embeddings + vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# 🔹 Retriever
retriever = vectorstore.as_retriever()

# 🔹 Query
query = "What are the key takeaways from the document?"
retrieved_docs = retriever.invoke(query)

# 🔹 Combine retrieved text
retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

# 🔹 LLM (chat model)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 🔹 Prompt + response
prompt = f"Based on the following text, answer the question:\n{query}\n\n{retrieved_text}"
response = llm.invoke(prompt)

print("Answer:", response.content)