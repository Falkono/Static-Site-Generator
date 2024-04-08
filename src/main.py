from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():

    textHtml = TextNode("Test","code")
    textgoogle = TextNode("google", "link", "google.com")

    print(textHtml.text_node_to_html_node())
    
    print(textgoogle.text_node_to_html_node())
   
    
main()