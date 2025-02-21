import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            new_nodes.append(node)
        else:
            if node.text.count(delimiter) % 2:
                raise ValueError("unmatched delimiters")           
            parts = node.text.split(delimiter)
            nodes = []
            for i, part in enumerate(parts):
                if part:
                    nodes.append(TextNode(part, 
                                          text_type if i % 2 
                                          else TextType.TEXT))
            new_nodes.extend(nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)