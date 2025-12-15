import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pinecone import Pinecone
# NEW: Import HuggingFace
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("🔌 Connecting to AI Services...")

# 1. Setup Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("samvidhan-index")

# 2. Setup Embeddings (LOCAL - Matches ingest.py)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# 3. Setup Gemini (Still used for ANSWERING, but not embedding)
# This uses very little quota, so it shouldn't crash.
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", google_api_key=GOOGLE_API_KEY)

print("✅ Services Connected!")

@app.get("/")
def read_root():
    return {"status": "Samvidhan AI (Hybrid Engine) Online"}

@app.get("/search")
def search_law(query: str):
    print(f"\n🔎 User asked: {query}")
    
    try:
        # STEP 1: Search using Local Embeddings
        query_vector = embeddings.embed_query(query)
        search_results = index.query(vector=query_vector, top_k=3, include_metadata=True)
        
        context_text = ""
        sources = []
        for match in search_results['matches']:
            if match['score'] > 0.30: # Slightly lower threshold for this model
                context_text += match['metadata']['text'] + "\n\n"
                sources.append(match['id'])

        if not context_text:
            return {"result": "I couldn't find a specific law for that. Try asking about 'Rights' or 'Arrest'.", "source": "No Match"}

        # STEP 2: Answer using Gemini
        print(f"   📚 Found context: {sources}")
        prompt = f"""
        You are a legal expert. Answer the user based ONLY on this context from the Indian Constitution:
        {context_text}
        
        Question: {query}
        """
        
        response = llm.invoke(prompt)
        
        return {
            "result": response.content,
            "source": f"Sources: Article {', '.join(sources)}"
        }

    except Exception as e:
        print(f"❌ Error: {e}")
        return {"result": "System Error. Please check backend logs.", "source": "Error"}