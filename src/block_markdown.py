from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "quote"
	UNORDERED_LIST = "unordered_list"
	ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
	blocks = markdown.split("\n\n")
	filtered_blocks = []
	for block in blocks:
		if block == "":
			continue
		block = block.strip()
		filtered_blocks.append(block)
	return filtered_blocks


def block_to_block_type(markdown_block):
	lines = markdown_block.split("\n")

	if markdown_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
		return BlockType.HEADING
	if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
		return BlockType.CODE
	if markdown_block.startswith(">"):
		for line in lines:
			if not line.startswith(">"):
				return BlockType.PARAGRAPH
		return BlockType.QUOTE
	if markdown_block.startswith("- "):
		for line in lines:
			if not line.startswith("- "):
				return BlockType.PARAGRAPH
		return BlockType.UNORDERED_LIST
	if markdown_block.startswith("1. "):
		i = 1
		for line in lines:
			if not line.startswith(f"{i}. "):
				return BlockType.PARAGRAPH
			i += 1
		return BlockType.ORDERED_LIST
	return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)
	children = []
	for block in blocks:
		html_node = block_to_html_node(block)
		children.append(html_node)
	return ParentNode("div", children)


def block_to_html_node(markdown_block):
	block_type = block_to_block_type(markdown_block)
	if block_type == BlockType.PARAGRAPH:
		return paragraph_to_html_node(markdown_block)
	if block_type == BlockType.HEADING:
		return heading_to_html_node(markdown_block)
	if block_type == BlockType.CODE:
		return code_to_html_node(markdown_block)
	if block_type == BlockType.ORDERED_LIST:
		return ordered_list_to_html_node(markdown_block)
	if block_type == BlockType.UNORDERED_LIST:
		return unordered_list_to_html_node(markdown_block)
	if block_type == BlockType.QUOTE:
		return quote_to_html_node(markdown_block)
	raise ValueError(f"Unknown block type: {block_type}")


def text_to_children(text):
	text_nodes = text_to_textnodes(text)
	children = []
	for text_node in text_nodes:
		html_node = text_node_to_html_node(text_node)
		children.append(html_node)
	return children


def paragraph_to_html_node(block):
	lines = block.split("\n")
	paragraph = " ".join(lines)
	children = text_to_children(paragraph)
	return ParentNode("p", children)


def heading_to_html_node(block):
	level = 0
	for char in block:
		if char == "#":
			level += 1
		else:
			break
	if level + 1 >= len(block):
		raise ValueError(f"Invalid heading level: {level}")
	text = block[level + 1:]
	children = text_to_children(text)
	return ParentNode(f"h{level}", children)


def code_to_html_node(block):
	if not block.startswith("```") or not block.endswith("```"):
		raise ValueError(f"Invalid code block: {block}")
	text = block[4:-3]
	raw_text_node = TextNode(text, TextType.TEXT)
	child = text_node_to_html_node(raw_text_node)
	code = ParentNode("code", [child])
	return ParentNode("pre", [code])


def ordered_list_to_html_node(block):
	items = block.split("\n")
	list_items = []
	for item in items:
		text = item[3:]
		children = text_to_children(text)
		list_items.append(ParentNode('li', children))
	return ParentNode("ol", list_items)


def unordered_list_to_html_node(block):
	items = block.split("\n")
	list_items = []
	for item in items:
		text = item[2:]
		children = text_to_children(text)
		list_items.append(ParentNode('li', children))
	return ParentNode("ul", list_items)


def quote_to_html_node(block):
	lines = block.split("\n")
	new_lines = []
	for line in lines:
		if not line.startswith(">"):
			raise ValueError(f"Invalid quote block: {block}")
		new_lines.append(line.lstrip(">").strip())
	quote_text = " ".join(new_lines)
	children = text_to_children(quote_text)
	return ParentNode("blockquote", children)
