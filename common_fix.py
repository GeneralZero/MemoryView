from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re

class CommonFixExtention(Extension):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        """ Add FencedBlockPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        md.preprocessors.register(NewLineAfterList(md), 'common_fix', 5)


class NewLineAfterList(Preprocessor):
    """ Skip any line with words 'NO RENDER' in it. """
    def run(self, lines):
        new_lines = []
        not_empty_last_line = True

        for line in lines:
            if bool(re.search(r'^[ ]{0,3}((\d+\.)|[*+-])[ ]+(.*)', line)) and not_empty_last_line:    
                # Append a new line before the list if the previous one was empty
                new_lines.append("")  
                new_lines.append(line)
                #print("Found Line: {}".format(line))
            
            else:
                new_lines.append(line)
            
            not_empty_last_line = (line.strip() != '')

        return new_lines

def makeExtension(**kwargs):  # pragma: no cover
    return CommonFixExtention(**kwargs)


if __name__ == "__main__":
    import markdown
    data = open("/opt/Memory/Crypto/Asymmetric Encryption/ECC.md", "r")
    html = markdown.markdown(data.read(), extensions=['common_fix:CommonFixExtention'])
    print(html)