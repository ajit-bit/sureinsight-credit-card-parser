from app.services.base_parser import BaseParser

class HDFCParser(BaseParser):
    def parse(self):
        return {
            "bank": "HDFC Bank",

            # 01 Aug 2024 - 31 Aug 2024
            "billing_cycle": self.find(
                r"Statement Period\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4}\s*-\s*\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 05 September 2024
            "due_date": self.find(
                r"Payment Due Date\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 01 September 2024
            "statement_issue_date": self.find(
                r"Statement Date\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            "previous_balance": self.find(
                r"Previous Balance\s+([\d,]+\.\d{2})"
            ),

            "outstanding_amount": self.find(
                r"Total Amount Due\s+([\d,]+\.\d{2})"
            ),

            "minimum_due": self.find(
                r"Minimum Amount Due\s+([\d,]+\.\d{2})"
            ),

            "credit_limit": self.find(
                r"Credit Limit\s+([\d,]+\.\d{2})"
            ),

            "available_credit": self.find(
                r"Available Credit\s+([\d,]+\.\d{2})"
            ),

            "used_credit": self.find(
                r"Used Credit\s+([\d,]+\.\d{2})"
            ),

            "reward_points": self.find(
                r"Points Earned\s+(\d+)"
            ),
        }
