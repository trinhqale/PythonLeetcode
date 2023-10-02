class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_ascii_tree(root, prefix="", is_left=True):
    if root is not None:
        if level == 0:
            print(prefix + str(root.val))
        else:
            print(" " * (level * 4 - 2) + ("L--- " if is_left else "R--- ") + str(root.val))
        if root.left is not None or root.right is not None:
            print_ascii_tree(root.left, level + 1, "L--- ", True)
            print_ascii_tree(root.right, level + 1, "R--- ", False)