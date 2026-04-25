from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader("DL_Curriculum.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)

final_chunks = splitter.split_documents(docs)

print(f"Total Document Chunks: {len(final_chunks)}")
print(f"Content of Chunk 1: {final_chunks[0].page_content}")