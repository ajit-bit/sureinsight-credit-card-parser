from app.services.base_parser import BaseParser

class ICICIParser(BaseParser):
    def parse(self):
        return {
            "bank": "ICICI Bank",

            # Not in model, but keeping for completeness as shown in output image
            "billing_cycle": self.find(
                r"Statement Period:\s*([A-Za-z]+\s+\d{1,2},\s*\d{4}\s*-\s*[A-Za-z]+\s+\d{1,2},\s*\d{4})"
            ),

            "due_date": self.find(
                r"Payment Due Date:\s*([A-Za-z]+\s+\d{1,2},\s*\d{4})"
            ),

            "previous_balance": self.find(
                r"Previous Balance\s*:?\s+([\d,]+\.\d{2})"
            ),

            "outstanding_amount": self.find(
                r"Total Amount Due\s*:?\s+([\d,]+\.\d{2})"
            ),

            "minimum_due": self.find(
                r"Minimum Amount Due\s*:?\s+([\d,]+\.\d{2})"
            ),

            "credit_limit": self.find(
                r"Total Credit Limit\s*:?\s+([\d,]+\.\d{2})"
            ),

            "available_credit": self.find(
                r"Available Credit\s*:?\s+([\d,]+\.\d{2})"
            ),

            "used_credit": self.find(
                r"(?:Used Balance|Used Credit)\s*:?\s+([\d,]+\.\d{2})"
            ),

            "reward_points": self.find(
                r"Points Earned:\s*(\d+)"
            ),

            "statement_issue_date": self.find(
                r"Statement Issue Date:\s*([A-Za-z]+\s+\d{1,2},\s*\d{4})"
            ),
        }