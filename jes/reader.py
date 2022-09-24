import sys
import pathlib
import requests

import logger

def parse() -> str:
    """This does not parse any CSS, but the command line arguments."""
    args = sys.argv

    style_file = None
    for arg in list(reversed(args)):
        if not arg.endswith('.py'):
            style_file = arg
            break

    if not style_file:
        raise SyntaxError('No stylesheet file given.')

    logger.info(f'Working with stylesheet {style_file}...')
    return (style_file, pathlib.Path(style_file).name)

def get_css(style_file: str) -> str:
    """
    Gets the stylesheet content from a file or URL.
    The URL has contain the raw contents of the style sheet.
    """

    if '://' in style_file:
        style_content = requests.get(style_file).text
        logger.success(f'Successfully requested stylesheet content of {style_file}')

    else:
        with open(style_file, 'r') as f:
            style_content = f.read()
        logger.success(f'Successfully read stylesheet content of {style_file}')

    return style_content
