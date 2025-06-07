import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
