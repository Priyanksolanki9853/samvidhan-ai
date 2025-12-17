# ⚖️ Samvidhan AI: Intelligent Legal Assistant

![Platform](https://img.shields.io/badge/Platform-Web-blue)
![Python](https://img.shields.io/badge/Python-3.11-green)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-black)
![LLM](https://img.shields.io/badge/LLM-Llama--3.3--70B-orange)
![Database](https://img.shields.io/badge/Vector%20DB-Pinecone-blueviolet)

**Samvidhan AI** is a cutting-edge, Full-Stack Legal Assistant designed to bridge the gap between complex Indian Law and the common citizen. By leveraging **Retrieval-Augmented Generation (RAG)** and the latest **Llama 3.3 70B** model, it provides accurate, real-time insights into the Indian Constitution and the new **Bhartiya Nyaya Sanhita (BNS)**.

---

## 🚀 Key Features

### 1. 🧑‍⚖️ AI Judge (Verdict Predictor)
Users can input real-life scenarios, and the AI acts as a Senior Judge to identify applicable BNS/IPC sections, predict likely verdicts, and determine bail eligibility.

### 2. 📝 Legal Document Drafter
Instantly generate professional-grade legal documents like **Rent Agreements, Affidavits, and Court Petitions**.
- **PDF Download:** Generated drafts can be exported as high-quality PDFs with a single click.

### 3. 📄 PDF Analysis (Document OCR)
Upload existing legal documents (Notices, Agreements, FIRs). The AI extracts text and provides a **Risk Analysis** and summary in plain language.

### 4. ⚖️ IPC to BNS Converter
Deep mapping of old Indian Penal Code (IPC) sections to the new 2023 Bhartiya Nyaya Sanhita (BNS) laws.

### 5. 🗣️ Multilingual Support & Voice
Supports **Hinglish/Hindi** queries to ensure accessibility. Built-in **Voice Recognition** allow users to speak their legal concerns.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 (Glassmorphism UI), JavaScript (ES6+) |
| **Backend** | Python, FastAPI, Uvicorn |
| **AI Model** | Llama 3.3 70B (via Groq Cloud) |
| **Vector DB** | Pinecone (High-speed Vector Search) |
| **Embeddings** | HuggingFace (`all-mpnet-base-v2`) |
| **OCR/PDF** | PyPDF & HTML2PDF.js |

---

## 🏗️ System Architecture

1. **User Query:** Entered via text or voice.
2. **Retrieval:** System generates a vector embedding and searches the **Pinecone Database** for relevant Articles/Sections.
3. **Augmentation:** Top results are fed into the **Llama 3.3** model as context.
4. **Generation:** AI provides a structured, professional response with sources.

---

## ⚙️ Installation & Setup

### 1. Clone the Project
```bash
git clone [https://github.com/YOUR_USERNAME/samvidhan-ai.git](https://github.com/YOUR_USERNAME/samvidhan-ai.git)
cd samvidhan-ai
