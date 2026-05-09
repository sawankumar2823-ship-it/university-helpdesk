from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rag import ask_question

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home Route
@app.get("/")
def home():
    return {"message": "University AI Helpdesk Running"}


# Ask Route
@app.get("/ask")
def ask(query: str):
    try:
        answer = ask_question(query)
        return {"answer": answer}

    except Exception as e:
        print("API error:", e)
        return {"answer": "⚠️ Server error. Please try again."}
