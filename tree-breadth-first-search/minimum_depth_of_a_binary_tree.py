from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minimumDepth(root: TreeNode):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    minDepth = 1

    while queue:
        levelSize = len(queue)
        for _ in range(levelSize):
            node: TreeNode = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if not node.left and not node.right:
                return minDepth

        minDepth += 1

    return minDepth


def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)

    print(minimumDepth(root))


test()
