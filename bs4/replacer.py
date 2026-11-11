class SoupReplacer:
    """
    Transform tags while the tree is being built

    Old style: SoupReplacer("b", "blockquote")
    New style: SoupReplacer(name_xformer, attr_xformer, xformer)
    p.s. These xformer are all functions
    """

    def __init__(
        self,
        og_tag=None,
        alt_tag=None,
        name_xformer=None,
        attrs_xformer=None,
        xformer=None,
    ):
        if og_tag is not None and name_xformer is None:

            def rename(tag):
                if tag.name == og_tag:
                    return alt_tag
                return tag.name

            name_xformer = rename

        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    def apply(self, tag):
        """
        Apply the three transformers to a freshly built tag.
        """
        if self.name_xformer:
            tag.name = self.name_xformer(tag)
        if self.attrs_xformer:
            tag.attrs = self.attrs_xformer(tag)
        if self.xformer:
            self.xformer(tag)
