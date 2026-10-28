# Milestone 2

## Part 1: SoupStrainer (apps/m2)

- task2.py: `SoupStrainer("a")`, parse only `<a>` tags.
- task3.py: `SoupStrainer(True)`, keep all tags. This task needs every tag, so there is little to filter out.
- task4.py: `SoupStrainer(id=True)`, keep only tags with an id.

Run on treebank.xml (82 MB), which has no `<a>` and no id:
task2 14.0 s, task3 64.0 s, task4 13.7 s.
Times are wall-clock, measured with `time` on this machine.
task2 and task4 are fast here because almost no nodes are kept. This is not a like-for-like comparison with the Milestone 1 scripts.

## Part 2: Where the API functions are defined (original source, before changes)

| API used | File | Line |
|---|---|---|
| `BeautifulSoup` (class) | `bs4/__init__.py` | 133 |
| `BeautifulSoup.__init__` | `bs4/__init__.py` | 209 |
| `Tag.prettify` | `bs4/element.py` | 2601 |
| `Tag.find_all` | `bs4/element.py` | 2715 |
| `PageElement.find_parent` | `bs4/element.py` | 992 |
| `Tag.select` | `bs4/element.py` | 2799 |
| `Tag.__getitem__` | `bs4/element.py` | 2203 |
| `Tag.__setitem__` | `bs4/element.py` | 2223 |
| `SoupStrainer` (class) | `bs4/filter.py` | 313 |

`find_all(True)` and `find_all(id=True)` call the same `find_all`.

## Part 3: SoupReplacer

- `bs4/replacer.py`: `SoupReplacer(og_tag, alt_tag)` with a `replace(name)` method.
- `bs4/__init__.py`: `BeautifulSoup.__init__` takes an optional `replacer` argument. `handle_starttag` and `handle_endtag` rename the tag through the replacer, so the replacement happens while the tree is built. Both must be renamed, otherwise `</b>` cannot find `blockquote` on the stack.
- `apps/m2/task6.py`: Milestone 1 task 6 using `SoupReplacer("b", "blockquote")`.
- Tests: `bs4/tests/test_soupreplacer.py` (2 tests):
   1.  `<b>` becomes `<blockquote>` and no `<b>` remains
   2.  other tags are untouched and multiple replacements close correctly.