from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text"),ParentNode("p",[LeafNode("b","Bold Tex"), LeafNode("i","italic text")])])
        ],
    )

    print(node.to_html())

   
    
main()