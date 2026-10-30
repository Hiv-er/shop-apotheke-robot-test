def parse_price(price: str) -> str:
    """Parse price from '€ 23,99' format to '23,99'"""
    return price.replace("€", "").replace("\u00a0", "").strip()
