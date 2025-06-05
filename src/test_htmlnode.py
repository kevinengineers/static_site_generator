import unittest
from htmlnode import HTMLNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode("<a>", "value", "<p>", {"href": "https://www.google.com"})
        html_node_repr = html_node.props_to_html()
        expected_value = "href=\"https://www.google.com\" "
        self.assertEqual(expected_value, html_node_repr)


    def test_leaf_to_html(self):
        node = LeafNode("a", "https://www.google.com")
        self.assertEqual(node.to_html(), "<a>https://www.google.com</a>")

        node2 = LeafNode("p", "This is a paragraph.")
        self.assertEqual("<p>This is a paragraph.</p>", node2.to_html())

        node3 = LeafNode("h1", "this is a level 1 heading")
        self.assertNotEqual("<h1>This is a level 1 heading.</h1>", node3)

if __name__ == "__main__":
    unittest.main()
