import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        firstHTMLNode = HTMLNode("a", "hello",props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(firstHTMLNode.props_to_html(),  f" href=\"https://www.google.com\" target=\"_blank\"")

