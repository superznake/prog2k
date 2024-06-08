from gen_bin_tree_no_rec import gen_bin_tree_no_rec


def test_type_of_zero_height_tree():
    assert type(gen_bin_tree_no_rec(root=9, height=0)['9']) is list

def test_val_treee_with_zero_height():
    assert gen_bin_tree_no_rec(root=9, height=0) == {'9':[]}

def test_val_treee_with_height_equals_to_one():
    assert gen_bin_tree_no_rec(root=9, height=1) == {'9': [{'19': []}, {'17': []}]}

def test_val_treee_with_height_equals_to_two():
    assert gen_bin_tree_no_rec(root=9, height=2) == {'9':[ {'19':[{'39':[]},{'37':[]}]}, {'17':[ {'35':[]},{'33':[]}]} ]}