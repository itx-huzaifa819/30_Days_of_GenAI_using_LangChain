from langchain_community.document_loaders import TextLoader

loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()

print(f"Total Documents: {len(docs)}")
print(f"Metadata: {docs[0].metadata}")
print(f"Content Preview: {docs[0].page_content[:100]}")s