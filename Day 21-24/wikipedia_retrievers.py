from langchain_community.retrievers import WikipediaRetriever


retriever = WikipediaRetriever(top_k_results=2, lang='en')

query = "The geopolitical history of India and Pakistan from the perspective of China"

docs = retriever.invoke(query)

for doc in docs:
    print(f"Source: {doc.metadata['source']}")
    print(f"Content: {doc.page_content[:200]}...")
    print("-" * 50)