# ⚖️ NYAYA AI: Intelligent Legal Assistant

![Status](https://img.shields.io/badge/status-active-success.svg) ![Python](https://img.shields.io/badge/python-3.11-blue.svg) ![FastAPI](https://img.shields.io/badge/FastAPI-v0.100+-005571.svg) ![LLM](https://img.shields.io/badge/LLM-Llama--3.3--70B-orange) ![Pinecone](https://img.shields.io/badge/Vector%20DB-Pinecone-blueviolet)

**NYAYA AI** is a cutting-edge, full-stack conversational legal assistant designed to bridge the gap between complex legal jargon and the common Indian citizen. Utilizing **Retrieval-Augmented Generation (RAG)**, it provides instant, cited, and simplified insights into the Indian Constitution and the new **Bhartiya Nyaya Sanhita (BNS)**.

> **"Democratizing access to justice through AI-driven legal literacy."**

---

## 🚀 Key Features

### 🧑‍⚖️ Virtual Intelligence
* **AI Judge (Verdict Predictor):** Input real-life scenarios to identify applicable **BNS (2023)** and IPC sections, predict likely jail terms, and determine bail eligibility based on current legal frameworks.
* **Case Simplifier:** Instantly translates complex, jargon-heavy court judgments and legal texts into plain, easy-to-understand language.
* **Universal Semantic Search:** Finds relevant articles and sections from the Constitution even if the user doesn't know the exact legal terminology.

### 📝 Legal Drafting & Analysis
* **Document Drafter:** Generates professional-grade legal templates (Rent Agreements, Affidavits, Petitions) with dynamic placeholders for user data.
* **PDF Analysis (OCR):** Upload legal notices, contracts, or FIRs directly via the attachment tool (📎). The AI extracts text, performs risk identification, and highlights critical deadlines.
* **PDF Export:** Directly download AI-generated drafts as professional, formatted PDF files with a single click.

### 🎨 UI/UX & Accessibility
* **SaaS Dashboard:** A modern, sidebar-driven interface featuring a "Hero" dashboard with quick-action suggestion cards for a seamless user experience.
* **Multilingual Support:** Communicate fluently in English, Hindi, or **Hinglish** to ensure maximum inclusivity for users across India.
* **Voice Search:** Integrated **Speech-to-Text** capabilities (🎤) allow users to speak their legal queries naturally rather than typing.

---

## 🏗️ Technical Architecture (RAG Pipeline)

NYAYA AI ensures 100% accuracy and eliminates AI "hallucinations" through a robust 4-step pipeline:

1.  **Vectorization:** Legal documents (Constitution, BNS Acts) are broken into contextual chunks and converted into 768-dimensional vectors using `all-mpnet-base-v2`.
2.  **Storage:** These vectors are indexed in a **Pinecone Vector Database** for sub-second similarity retrieval.
3.  **Retrieval:** When a query is made, the system fetches the most relevant legal context from the database using mathematical similarity.
4.  **Augmentation & Generation:** The retrieved context is fed into **Llama 3.3 (via Groq)** to produce a verified, professional answer.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 (Modern Gradients & Glassmorphism), JavaScript (ES6+) |
| **Backend** | Python 3.11, FastAPI, Uvicorn |
| **AI Brain** | Llama 3.3 70B (Groq Cloud API) |
| **Vector DB** | Pinecone (Serverless Vector Search) |
| **Embeddings** | HuggingFace Sentence Transformers (`all-mpnet-base-v2`) |
| **Processing** | PyPDF (Server-side OCR) & HTML2PDF.js (Client-side export) |

---

## ⚙️ Installation & Setup

### Prerequisites
* Python 3.11 or higher
* Groq API Key (for LLM access)
* Pinecone API Key (for Vector DB access)

### Steps

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/samvidhan-ai.git](https://github.com/your-username/samvidhan-ai.git)
    cd samvidhan-ai
    ```

2.  **Backend Configuration**
    ```bash
    cd backend
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate # Mac/Linux
    pip install -r requirements.txt
    ```

3.  **Environment Variables**
    Create a `.env` file in the `backend/` folder:
    ```env
    GROQ_API_KEY=your_groq_api_key
    PINECONE_API_KEY=your_pinecone_key
    ```

4.  **Launch the Application**
    ```bash
    # Start Backend
    python -m uvicorn main:app --reload
    ```
    Simply open `frontend/index.html` in your browser to start using the assistant.

---

## 📸 User Interface

| Dashboard Hero | Chat Interface |
| :---: | :---: |
| ![Dashboard](<img width="1832" height="1042" alt="image" src="https://github.com/user-attachments/assets/2b252952-a819-4f0c-b35a-23dbc2169c3e" />) | ![Chat](<img width="1881" height="1038" alt="image" src="https://github.com/user-attachments/assets/91c71616-e875-4ea3-a5d9-6d17ded5566a" />) |

---

## 📜 Disclaimer

*Samvidhan AI is an experimental tool provided for educational and informational purposes only. It does not constitute formal legal advice. Always consult with a certified legal professional for serious matters. Predictions made by the AI Judge are based on data patterns and do not guarantee court outcomes.*

---

## 🤝 Contributing

We welcome contributions to make Indian Law more accessible!
1.  Fork the Project
2.  Create your Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

<p align="center">
  Built with ❤️ for Legal Literacy in India 🇮🇳<br>
  <b>Developed by [Priyank Solanki]</b>
</p>
