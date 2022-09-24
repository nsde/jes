import cssutils

import sysutils

md = ''

def add(new_line: str='', prefix: str='') -> str:
    """Simply adds a new line to the markdown document."""
    global md
    md += f'{prefix + " " if prefix else ""}{new_line}\n' 

def documentate(css: str, style_name: str) -> str:
    """Parses the CSS and writes the documentation accordingly."""
    global md
    add(f'Stylesheet Documentation · **`{style_name}`**', '#')

    with sysutils.HidePrints(): # block unnecessary false-positive warnings | Does not seem to work on Manjaro Linux (24/09/2022)
        sheet = cssutils.parseString(css) # remove "print hider" if you are experiencing problems!
    
    add(f'**Rules:** {len([rule for rule in sheet if rule.type == rule.STYLE_RULE])} · ')
    add(f'**Comments:** {len([rule for rule in sheet if rule.type == rule.COMMENT])} · ')
    add(f'**Total rules:** {len([rule for rule in sheet])}')
    add('---')

    for rule in sheet:
        if rule.type == rule.STYLE_RULE:
            add(f'`{rule.selectorText}`', '##')
            add(md)
            add('This selector affects the following properties:')
            
            for details in rule.style:
                add(f'`{details.name}`', '-')
    
        if rule.type == rule.COMMENT:
            add(md)
            comment = rule.cssText.split('/*')[1].split('*/')[0]
            add(comment, '>')
    
    return md
