class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props={}):
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
            