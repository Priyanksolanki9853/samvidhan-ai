import os
import json
import time
from dotenv import load_dotenv
from pinecone import Pinecone
# NEW: Import HuggingFace (Local)
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
PINECONE_KEY = os.getenv("PINECONE_API_KEY")

# 1. Setup Pinecone
pc = Pinecone(api_key=PINECONE_KEY)
index = pc.Index("samvidhan-index")

# 2. Setup Local Embeddings (Running on your laptop)
# We use 'all-mpnet-base-v2' because it has 768 dimensions (matches Google/Pinecone)
print("📥 Loading Local Embedding Model (This happens once)...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# 3. Load Data
filename = "data/constitution_of_india.json"
if not os.path.exists(filename): filename = "data/constitution.json"

with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)

# Start fresh or where you left off
START_INDEX = 1
print(f"🚀 Starting Local Upload from Article {START_INDEX}...")

vectors = []
for i, item in enumerate(data):
    if i < START_INDEX: continue

    doc_id = str(item.get('article', 'unknown'))
    text = f"{item.get('title', '')}: {item.get('description', '')}"
    if not text.strip(): continue

    try:
        # 1. Embed LOCALLY (Fast & No Limits)
        vector = embeddings.embed_query(text)
        
        vectors.append({
            "id": doc_id,
            "values": vector,
            "metadata": {"text": text}
        })
        print(f"   Generated: {doc_id}")

        # 2. Upload in bigger batches (since local is fast)
        if len(vectors) >= 20:
            index.upsert(vectors=vectors)
            vectors = []
            print(f"   💾 Saved batch.")

    except Exception as e:
        print(f"   ❌ Error on {doc_id}: {e}")

if vectors:
    index.upsert(vectors=vectors)
    print("\n✅ Upload Complete! No API limits used.")