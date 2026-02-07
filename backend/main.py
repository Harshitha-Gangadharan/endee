import io
import os
from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv

# Import your modular services
from .core.parser import ComplianceParser
from .core.scanner import ComplianceScanner
from .core.embedder import OnlineEmbedder
from .services.endee_client import EndeeClient

load_dotenv()
app = FastAPI(title="Resume-Shield: AI Compliance Checker")

# Initialize Services
parser = ComplianceParser()
scanner = ComplianceScanner()
embedder = OnlineEmbedder(token=os.getenv("HF_TOKEN"))
db_client = EndeeClient()

@app.on_event("startup")
async def startup():
    db_client.initialize_collection()

@app.post("/upload-compliant")
async def upload_resume(file: UploadFile = File(...)):
    # 1. PARSE: Extract raw text & Metadata (Location/Experience)
    content = await file.read()
    raw_text = parser.extract_clean_stream(io.BytesIO(content))
    meta_tags = parser.get_compliance_metadata(raw_text)

    # 2. SCAN: Redact PII (The Security Layer)
    # Only clean_text goes forward to the AI
    clean_text, violations, score = scanner.scan_and_redact(raw_text)

    # 3. VECTORIZE: Use HF API on the REDACTED text
    vector = embedder.generate_vector(clean_text)

    # 4. STORE: Save to Endee with filtered metadata
    db_client.insert_resume(
        filename=file.filename,
        vector=vector,
        metadata={
            "compliance_score": score,
            "violations": violations,
            "detected_location": meta_tags["detected_location"],
            "exp_level": meta_tags["experience_level"],
            "preview": clean_text[:200]
        }
    )

    return {
        "filename": file.filename,
        "compliance_score": score,
        "location_detected": meta_tags["detected_location"],
        "status": "Securely Indexed"
    }

@app.get("/search")
async def search(query: str):
    query_vector = embedder.generate_vector(query)
    results = db_client.search(query_vector)
    return {"results": results}