def invertbinarytree(root):
    if not root:
        return None
    root.left, root.right = invertbinarytree.invertTree(root.right), invertbinarytree.invertTree(root.left)
    return root