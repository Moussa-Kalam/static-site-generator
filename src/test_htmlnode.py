import unittest

from htmlnode import HTMLNode

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

if __name__ == '__main__':
    unittest.main()