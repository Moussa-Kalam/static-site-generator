import re

from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_parts = node.text.split(delimiter)

            if len(node_parts) % 2 == 0:
                raise Exception(f"Invalid Markdown: unmatched delimiter '{delimiter}' in '{node.text}'")

            for index, part in enumerate(node_parts):
                if not part:
                    continue
                if index % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes


def extract_markdown_images(image_text):
    image_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", image_text)
    return image_matches


def extract_markdown_links(link_text):
    link_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", link_text)
    return link_matches


def split_nodes_image(old_nodes):
    return split_nodes_by_extractor(old_nodes, extract_markdown_images, TextType.IMAGE)


def split_nodes_link(old_nodes):
    return split_nodes_by_extractor(old_nodes, extract_markdown_links, TextType.LINK)


def split_nodes_by_extractor(old_nodes, extract_function, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        matches = extract_function(original_text)
        if len(matches) == 0:
            new_nodes.append(old_node)
            continue

        for url_text, url_link in matches:
            sections = original_text.split(f"{'!' if text_type == TextType.IMAGE else ''}[{url_text}]({url_link})", 1)
            if len(sections) != 2:
                raise ValueError(f"Invalid Markdown: {text_type.value} section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(url_text, text_type, url_link))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
