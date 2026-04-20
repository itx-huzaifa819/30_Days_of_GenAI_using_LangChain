
#       Document_Similarity Application 

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Imran Khan led Pakistan to its historic victory in the 1992 Cricket World Cup",
    "Wasim Akram is widely regarded as one of the greatest fast bowlers the game has ever produced.",
    "Waqar Youni was famous for his lethal reverse swing bowling and wicket-taking ability.",
    "Misbah-ul-Haq led Pakistan to the number one Test ranking in 2016",
    "Inzamam-ul-Haq remains one of the highest run scorers in the country’s cricket history."
     
]

query = 'tell me about Imran Khan'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is :", score)