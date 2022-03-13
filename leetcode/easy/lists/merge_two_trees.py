from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 or not root2:
        return root1 or root2
    root = TreeNode(root1.val + root2.val)
    root.left = mergeTrees(root1.left, root2.left)
    root.right = mergeTrees(root1.right, root2.right)
    return root


tree_node_1_4 = TreeNode(val=5)
tree_node_1_3 = TreeNode(val=3, left=tree_node_1_4)
tree_node_1_2 = TreeNode(val=2)
tree_node_1_1 = TreeNode(val=1, left=tree_node_1_3, right=tree_node_1_2)

tree_node_2_5 = TreeNode(val=4)
tree_node_2_4 = TreeNode(val=7)
tree_node_2_3 = TreeNode(val=1, right=tree_node_2_5)
tree_node_2_2 = TreeNode(val=3, right=tree_node_2_4)
tree_node_2_1 = TreeNode(val=2, left=tree_node_2_3, right=tree_node_2_2)

r = mergeTrees(root1=tree_node_1_1, root2=tree_node_2_1)

print(r)
