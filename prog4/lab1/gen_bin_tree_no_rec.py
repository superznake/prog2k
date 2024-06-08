def gen_bin_tree_no_rec(height: int, root: int):
    tree = {str(root): []}
    buff = []
    left_func = lambda x: x * 2 + 1
    right_func = lambda x: x * 2 - 1
    while height > 0:
        height -= 1
        a = left_func(root)
        b = right_func(root)
        buff.append([a, b])

    return tree
