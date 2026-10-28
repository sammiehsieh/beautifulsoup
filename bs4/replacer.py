class SoupReplacer:
    """
    Replaces every tag named og_tag with alt_tag while the tree is being built,
    so no second pass over the tree is needed.
    """

    def __init__(self, og_tag: str, alt_tag: str):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def replace(self, name: str) -> str:
        if name == self.og_tag:
            return self.alt_tag
        return name
