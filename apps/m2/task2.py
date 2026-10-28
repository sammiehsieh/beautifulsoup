import sys

from bs4 import BeautifulSoup, SoupStrainer

only_a = SoupStrainer("a")

with open(sys.argv[1], "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser", parse_only=only_a)

for a in soup.find_all("a", href=True):
    print(a["href"])