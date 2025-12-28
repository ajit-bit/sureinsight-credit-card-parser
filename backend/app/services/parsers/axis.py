from app.services.base_parser import BaseParser

class AxisParser(BaseParser):
    def parse(self):
        return {
            "bank": "Axis Bank",

            # 01 Aug 2024 - 31 Aug 2024
            "billing_cycle": self.find(
                r"Statement Period\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4}\s*-\s*\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 07 Sep 2024
            "due_date": self.find(
                r"Payment Due Date\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 01 Sep 2024
            "statement_issue_date": self.find(
                r"Statement Date\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})"
            ),

            # 8,600.00
            "previous_balance": self.find(
                r"Previous Balance\s+([\d,]+\.\d{2})"
            ),

            # 21,400.00
            "outstanding_amount": self.find(
                r"Total Amount Due\s+([\d,]+\.\d{2})"
            ),

            # 1,070.00
            "minimum_due": self.find(
                r"Minimum Amount Due\s+([\d,]+\.\d{2})"
            ),

            # 60,000.00
            "credit_limit": self.find(
                r"Credit Limit\s+([\d,]+\.\d{2})"
            ),

            # 38,600.00
            "available_credit": self.find(
                r"Available Credit\s+([\d,]+\.\d{2})"
            ),

            # 21,400.00
            "used_credit": self.find(
                r"Used Credit\s+([\d,]+\.\d{2})"
            ),

            # 950
            "reward_points": self.find(
                r"Points Earned\s+(\d+)"
            ),
        }
