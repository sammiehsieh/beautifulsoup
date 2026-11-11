# Milestone 3

## What changed (bs4/ and apps/m3)

- `bs4/replacer.py`: `SoupReplacer` now takes optional `name_xformer`, `attrs_xformer` and `xformer`. The old M2 style `SoupReplacer("b", "blockquote")` still works. It is turned into a `name_xformer` inside, so there is only one code path.
- `bs4/__init__.py`: `handle_starttag` creates the tag first, then calls `replacer.apply(tag)` before `pushTag`. `BeautifulSoup` also keeps a list `_renamed` of `(old_name, new_name)`. When `handle_endtag` sees `</b>`, it looks in this list from the end, finds the new name, and closes the right tag.
- `apps/m3/task7.py`: Milestone 1 task 7 using `attrs_xformer`.
- Tests: `bs4/tests/test_soupreplacer.py` (6 new tests, 8 in total):
   1. `name_xformer` renames a tag
   2. `xformer` deletes the class attribute
   3. `attrs_xformer` replaces attributes
   4. same-name tags renamed differently by attribute still close correctly
   5. no replacer: the tree is unchanged
   6. old and new style give the same result

## Technical brief: SoupReplacer in M2 vs M3

### M2: replacement pairs

`SoupReplacer("b", "blockquote")` is easy to read and easy to use. It swaps one tag name for another. But it can only change names. It cannot add, delete or change attributes, so it cannot do task 7.

### M3: transformer functions

`name_xformer`, `attrs_xformer` and `xformer` are functions, so users can do much more. Rename by rule, change attributes, or edit the tag directly. The costs:

- `BeautifulSoup` keeps an extra list `_renamed` so end tags find the new name.
- `attrs_xformer` must return the attributes in every branch. If one branch forgets, the tag gets `None`.
- `xformer` has side effects, so it is harder to trace who changed what.
- The name changes after the tag is created, so settings that depend on the old name are not updated.

### Recommendation

I recommend keeping both in one constructor. Use the pair style for simple renames, because it is short and clear. Use the functions when the change depends on attributes or needs more than a rename.