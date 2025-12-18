def detect_bank(text: str) -> str:
    t = text.lower()
    if "icici" in t:
        return "ICICI"
    if "hdfc" in t:
        return "HDFC"
    if "state bank" in t or "sbi" in t:
        return "SBI"
    if "axis" in t:
        return "AXIS"
    if "american express" in t or "amex" in t:
        return "AMEX"
    return "UNKNOWN"
