from app.services.base_parser import BaseParser

class SBIParser(BaseParser):
    def parse(self):
        return {
            "bank": "State Bank of India",

            # 16 July 2024 to 15 August 2024
            "billing_cycle": self.find(
                r"Statement Period\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4}\s+to\s+\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 03 September 2024
            "due_date": self.find(
                r"Payment Due Date\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 16 August 2024
            "statement_issue_date": self.find(
                r"Statement Issue Date\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 13,385.00
            "previous_balance": self.find(
                r"Previous Balance\s+([\d,]+\.\d{2})"
            ),

            # 23,458.00
            "outstanding_amount": self.find(
                r"Total Amount Due\s+([\d,]+\.\d{2})"
            ),

            # 1,880.00
            "minimum_due": self.find(
                r"Minimum Amount Due\s+([\d,]+\.\d{2})"
            ),

            # 50,000.00
            "credit_limit": self.find(
                r"Total Credit Limit\s+([\d,]+\.\d{2})"
            ),

            # 15,842.00
            "available_credit": self.find(
                r"Available Credit\s+([\d,]+\.\d{2})"
            ),

            # 9,600.00
            "used_credit": self.find(
                r"Used Credit\s+([\d,]+\.\d{2})"
            ),

            # 744
            "reward_points": self.find(
                r"Points Earned\s+(\d+)"
            ),
        }
