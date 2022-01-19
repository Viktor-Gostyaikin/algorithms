# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    def comparator(node):
        if node.right == None and node.left == None:
            return True
        if node.left.value > node.value or node.right.value < node.value:
            return False
        if node.left.value > root.value or node.right.value < root.value:
            return False
        left = True
        rigth = True
        if node.left:
                left = comparator(node.left, root.value)
        if node.right and left:
            rigth = comparator(node.right, root.value)
        return left + rigth
    return comparator()

def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

test()