import os
import json
import time
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
PINECONE_KEY = os.getenv("PINECONE_API_KEY")

# 1. Setup
pc = Pinecone(api_key=PINECONE_KEY)
index = pc.Index("samvidhan-index")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# 2. Load Data
# We will check for sample first, then full
filename = "data/constitution_of_india.json"
if not os.path.exists(filename): 
    filename = "data/constitution.json"
    print("⚠️ Sample not found, using full file.")

with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"🚀 Starting Full Upload from: {filename}")

vectors = []
for i, item in enumerate(data):
    # Standardize data keys
    doc_id = str(item.get('article', item.get('id', 'unknown')))
    title = item.get('title', item.get('id', ''))
    desc = item.get('description', item.get('text', ''))
    
    # Create the text blob
    text = f"{title}: {desc}"
    if not text.strip() or "unknown" in doc_id: continue

    try:
        # Embed Locally
        vector = embeddings.embed_query(text)
        
        vectors.append({
            "id": doc_id,
            "values": vector,
            "metadata": {"text": text}
        })
        
        print(f"   Generated: {doc_id}")

        # Upload in batches of 50
        if len(vectors) >= 50:
            index.upsert(vectors=vectors)
            vectors = []
            print(f"   💾 Saved batch.")

    except Exception as e:
        print(f"   ❌ Error on {doc_id}: {e}")

# Upload leftovers
if vectors:
    index.upsert(vectors=vectors)
    print("\n✅ Upload Complete! Your Demo is Ready.")