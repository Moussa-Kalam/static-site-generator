import os

from block_markdown import markdown_to_html_node


def extract_title(markdown):
	lines = markdown.split('\n')
	for line in lines:
		if line.startswith('# '):
			return line[2:]
	raise Exception("Header should start with #. No title found.")


def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")

	with open(from_path, "r", encoding="utf-8") as f:
		markdown_content = f.read()

	with open(template_path, "r", encoding="utf-8") as f:
		template = f.read()

	html_nodes = markdown_to_html_node(markdown_content).to_html()
	title = extract_title(markdown_content)
	updated_template = template.replace('{{ Title }}', title).replace('{{ Content }}', html_nodes)

	dest_dir_path = os.path.dirname(dest_path)
	if dest_dir_path != "":
		os.makedirs(dest_dir_path, exist_ok=True)

	with open(dest_path, "w", encoding="utf-8") as f:
		f.write(updated_template)
