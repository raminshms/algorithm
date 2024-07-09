from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findSuccessor(root: TreeNode, key):

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        for _ in range(levelSize):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if node.val == key:
                return queue[0] if queue else None


def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(findSuccessor(root, 3))


test()
