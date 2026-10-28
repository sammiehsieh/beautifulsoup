import sys

from bs4 import BeautifulSoup, SoupStrainer

only_with_id = SoupStrainer(id=True)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser", parse_only=only_with_id)

for tag in soup.find_all(id=True):
    print(tag.name, tag["id"])
