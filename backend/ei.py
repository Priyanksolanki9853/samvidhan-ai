import os
import time
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone

# 1. Load Keys
load_dotenv()
PINECONE_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

# 2. Setup Services
pc = Pinecone(api_key=PINECONE_KEY)
index = pc.Index("samvidhan-index")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_KEY)

# 3. The "Golden 5" Articles (Hardcoded)
tiny_data = [
    {
        "id": "Preamble",
        "text": "WE, THE PEOPLE OF INDIA, resolve to constitute India into a SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC and to secure to all its citizens: JUSTICE, LIBERTY, EQUALITY, and FRATERNITY."
    },
    {
        "id": "Article 14",
        "text": "Equality before law. The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India."
    },
    {
        "id": "Article 19",
        "text": "Protection of certain rights regarding freedom of speech, etc. All citizens shall have the right (a) to freedom of speech and expression; (b) to assemble peaceably; (c) to form associations."
    },
    {
        "id": "Article 21",
        "text": "Protection of life and personal liberty. No person shall be deprived of his life or personal liberty except according to procedure established by law. This is the fundamental right to life."
    },
    {
        "id": "Article 32",
        "text": "Remedies for enforcement of rights. The right to move the Supreme Court by appropriate proceedings for the enforcement of the rights conferred by this Part is guaranteed."
    }
]

print("🚑 Starting Emergency Upload (Very Slow Mode)...")

for item in tiny_data:
    try:
        print(f"   Processing: {item['id']}...")
        
        # 1. Embed
        vector = embeddings.embed_query(item['text'])
        
        # 2. Upload
        index.upsert(vectors=[{
            "id": item['id'],
            "values": vector,
            "metadata": {"text": item['text']}
        }])
        
        print(f"   ✅ Success! {item['id']} is in memory.")
        
        # 3. SUPER LONG PAUSE (30 seconds) to keep Google happy
        print("   ⏳ Waiting 30 seconds for quota refill...")
        time.sleep(30)

    except Exception as e:
        print(f"   ❌ Failed {item['id']}: {e}")

print("\n🎉 Emergency Upload Done! You can now search for 'Speech', 'Life', or 'Equality'.")