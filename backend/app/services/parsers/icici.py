from app.services.base_parser import BaseParser


class ICICIParser(BaseParser):
    def parse(self):
        return {
            "bank": "ICICI Bank",

            "outstanding_amount": self.find(
                r"(?:Total Amount Due|Outstanding Amount|Total Outstanding)\s*:?\s*₹([\d,]+)"
            ),

            "minimum_due": self.find(
                r"(?:Minimum Amount Due|Minimum Due Amount|Minimum Due)\s*:?\s*₹([\d,]+)"
            ),

            "due_date": self.find(
                r"(?:Payment Due Date|Due Date)\s*:?\s*(\d{2}[/-]\d{2}[/-]\d{4})"
            ),

            "interest_rate": self.find(
                r"Interest Rate\s*:?\s*([\d.]+%)"
            ),

            "late_fee": self.find(
                r"(?:Late Payment Fee|Late Fee|Late Payment Charges)\s*:?\s*₹([\d,]+)"
            ),

            "transaction_count": self.transaction_count(),

            "top_spending_category": self.top_category(),
        }
