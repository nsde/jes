import sys
import pathlib
import requests

def parse() -> str:
    args = sys.argv

    style_file = None
    for arg in list(reversed(args)):
        if not arg.endswith('.py'):
            style_file = arg
            break

    if not style_file:
        raise SyntaxError('No stylesheet file given.')

    return (style_file, pathlib.Path(style_file).name)

def get_css(style_file: str) -> str:
    """Gets the CSS content from a file or URL."""

    if '://' in style_file:
        style_content = requests.get(style_file).text

    else:
        with open(style_file, 'r') as f:
            style_content = f.read()

    return style_content
