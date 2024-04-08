import unittest

from parentnode import ParentNode
from leafnode import LeafNode


#TODO need some asserts for each function
class TestParentNode(unittest.TestCase):
    def test_only_leafnodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_leafnodes_with_one_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text")])
            ],
        )
        
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b><i>italic text</i></p></p>")

    def test_leafnodes_with_two_parents(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text")]),
                ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text")])
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b><i>italic text</i></p><p><b>Bold text</b><i>italic text</i></p></p>")

    def test_leafnodes_with_a_parent_with_a_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text"), ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text")])]),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b><i>italic text</i><p><b>Bold text</b><i>italic text</i></p></p></p>")
         

    def test_parent_without_tag_choiced(self):
        node = ParentNode(
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text"), ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text")])]),
            ],
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_without_tag_none(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text"), ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text")])]),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()
        #raise Exception()

    def test_parent_without_tag_empty_string(self):
        node = ParentNode(
            "",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("b","Bold tex"), LeafNode("i","italic text"), ParentNode("p",[LeafNode("b","Bold text"), LeafNode("i","italic text")])]),
            ],
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_without_childern_not_choiced(self):
        node = ParentNode("p")
        
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_without_childern_empty_list(self):
        node = ParentNode("p",[])
        
        with self.assertRaises(ValueError):
            node.to_html()