from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode

def main():
    text_node = TextNode("anchor text", "link", "https://www.google.com")

    print(text_node)

    html_node = HTMLNode("href", "https://www.google.com", None, {"href": "https://www.google.com", "target": "_blank"})
    print(html_node.props_to_html())

    leaf_node = LeafNode("a", "href=something")
    leaf_node2 = LeafNode("p", "paragraph")
    parent_node = ParentNode("a", [leaf_node, leaf_node2])
    print(parent_node.to_html())
main()

