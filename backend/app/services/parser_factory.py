from app.services.parsers.icici import ICICIParser
from app.services.parsers.hdfc import HDFCParser
from app.services.parsers.sbi import SBIParser
from app.services.parsers.axis import AxisParser
from app.services.parsers.amex import AmexParser


def get_parser(bank: str, text: str):
    bank = bank.upper()

    factory = {
        "ICICI": ICICIParser,
        "HDFC": HDFCParser,
        "SBI": SBIParser,
        "AXIS": AxisParser,
        "AMEX": AmexParser,
    }

    parser_class = factory.get(bank)

    if not parser_class:
        return None

    return parser_class(text)
