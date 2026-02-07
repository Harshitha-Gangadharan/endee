import io
import os
from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
from .core.scanner import ComplianceScanner
from .core.embedder import OnlineEmbedder 
from .services.endee_client import EndeeClient
import fitz 

load_dotenv()
app = FastAPI(title="AI Compliance Checker - Modular")

# Initialize Modular Services
HF_TOKEN = os.getenv("HF_TOKEN")
scanner = ComplianceScanner()
embedder = OnlineEmbedder(token=HF_TOKEN)
db_client = EndeeClient()



@app.on_event("startup")
async def startup():
    db_client.initialize_index()

@app.post("/upload-compliant")
async def upload_resume(file: UploadFile = File(...)):
    # 1. Extract
    content = await file.read()
    doc = fitz.open(stream=content, filetype="pdf")
    raw_text = "".join([page.get_text() for page in doc])

    # 2. Scan & Redact (Compliance Layer)
    clean_text, violations, score = scanner.scan_and_redact(raw_text)

    # 3. Vectorize (Using CLEAN text only)
    vector = embedder.generate_vector(clean_text)

    # 4. Store in Endee
    db_client.upsert_resume(
        id=file.filename,
        vector=vector,
        meta={
            "score": score,
            "violations": violations,
            "preview": clean_text[:200]
        }
    )

    return {
        "filename": file.filename,
        "compliance_score": score,
        "status": "Securely Indexed"
    }

@app.get("/search")
async def search(query: str):
    query_vector = embedder.generate_vector(query)
    results = db_client.search(query_vector)
    return {"results": results}