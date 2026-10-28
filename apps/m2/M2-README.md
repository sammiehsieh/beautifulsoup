# Milestone-2

## Part 2: Where the API functions are defined (original source, before changes)

| API used | File | Line |
|---|---|---|
| `BeautifulSoup` (class) | `bs4/__init__.py` | 133 |
| `BeautifulSoup.__init__` (constructor, takes `parse_only`) | `bs4/__init__.py` | 209 |
| `Tag.prettify` | `bs4/element.py` | 2601 |
| `Tag.find_all` | `bs4/element.py` | 2715 |
| `PageElement.find_parent` | `bs4/element.py` | 992 |
| `Tag.select` | `bs4/element.py` | 2799 |
| `Tag.__getitem__` (`a["href"]`) | `bs4/element.py` | 2203 |
| `Tag.__setitem__` (`p["class"] = "test"`) | `bs4/element.py` | 2223 |
| `SoupStrainer` (class) | `bs4/filter.py` | 313 |

Notes:
- `find_all(True)` and `find_all(id=True)` (tasks 3, 4) call the same `find_all`.
- `tag.name = "blockquote"` (task 6) is an attribute assignment, not a function.