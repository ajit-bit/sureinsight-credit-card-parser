from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import statement
import app.config   # Loads Tesseract OCR path globally

app = FastAPI(title="SureInsight API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(statement.router)

@app.get("/")
def health():
    return {
        "status": "Backend running",
        "ocr": "enabled",
        "supported_banks": ["ICICI", "HDFC", "SBI", "AXIS", "AMEX"]
    }
