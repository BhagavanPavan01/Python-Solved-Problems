class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(values):
    if not values or values[0] is None:
        return None

    nodes = []

    # Create TreeNodes
    for value in values:
        if value is None:
            nodes.append(None)
        else:
            nodes.append(TreeNode(value))

    # Connect nodes
    for i in range(len(nodes)):
        if nodes[i] is not None:

            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]

            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]

    return nodes[0]


def kthSmallest(root, k):

    result = []

    def inorder(node):
        if node:
            inorder(node.left)

            result.append(node.val)

            inorder(node.right)

    inorder(root)

    return result[k - 1]


# Input
values = [5, 3, 6, 2, 4, None, None, 1]

k = 3

root = buildTree(values)

print(kthSmallest(root, k))