# Milestone 4

## What changed (bs4/ and apps/m4)

- `bs4/__init__.py`: `BeautifulSoup` now has an `__iter__` method. It is a generator. It starts at the first child (`soup.contents[0]`), yields one node, then moves to `next_element`, until there is no next node. It does not build a list.
- `apps/m4/iterable.py`: counts tags and other nodes with `for node in soup`. Run from the repo root: `PYTHONPATH=. python apps/m4/iterable.py <input_file>`
- Tests: `bs4/tests/test_iteration.py` (5 tests):
   1. nested tags come in document order
   2. text nodes are included
   3. an empty document yields nothing
   4. comment nodes are included
   5. iteration is lazy: `next()` gives one node at a time

## Technical brief: iterable BeautifulSoup

### How it works

Every node already points to the next node in document order (`next_element`). The parser sets this while it builds the tree. The iterator follows this chain. `yield` gives one node and pauses until the next one is asked for. No list of nodes is built.

### Design choices

- The root `soup.next_element` is `None`, so the walk starts at `soup.contents[0]`. If the document is empty, the iterator gives nothing and stops.
- Only the `BeautifulSoup` class is changed. A normal `Tag` still loops over its direct children, so existing code that loops over a tag works as before.
- `for x in soup` used to give only the top level children. Now it gives every node. `len(soup)` still counts direct children only, so it no longer matches the number of nodes iterated.
- The existing test suite still passes, so no old behavior covered by tests was broken.
