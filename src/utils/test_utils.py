import unittest

from src.utils.extract_markdown_images import extract_markdown_images, extract_markdown_links
from src.textnode import TextNode, TextType
from src.utils.split_nodes_delimiter import split_nodes_delimiter

class TestUtils(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is a text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], " ", TextType.TEXT)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This")
        self.assertEqual(new_nodes[1].text, "is")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_extract_markdown_images(self):
        text = ""
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_extract_markdown_images_with_image(self):
        text = "![alt text](https://example.com/image.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text", "https://example.com/image.jpg")])

    def test_extract_markdown_images_with_multiple_images(self):
        text = "![alt text 1](https://example.com/image1.jpg) ![alt text 2](https://example.com/image2.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text 1", "https://example.com/image1.jpg"), ("alt text 2", "https://example.com/image2.jpg")])

    def test_extract_markdown_links(self):
        text = ""
        links = extract_markdown_links(text)
        self.assertEqual(links, [])
        
    def test_extract_markdown_links_with_link(self):
        text = "[link text](https://example.com)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("link text", "https://example.com")])
