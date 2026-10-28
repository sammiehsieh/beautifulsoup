from bs4 import BeautifulSoup, SoupReplacer


def test_replaces_b_with_blockquote():
    r = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup("<p>hi <b>there</b></p>", "html.parser", replacer=r)
    assert str(soup) == "<p>hi <blockquote>there</blockquote></p>"
    assert soup.find("b") is None


def test_other_tags_unchanged_and_nested_closes_correctly():
    r = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(
        "<div><b>one</b><i>two</i><b>three</b></div>", "html.parser", replacer=r
    )
    assert len(soup.find_all("blockquote")) == 2
    assert soup.find("i").get_text() == "two"
    assert soup.div.name == "div"
