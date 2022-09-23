import cssutils

import sysutils

md = ''

def add(markdown_content: str, new_line: str='', prefix: str='') -> str:
    global md
    md += f'{prefix + " " if prefix else ""}{new_line}\n' 

def documentate(css: str, style_name: str) -> str:
    global md
    add(md, f'Stylesheet Documentation · **`{style_name}`**', '#')

    with sysutils.HidePrints(): # block unnecessary false-positive warnings | Does not seem to work on Manjaro Linux (24/09/2022)
        sheet = cssutils.parseString(css) # remove "print hider" if you are experiencing problems!
    
    add(md, f'**Rules:** {len([rule for rule in sheet if rule.type == rule.STYLE_RULE])} · ')
    add(md, f'**Comments:** {len([rule for rule in sheet if rule.type == rule.COMMENT])} · ')
    add(md, f'**Total rules:** {len([rule for rule in sheet])}')
    add(md, '---')

    for rule in sheet:
        if rule.type == rule.STYLE_RULE:
            add(md, f'`{rule.selectorText}`', '##')
            add(md)
            add(md, 'This selector affects the following properties:')
            
            for details in rule.style:
                add(md, f'`{details.name}`', '-')
    
        if rule.type == rule.COMMENT:
            add(md)
            comment = rule.cssText.split('/*')[1].split('*/')[0]
            add(md, comment, '>')
    
    return md
