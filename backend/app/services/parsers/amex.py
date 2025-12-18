from app.services.base_parser import BaseParser

class AmexParser(BaseParser):
    def parse(self):
        return {
            "bank": "American Express",

            "outstanding_amount": self.find(
                r"Total Balance Due\s*:?\s*₹([\d,]+)"
            ),

            "minimum_due": self.find(
                r"Minimum Amount Due\s*:?\s*₹([\d,]+)"
            ),

            "due_date": self.find(
                r"Payment Due By\s*:?\s*(\d{2}/\d{2}/\d{4})"
            ),

            "interest_rate": self.find(
                r"(?:Annual Percentage Rate|APR).*?([\d.]+%)"
            ),

            "late_fee": self.find(
                r"Late Payment Fee\s*:?\s*₹([\d,]+)"
            ),

            "transaction_count": self.transaction_count(),

            "top_spending_category": self.top_category(),
        }
