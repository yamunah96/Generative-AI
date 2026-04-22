import chromadb
import os

from utils.embedding import get_embedding
from utils.chucking import chunk_text


def load_chorma_collection():
    client= chromadb.PersistentClient(path="chorma_store")
    collection= client.get_or_create_collection(name="ai_history")
    if collection.count() >0:
        return collection
    
    print("Generating new chromadb")

    with open("data/ai_history.txt","r") as f:
        text= f.read()


    chunks= chunk_text(text)
    embeddings=[]
    ids=[]

    for i, chunk in enumerate(chunks):
        emb= get_embedding(chunk)
        embeddings.append(emb)
        ids.append(f"chunk_{i}")

    collection.add(
        embeddings=embeddings,
        documents=chunks,
        ids=ids
    )
    print("collection bulit and saved")
    return collection

#  retriev chunks ("whats transformer")
def retrieve_chunks(query, collection, k=3):
    query_vec = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_vec.tolist()],   # convert numpy array → plain list
        n_results=k
    )
    return results["documents"][0]


