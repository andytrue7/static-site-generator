import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "container"})
        self.assertEqual(node.props_to_html(), " class=\"container\"")

    def test_default_props_to_html(self):
        node = HTMLNode("div", "Hello, world!")
        self.assertEqual(node.props_to_html(), "")