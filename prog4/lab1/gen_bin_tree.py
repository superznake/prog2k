import gen_bin_tree_exceptions


# базовый вариант сигнатуры функции
def gen_bin_tree(height: int, root: int):
    tree = {str(root): []}
    left_func = lambda x: x*2+1
    right_func = lambda x: x*2-1
    
    if height == 0:
        return tree
    else:
        l_l = left_func(root)
        r_l = right_func(root)
        a = gen_bin_tree(root=l_l, height = height -1)
        b = gen_bin_tree(root=r_l, height = height -1)
        tree[str(root)] = [a,b]
        return tree

# TODO
# расширенный, нерекурсивный вариант
# def gen_bin_tree(height: int, root: int, left_leaf_f, right_leaf_f):
#     pass