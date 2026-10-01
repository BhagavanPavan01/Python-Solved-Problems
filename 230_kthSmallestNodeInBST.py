class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):

    result = []

    def inorder(node, result):
        if node:
            inorder(node.left, result)

            result.append(node.val)

            if len(result) == k:
                return result[-1]

            inorder(node.right, result)

    inorder(root, result)

    return result[k - 1]


# Create tree
root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.left.left.left = TreeNode(1)

k = 2

print(kthSmallest(root, k))