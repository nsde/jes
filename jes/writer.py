import webbrowser

import logger

def write(markdown: str, style_name: str='jes_output') -> str:
    """Writes markdown content to a file."""
    output_file = f'{style_name}.md'
    with open(output_file, 'w') as f:
        f.write(markdown)

    logger.success(f'Successfully wrote to {output_file}')
    return output_file
