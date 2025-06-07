from htmlnode import HTMLNode, ParentNode, LeafNode
import htmlnode
from textnode import TextNode

def main():
    a_node = HTMLNode("a", "href")
    p_leaf = LeafNode("p", "paragraph")
    parent = ParentNode("body", [a_node, p_leaf])
    print(parent.to_html())
    
main()

