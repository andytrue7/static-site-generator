from src.textnode import TextNode, TextType
from src.utils.extract_markdown_images import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        current_text = node.text
        images = extract_markdown_images(current_text)
        if not images:
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            parts = current_text.split(f"![{alt_text}]({url})", 1)
            if len(parts) != 2:
                raise ValueError(f"Invalid markdown image: {current_text}")
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            current_text = parts[1] if len(parts) > 1 else ""
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        current_text = node.text
        links = extract_markdown_links(current_text)
        if not links:
            new_nodes.append(node)
            continue

        for text, url in links:
            parts = current_text.split(f"[{text}]({url})", 1)
            if len(parts) != 2:
                raise ValueError(f"Invalid markdown link: {current_text}")
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url))
            current_text = parts[1] if len(parts) > 1 else ""
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes