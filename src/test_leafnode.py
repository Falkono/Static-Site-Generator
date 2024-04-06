import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_no_prop(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), f"<p>This is a paragraph of text.</p>")
        
    def test_with_prop(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), f"<a href=\"https://www.google.com\">Click me!</a>")
        