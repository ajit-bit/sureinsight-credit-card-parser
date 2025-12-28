import pytesseract
import os

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if not os.path.exists(TESSERACT_PATH):
    raise RuntimeError("Tesseract not found at " + TESSERACT_PATH)

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
