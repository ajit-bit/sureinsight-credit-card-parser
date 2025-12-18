from app.services.parsers.icici import ICICIParser
from app.services.parsers.hdfc import HDFCParser
from app.services.parsers.sbi import SBIParser
from app.services.parsers.axis import AxisParser
from app.services.parsers.amex import AmexParser

def get_parser(bank, text):
    return {
        "ICICI": ICICIParser,
        "HDFC": HDFCParser,
        "SBI": SBIParser,
        "AXIS": AxisParser,
        "AMEX": AmexParser,
    }.get(bank, None)(text)
