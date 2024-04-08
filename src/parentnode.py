from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props={}):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag not provided")
        if self.children == None:
            raise ValueError("No Children provided")
        
    