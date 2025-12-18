from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.pdf_reader import extract_text
from app.services.bank_detector import detect_bank
from app.services.parser_factory import get_parser

router = APIRouter(prefix="/parse", tags=["Statement"])

@router.post("/")
async def parse_statement(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(400, "Only PDF files allowed")

    text = extract_text(file.file)
    bank = detect_bank(text)

    parser = get_parser(bank, text)
    if not parser:
        raise HTTPException(400, "Unsupported bank")

    return parser.parse()
