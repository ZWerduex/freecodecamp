def parse_link(markdown):
    text, link = markdown[1:-1].split('](')
    return f'<a href="{link}">{text}</a>'