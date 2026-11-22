from bs4 import BeautifulSoup, Comment, NavigableString, Tag


def test_iterates_nested_tags():
    soup = BeautifulSoup("<html><body><p>hi</p></body></html>", "html.parser")
    # isinstance(n, Tag) is same as `typeof n === Tag`` in JavaScript
    names = [n.name for n in soup if isinstance(n, Tag)]
    assert names == ["html", "body", "p"]


def test_includes_text_nodes():
    soup = BeautifulSoup("<p>one<b>two</b>three</p>", "html.parser")
    texts = [str(n) for n in soup if isinstance(n, NavigableString)]
    assert texts == ["one", "two", "three"]


def test_empty_document_yields_nothing():
    soup = BeautifulSoup("", "html.parser")
    assert list(soup) == []


def test_includes_comment_nodes():
    soup = BeautifulSoup("<p>a<!-- note --></p>", "html.parser")
    comments = [n for n in soup if isinstance(n, Comment)]
    assert len(comments) == 1
    assert comments[0] == " note "


def test_iteration_is_lazy_generator():
    soup = BeautifulSoup("<div><p>a</p><p>b</p></div>", "html.parser")
    it = iter(soup)
    first = next(it)
    assert first.name == "div"
    assert next(it).name == "p"
