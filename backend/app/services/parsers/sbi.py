from app.services.base_parser import BaseParser


class SBIParser(BaseParser):
    def parse(self):
        return {
            "bank": "SBI Card",

            "outstanding_amount": self.find(
                r"(?:Total Amount Due|Total Outstanding|Closing Balance|Outstanding Amount)\s*:?\s*₹([\d,]+)"
            ),

            "minimum_due": self.find(
                r"(?:Minimum Amount Due|Minimum Due|Minimum Payment Due)\s*:?\s*₹([\d,]+)"
            ),

            "due_date": self.find(
                r"(?:Payment Due Date|Due Date)\s*:?\s*(\d{2}[/-]\d{2}[/-]\d{4})"
            ),

            "interest_rate": self.find(
                r"Interest Rate\s*:?\s*([\d.]+%)"
            ),

            "late_fee": self.find(
                r"(?:Late Payment Charges|Late Fee|Late Payment Fee)\s*:?\s*₹([\d,]+)"
            ),

            "transaction_count": self.transaction_count(),

            "top_spending_category": self.top_category(),
        }
