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


def test_name_xformer_renames_tag():
    r = SoupReplacer(
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
    )
    soup = BeautifulSoup("<p><b>hi</b></p>", "html.parser", replacer=r)
    assert str(soup) == "<p><blockquote>hi</blockquote></p>"


def test_xformer_deletes_class_attribute():
    def remove_class_attr(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]

    r = SoupReplacer(xformer=remove_class_attr)
    soup = BeautifulSoup('<p class="x">hi</p>', "html.parser", replacer=r)
    assert soup.p.get("class") is None


def test_attrs_xformer_replaces_attributes():
    r = SoupReplacer(attrs_xformer=lambda tag: {"id": "new"})
    soup = BeautifulSoup('<p class="x">hi</p>', "html.parser", replacer=r)
    assert soup.p["id"] == "new"
    assert soup.p.get("class") is None


def test_name_depends_on_attributes_nested():
    r = SoupReplacer(
        name_xformer=lambda tag: "blockquote" if tag.attrs.get("class") else tag.name
    )
    soup = BeautifulSoup(
        '<b class="x"><b>inner</b> tail</b>', "html.parser", replacer=r
    )
    assert soup.blockquote.b.get_text() == "inner"
    assert soup.blockquote.get_text() == "inner tail"


# while not using replacer, Beautiful can still perform as usual
def test_no_replacer_leaves_tree_unchanged():
    soup = BeautifulSoup("<p><b>hi</b></p>", "html.parser")
    assert str(soup) == "<p><b>hi</b></p>"


def test_old_and_new_style_give_same_result():
    html = "<div><b>one</b><i>two</i><b>three</b></div>"
    old = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))
    new = BeautifulSoup(
        html,
        "html.parser",
        replacer=SoupReplacer(
            name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
        ),
    )
    assert str(old) == str(new)
