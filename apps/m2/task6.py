import sys

from bs4 import BeautifulSoup, SoupReplacer

path = sys.argv[1]
replacer = SoupReplacer("b", "blockquote")

with open(path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser", replacer=replacer)

out_path = path + ".change_b.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print("Wrote", out_path)
