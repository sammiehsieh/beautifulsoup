import sys

from bs4 import BeautifulSoup, SoupStrainer

only_tags = SoupStrainer(True)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser", parse_only=only_tags)

for tag in soup.find_all(True):
    print(tag.name)
