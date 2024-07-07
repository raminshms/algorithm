from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root: TreeNode):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        s = 0
        for _ in range(levelSize):
            node: TreeNode = queue.popleft()
            s += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        a = s / levelSize
        result.append(a)
    
    return result


def test():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(averageOfLevels(root))


test()
        
