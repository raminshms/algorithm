from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findPaths(root: TreeNode, targetSum: int):
    allPaths = []
    findPathsRecursive(root, targetSum, [], allPaths)
    return allPaths


def findPathsRecursive(currentNode, targetSum, currentPath, allPaths):
    if not currentNode:
        return

    currentPath.append(currentNode.val)
    if currentNode.val == targetSum and not currentNode.left and not currentNode.right:
        allPaths.append(list(currentPath))
    else:
        findPathsRecursive(currentNode.left, targetSum -
                           currentNode.val, currentPath, allPaths)
        findPathsRecursive(currentNode.right, targetSum -
                           currentNode.val, currentPath, allPaths)

    del currentPath[-1]


def test():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)

    print(findPaths(root, 12))


test()
