def write(markdown: str, style_name: str='jes_output') -> str:    
    with open(f'{style_name}.md', 'w') as f:
        f.write(markdown)
