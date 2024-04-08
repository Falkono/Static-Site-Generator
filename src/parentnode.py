from htmlnode import HTMLNode

#TODO need to be tested

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props={}):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Tag not provided")
        if self.children == []:
            raise ValueError("No Children provided")
        
        output_string = ""
        for child in self.children:
            output_string += child.to_html()
        return f"<{self.tag}>{output_string}</{self.tag}>"

    