import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is also a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is a text node", TextType.ITALIC, "string")
        node6 = TextNode("This is a text node", TextType.ITALIC, "string")
        node7 = TextNode("This is a text node", TextType.ITALIC, None)
        
        self.assertEqual(node, node2)
        self.assertEqual(node6, node5)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)
        self.assertNotEqual(node7, node5)


if __name__ == "__main__":
    unittest.main()