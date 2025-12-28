from app.services.base_parser import BaseParser

class AmexParser(BaseParser):
    def parse(self):
        return {
            "bank": "American Express",

            # 01 Aug 2024 - 31 Aug 2024
            "billing_cycle": self.find(
                r"Statement Period\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4}\s*-\s*\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 10 Sep 2024
            "due_date": self.find(
                r"Payment Due Date\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 31 Aug 2024
            "statement_issue_date": self.find(
                r"Statement Date\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 18,200.00
            "previous_balance": self.find(
                r"Previous Balance\s+([\d,]+\.\d{2})"
            ),

            # 42,900.00
            "outstanding_amount": self.find(
                r"Total Amount Due\s+([\d,]+\.\d{2})"
            ),

            # 2,150.00
            "minimum_due": self.find(
                r"Minimum Amount Due\s+([\d,]+\.\d{2})"
            ),

            # 1,50,000.00
            "credit_limit": self.find(
                r"Credit Limit\s+([\d,]+\.\d{2})"
            ),

            # 1,07,100.00
            "available_credit": self.find(
                r"Available Credit\s+([\d,]+\.\d{2})"
            ),

            # 42,900.00
            "used_credit": self.find(
                r"Used Credit\s+([\d,]+\.\d{2})"
            ),

            # 3400
            "reward_points": self.find(
                r"Points Earned\s+(\d+)"
            ),
        }
