from leafnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, text_node):
        return self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
        match self.text_type:
            case "text":
                return LeafNode(value=self.text)
            case "bold":
                return LeafNode("b", self.text)
            case "italic":
                return LeafNode("i", self.text)
            case "code":
                return LeafNode("code", self.text)
            case "link":
                return LeafNode("a", self.text, {"href": self.url})
            case "image":
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case _:
                raise Exception("Unvalid TextNode")