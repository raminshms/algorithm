from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root: TreeNode):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        levelNodes = []
        for _ in range(levelSize):
            node = queue.popleft()
            levelNodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(levelNodes)

    return result


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(traverse(root))


test()
