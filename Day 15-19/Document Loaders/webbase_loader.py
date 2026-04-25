from langchain_community.document_loaders import WebBaseLoader

url = "https://docs.smith.langchain.com/"
loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content[:500])