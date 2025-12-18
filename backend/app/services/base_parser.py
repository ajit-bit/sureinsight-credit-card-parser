import re


class BaseParser:
    def __init__(self, text: str):
        self.text = text

    # ---------- SAFE VALUE EXTRACTOR ----------
    def find(self, pattern):
        match = re.search(pattern, self.text, re.IGNORECASE)
        return match.group(1).replace(",", "") if match else None

    # ---------- ACCURATE TRANSACTION COUNT ----------
    def transaction_count(self):
        return len(
            re.findall(r"\n\d{2}[/-]\d{2}[/-]\d{4}.*₹[\d,]+", self.text)
        )

    # ---------- ERROR-PROOF TOP CATEGORY ----------
    def top_category(self):
        categories = {
            "food": ["zomato", "swiggy", "starbucks"],
            "shopping": ["amazon", "flipkart", "myntra"],
            "travel": ["ola", "uber", "air india", "indigo"],
            "entertainment": ["netflix", "spotify"],
        }

        totals = {cat: 0 for cat in categories}
        lines = self.text.lower().splitlines()

        for line in lines:
            # extract amount safely
            amount_match = re.search(r"₹([\d,]+)", line)
            if not amount_match:
                continue

            amount = int(amount_match.group(1).replace(",", ""))

            # assign amount to correct category
            for category, keywords in categories.items():
                if any(keyword in line for keyword in keywords):
                    totals[category] += amount
                    break  # prevent double counting

        # return highest spending category
        return max(totals, key=totals.get) if max(totals.values()) > 0 else "Others"
