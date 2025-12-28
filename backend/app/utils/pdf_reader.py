import pdfplumber
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io


def extract_text(file) -> str:
    text = ""

    # ---------- STEP 1 : Try Normal Digital Extraction ----------
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    # ---------- STEP 2 : If Empty → OCR Fallback ----------
    if len(text.strip()) < 50:   # SBI / Axis / Amex / Scanned PDFs
        file.seek(0)
        doc = fitz.open(stream=file.read(), filetype="pdf")

        ocr_text = ""
        for page in doc:
            pix = page.get_pixmap(dpi=300)
            img = Image.open(io.BytesIO(pix.tobytes()))
            ocr_text += pytesseract.image_to_string(img, lang="eng")

        text = ocr_text

    return text
