from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("DL_Curriculum.pdf")

docs = loader.load()

print(f"Total Pages: {len(docs)}")
print(f"Page 1 Content: {docs[0].page_content}")
print(f"Page 1 Metadata: {docs[0].metadata}") # Isme 'page' number dikhayega