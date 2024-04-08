import unittest

from parentnode import ParentNode

#TODO need some asserts for each function
class TestParentNode(unittest.TestCase):
    def test_only_leafnodes():
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

    def test_leafnodes_with_one_parent():
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text")])
            ],
        )

    def test_leafnodes_with_two_parents():
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text")]),
                ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text")])
            ],
        )

    def test_leafnodes_with_a_parent_with_a_parent():
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text"), ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text")])]),
            ],
        )
         

    def test_parent_without_tag_choiced():
        node = ParentNode(
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text"), ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text")])]),
            ],
        )

    def test_parent_without_tag_none():
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text"), ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text")])]),
            ],
        )

    def test_parent_without_tag_empty_string():
        node = ParentNode(
            "",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text"), ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text")])]),
            ],
        )

    def test_parent_without_childern_not_choiced():
            node = ParentNode("p")

    def test_parent_without_childern_empty_list():
            node = ParentNode("p",[])