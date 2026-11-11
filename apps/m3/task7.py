import sys

from bs4 import BeautifulSoup, SoupReplacer


def add_test_class(tag):
    if tag.name == "p":
        # same as `{ ...tag.attrs, class: "test" }` in javascript
        return {**tag.attrs, "class": "test"}
    return tag.attrs


path = sys.argv[1]
replacer = SoupReplacer(attrs_xformer=add_test_class)

with open(path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser", replacer=replacer)

out_path = path + ".class_text.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print("now all the <p> has class 'test' in this file:", out_path)
