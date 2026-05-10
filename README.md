# 🎓 University AI Helpdesk

An AI-powered conversational university support system built using **FastAPI, FAISS, RAG (Retrieval-Augmented Generation), and Google Gemini AI**.  
The platform enables students and staff to instantly retrieve accurate information from official university documents such as admission guidelines, fee structures, scholarship policies, and eligibility criteria through a multilingual chatbot interface.

---

# 🚀 Live Demo

🌐 Frontend:  
https://university-helpdesk.netlify.app

⚡ Backend API:  
https://university-helpdesk-q9pw.onrender.com

---

# 📌 Features

- 🤖 AI-powered university chatbot
- 📄 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic document search using FAISS vector database
- 🌍 Multilingual responses
- 🎤 Voice input support using Web Speech API
- ⚡ FastAPI backend deployment on Render
- 🌐 Frontend deployed on Netlify CDN
- 📚 Answers grounded in official university PDF documents
- 🧠 Google Gemini AI integration
- ☁️ Optimized for free-tier cloud deployment

---

# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript
- Web Speech API

## Backend
- FastAPI
- Python
- FAISS Vector Database
- LangChain
- FastEmbed Embeddings
- Google Gemini API

## Deployment
- Netlify (Frontend)
- Render.com (Backend)

---

# 🧠 How It Works

1. Official university PDF documents are processed and indexed.
2. Documents are split into semantic chunks.
3. Chunks are converted into vector embeddings.
4. Embeddings are stored in a FAISS vector database.
5. User queries are semantically matched with relevant document chunks.
6. Retrieved context is passed to Gemini AI.
7. Gemini generates concise, context-aware answers grounded in university documents.

---

# 📂 Project Structure

```bash
university-helpdesk/
│
├── backend/
│   ├── documents/
│   ├── vectorstore/
│   ├── create_db.py
│   ├── main.py
│   ├── rag.py
│   ├── requirements.txt
│
├── frontend/
│   └── index.html
│
└── .gitignore
```

---

# ⚙️ Installation & Local Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/university-helpdesk.git
cd university-helpdesk
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create `.env` inside `backend/`

```env
GEMINI_API_KEY=your_api_key
```

---

## 5️⃣ Generate Vector Database

```bash
cd backend
python create_db.py
```

---

## 6️⃣ Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```txt
http://127.0.0.1:8000
```

---

## 7️⃣ Run Frontend

Inside `frontend/`

```bash
python -m http.server 5500
```

Open:

```txt
http://localhost:5500
```

---

# 📸 Screenshots

- AI-powered floating chatbot widget
- Voice-enabled query input
- Multilingual responses
- Real-time university information retrieval

---

# 🔥 Deployment Optimization

This project is optimized for free-tier cloud deployment using:

- ✅ Precomputed FAISS vector database
- ✅ Lazy loading architecture
- ✅ Lightweight FastEmbed embeddings
- ✅ Memory-optimized startup
- ✅ FastAPI asynchronous API design

---

# 🎯 Future Improvements

- User authentication system
- Chat history persistence
- Admin dashboard
- Fine-tuned university-specific language model
- PDF upload panel for administrators
- Analytics dashboard
- Mobile application support

---

# 👨‍💻 Author

**Sawan Kumar**

- AI & Backend Development Enthusiast
- FastAPI • RAG • Generative AI • Cloud Deployment

---

# 📄 License

This project is developed for educational and demonstration purposes.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
