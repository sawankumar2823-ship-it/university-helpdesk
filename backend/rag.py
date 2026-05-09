import os

from dotenv import load_dotenv
from google import genai
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# ---------------------------
# ENV SETUP
# ---------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ---------------------------
# CONFIGURE GEMINI
# ---------------------------
client = genai.Client(api_key=GEMINI_API_KEY)

# ---------------------------
# LOAD VECTOR DB
# ---------------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)

print("✅ Vector DB loaded successfully!")


# ---------------------------
# ASK FUNCTION
# ---------------------------
def ask_question(question):
    try:
        if not db:
            return "⚠️ No documents loaded."

        # Retrieve relevant chunks
        docs = db.similarity_search(question, k=5)

        context = "\n\n".join([doc.page_content for doc in docs])

        print("\n🔍 Retrieved context:\n", context[:500])

        prompt = f"""
        You are an AI-powered university helpdesk assistant.

        IMPORTANT RULE:
        - Detect the language of the user's question.
        - Answer in the SAME language as the question.
        - Do NOT translate to English unless the question is in English.

        Answer ONLY using the given context.

        If answer is not found, say:
        "I don't have that information in the university documents."

        Keep answers short and clear.

        Context:
        {context}

        Question:
        {question}
        """

        if not GEMINI_API_KEY:
            return "⚠️ Gemini API key missing."

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=prompt
        )

        return response.text if response.text else "No response generated."

    except Exception as e:
        print("❌ AI error:", e)
        return "⚠️ AI service temporarily unavailable."
