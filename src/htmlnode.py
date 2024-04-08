class HTMLNode:
    # tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    # value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    # children - A list of HTMLNode objects representing the children of this node
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def __init__(self, tag=None, value=None, children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        prop_string = ""
        
        for key, value in self.props.items():
            prop_string += f" {key}=\"{value}\""
        
        return prop_string 
    
    def __repr__(self):
        return f"(tag={self.tag} \n value={self.value} \n children={self.children} \n props={self.props}"
            