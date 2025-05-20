import unittest

from htmlnode import HTMLNode, LeafNode


class TextHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="Welcome!", props={"class": "text-bold", "ref": "pref"})
        self.assertEqual(node.props_to_html(), ' class="text-bold" ref="pref"')
        self.assertNotEqual(node.props_to_html(), ' class="text-italic" ref="pref"')

    def test_no_props(self):
        node = HTMLNode(tag="p", value="Welcome!")
        self.assertEqual(node.props, None)

    def test_node_value(self):
        node = HTMLNode(tag="p", value="Welcome!")
        self.assertEqual(node.value, "Welcome!")
        self.assertNotEqual(node.value, "Hello!")

    def test_node_tag(self):
        node = HTMLNode(tag="p", value="Welcome!")
        self.assertEqual(node.tag, "p")
        self.assertNotEqual(node.tag, "h1")

    def test_node_children(self):
        node = HTMLNode(tag="p", value="Welcome!", children="<span>Hello!</span>")
        self.assertEqual(node.children, "<span>Hello!</span>")
        self.assertNotEqual(node.children, "Hello!")

    def test_no_children(self):
        node = HTMLNode(tag="p", value="Welcome!")
        self.assertEqual(node.children, None)

    def test_repr(self):
        node = HTMLNode(tag="p", value="Welcome!", props={"class": "text-bold", "ref": "pref"})
        self.assertEqual(repr(node), "HTMLNode(p, Welcome!, None, {'class': 'text-bold', 'ref': 'pref'})")
        self.assertNotEqual(repr(node), "HTMLNode(p, Welcome!, None, {'class': 'text-italic', 'ref': 'pref'})")
        self.assertNotEqual(repr(node), "HTMLNode(p, Welcome!, None, {'class': 'text-bold'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == '__main__':
    unittest.main()
