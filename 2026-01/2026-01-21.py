import re

def parse_inline_code(md):
    return re.sub(r"`(.*?)`", r"<code>\1</code>", md)