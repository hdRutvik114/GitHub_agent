from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def create_Vector_store(chunks,metadatas):
    """
    convert text into embeddings and store them in FAiss
    
     
    """
    
    # -----------------------------
    # 1. EMBEDDING MODEL (FREE)
    # -----------------------------
     # correct model name (no spaces!)
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    # -----------------------------
    # 2. GEMINI LLM (FREE TIER)
    # -----------------------------
    
    # llm = ChatGroq(
    #     model="llama-3.1-8b-instant",
       
    # )# ✅ stable & available
    llm=ChatGoogleGenerativeAI(model="gemini-3.    1-flash-lite-preview")  
        
    vectorstore = FAISS.from_texts(
    texts=chunks,
    embedding=embedding_model,
    metadatas=metadatas,
    )
    return vectorstore
    
    
  
