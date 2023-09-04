import re

def is_valid_payeer_wallet(wallet):
    pattern = r'^P\d{8}$'

    if re.match(pattern, wallet):
        return True
    else:
        return False