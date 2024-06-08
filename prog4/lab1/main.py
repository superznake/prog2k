import pprint as pp

from gen_bin_tree import gen_bin_tree
from gen_bin_tree_no_rec import gen_bin_tree_no_rec

if __name__ == '__main__':
    res = gen_bin_tree(root=9, height=6)
    pp.pprint(res)
    #res = gen_bin_tree_no_rec(root = 9, height = 6)
    #pp.pprint(res)