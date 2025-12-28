def detect_bank(text: str):
    t = text.upper()

    if "STATE BANK OF INDIA" in t or "SBI CARD" in t:
        return "SBI"
    if "ICICI" in t:
        return "ICICI"
    if "HDFC" in t:
        return "HDFC"
    if "AXIS" in t:
        return "AXIS"
    if "AMERICAN EXPRESS" in t or "AMEX" in t:
        return "AMEX"

    return None
