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
