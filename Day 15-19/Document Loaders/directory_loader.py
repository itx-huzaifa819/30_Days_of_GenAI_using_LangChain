from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Folder ke andar se sirf saari .pdf files load karne ke liye
loader = DirectoryLoader(
    "./books", 
    glob="*.pdf", 
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(f"Total pages loaded from directory: {len(docs)}")