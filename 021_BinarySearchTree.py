

#  ============== Binary Search Tree ===============

# creating the base treenode class =======


class TreeNode:
    def __init__(self,val = 0):
        self.val = val
        self.left = None
        self.right = None
        
def insert(root,val):
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
        
    return root


def dfs(root):
    if root is None:
        return
    
    print(root.val, end = " ")
    dfs(root.left)
    dfs(root.right)
    


#  creating a tree using a list


values = [7,8,6,4,8,3,2,1,5,6,8,9,5,6,8,8]

root = None

for value in values:
    root = insert(root,value)

dfs(root)
        