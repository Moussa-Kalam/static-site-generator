import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is an italic text node", TextType.ITALIC, 'https://www.google.com')
        self.assertEqual(repr(node), "TextNode(This is an italic text node, italic, https://www.google.com)")
        self.assertNotEqual(
            repr(node),
            "TextNode(This is an italic text node, normal, https://www.google.com)"
        )
        self.assertNotEqual(
            repr(node),
            "TextNode(This is an italic text node, italic, None)"
        )

    def test_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.google.com")
        self.assertEqual(node.url, "https://www.google.com")
        self.assertNotEqual(node.url, "https://www.youtube.com")

    def test_url_none(self):
        node = TextNode("This is a link", TextType.LINK)
        self.assertEqual(node.url, None)

    def test_text_type(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertNotEqual(node.text_type, TextType.ITALIC)

    def test_text(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        self.assertEqual(node.text, "This is a bold text node")
        self.assertNotEqual(node.text, "This is a normal text node")


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_text_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")



if __name__ == '__main__':
    unittest.main()
