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

def split_nodes_image(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            alt, link = image
            image_node = TextNode(alt, TextType.IMAGE, link)
            test_without_image = node.text.split(f"![{alt}]({link})")
            if test_without_image[0]:
                new_nodes.append(TextNode(test_without_image[0], TextType.TEXT))
            new_nodes.append(image_node)
            node.text = test_without_image[1]
        if node.text:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        
        for link_ in links:
            alt, link = link_
            link_node = TextNode(alt, TextType.LINK, link)
            test_without_link_ = node.text.split(f"[{alt}]({link})")
            if test_without_link_[0]:
                new_nodes.append(TextNode(test_without_link_[0], TextType.TEXT))
            new_nodes.append(link_node)
            node.text = test_without_link_[1]
        if node.text:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
    return new_nodes