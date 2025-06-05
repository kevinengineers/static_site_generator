import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode("<a>", "value", "<p>", {"href": "https://www.google.com"})
        html_node_repr = html_node.props_to_html()
        expected_value = "href=\"https://www.google.com\" "
        self.assertEqual(expected_value, html_node_repr)

if __name__ == "__main__":
    unittest.main()
