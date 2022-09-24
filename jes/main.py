"""This is the most important file, starting all the different functions."""

import docs
import reader
import writer

style_file, style_name = reader.parse()
css_content = reader.get_css(style_file=style_file)
documentation = docs.documentate(css=css_content, style_name=style_name)

writer.write(markdown=documentation, style_name=style_name)
