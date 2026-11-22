import sys

from bs4 import BeautifulSoup, Tag

path = sys.argv[1]

with open(path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

tags = 0
others = 0
for node in soup:
    if isinstance(node, Tag):
        tags += 1
    else:
        others += 1

print("tags:", tags)
print("text and other nodes:", others)
