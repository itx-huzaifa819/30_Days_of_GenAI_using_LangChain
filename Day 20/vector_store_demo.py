import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

os.environ["OPENAI_API_KEY"] = "api_key"

# 2. Document Objects Banayein
docs = [
    Document(
        page_content="Babar Azam is one of the most successful and consistent batsmen in PSL history.",
        metadata={"team": "Peshawar Zalmi"} 
    ),
    Document(
        page_content="Sarfaraz is the former captain of Quetta Gladiators and a prolific run-scorer.",
        metadata={"team": "Quetta Gladiators"}
    ),
    Document(
        page_content="Rizwan is the legendary captain of Multan Sultans and known for his finishing skills.",
        metadata={"team": "Multan Sultans"}
    ),
    Document(
        page_content="Muhammad Amir is a world-class fast bowler for Quetta Gladiators.",
        metadata={"team": "Quetta Gladiators"}
    ),
    Document(
        page_content="Shadab Khan is a key all-rounder for Islamabad United.",
        metadata={"team": "Islamabad United"}
    ),
]


embedding_function = OpenAIEmbeddings()

vector_store = Chroma(
    collection_name="psl_sample",
    embedding_function=embedding_function,
    persist_directory="./my_psl_db"  
)


ids = vector_store.add_documents(docs)
print(f"Generated IDs: {ids}")


stored_data = vector_store.get(include=['documents', 'metadatas']) # Embeddings hataya hai taaki output readable rahe
print(f"Stored {len(stored_data['ids'])} documents.")


print("\n--- Searching for 'Bowler' ---")
query = "Who among these are a bowler?"
results = vector_store.similarity_search(query, k=2)

for result in results:
    print(f"Content: {result.page_content}")
    print(f"Metadata: {result.metadata}")

print("\n--- Search with Score ---")
results_with_score = vector_store.similarity_search_with_score(query, k=1)
print(results_with_score)


print("\n--- Filtering Multan Sultans ---")
ms_players = vector_store.similarity_search(
    query="", 
    filter={"team": "Multan Sultans"}
)

print("Filtered Players:", ms_players)


print("\n--- Updating Babar's Document ---")
updated_doc = Document(
    page_content="Babar Azam, the captain of Stallions, is renowned for his aggressive leadership.",
    metadata={"team": "Peshawar Zalmi"}
)
vector_store.update_document(document_id=ids[0], document=updated_doc)

print("\n--- Deleting Babar's Document ---")
vector_store.delete(ids=[ids[0]])
print("Deleted Babar Azam's document. Remaining count:", len(vector_store.get()['ids']))