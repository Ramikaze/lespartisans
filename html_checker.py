import os
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', 'svg', 'path', 'polygon', 'rect', 'circle'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if not self.stack:
            print(f"[Error] {self.filename}: Unmatched closing tag </{tag}> at line {self.getpos()[0]}")
            return
        expected_tag, pos = self.stack.pop()
        if expected_tag != tag:
            # Simple fallback for some HTML5 optional tags
            if expected_tag in ('p', 'li', 'dt', 'dd', 'rb', 'rt', 'rtc', 'rp', 'optgroup', 'option', 'colgroup', 'thead', 'tbody', 'tfoot', 'tr', 'td', 'th'):
                # Pop until we find the match or empty
                while self.stack and self.stack[-1][0] != tag:
                    self.stack.pop()
                if self.stack:
                    self.stack.pop()
            else:
                print(f"[Error] {self.filename}: Expected </{expected_tag}> but found </{tag}> at line {self.getpos()[0]}")

    def close(self):
        super().close()
        for tag, pos in self.stack:
            if tag not in ('p', 'li', 'meta', 'link'): # ignore optional closing tags
                print(f"[Warning] {self.filename}: Unclosed tag <{tag}> at line {pos[0]}")

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                parser = MyHTMLParser(filepath)
                try:
                    parser.feed(file.read())
                    parser.close()
                except Exception as e:
                    print(f"Error parsing {filepath}: {e}")

