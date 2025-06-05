from htmlnode import HTMLNode
from textnode import TextNode

def main():
    text_node = TextNode("anchor text", "link", "https://www.google.com")

    print(text_node)

    html_node = HTMLNode("href", "https://www.google.com", None, {"href": "https://www.google.com", "target": "_blank"})
    print(html_node.props_to_html())

main()

