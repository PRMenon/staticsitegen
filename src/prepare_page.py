import os
from pathlib import Path

from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n\n")
    try:
        title = next(line[1: ].strip() 
                     for line in lines 
                     if line.startswith("# "))
    except:
        raise Exception("H1 header is required")
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()
    title = extract_title(markdown)
    markdown_html = markdown_to_html_node(markdown).to_html()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", markdown_html)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True) 
    with open(dest_path,"w") as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)