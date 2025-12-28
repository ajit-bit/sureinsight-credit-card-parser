import re

class BaseParser:
    def __init__(self, text: str):
        # Normalize currency symbols and artifacts
        text = text.replace("￿", " ").replace("₹", " ")
        self.text = re.sub(r"[ \t]+", " ", text)

    # Universal safe find
    def find(self, pattern):
        match = re.search(pattern, self.text, re.IGNORECASE)
        return match.group(1).replace(",", "").strip() if match else None

    def transaction_count(self):
        return len(re.findall(r"\n\d{2}/\d{2}/\d{4}", self.text))