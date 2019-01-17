# SHIV's
# takes in a pandas dataframe with heirachal structure and spits out a tree
import pandas as pd

class cool_tree:
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj
        self.children = []
    
    def add_child(self, child):
        assert(type(child) == type(self)), "Child must be of type 'cool tree'"
        self.children.append(child)
    
    def descendants(self):
        kids = []
        key = {}
        if not self.children:
            return {self.name: None}
        for child in self.children:
            kids.append(child.descendants())
        key[self.name] = kids
        return key
    
    def isleaf(self):
        if not self.children: return True
        else: return False
    
    def leaves(self):
        if self.isleaf():
            return self.obj
        leafs = []
        for L in self.children:
            mid_leaf = L.leaves()
            if type(mid_leaf) == float: leafs.append(mid_leaf)
            else: leafs.extend(L.leaves())
        return leafs

def pandas_2_tree(root, frame, cost):
    top_level = frame.columns.tolist()[0]
    unique_levels = frame[top_level].unique().tolist()
    cost_red = cost/len(unique_levels)
    for lev in unique_levels:
        curr_lev = cool_tree(lev, cost_red)
        idxs = frame.index
        temp = frame[frame[top_level] == lev].drop(columns=[top_level])
        if not temp.empty:
            root.add_child(pandas_2_tree(curr_lev, temp, cost_red))
        else:
            root.add_child(curr_lev)
    return root

#tests
def test():
    data = [[1, 2, 3 ,5, 6, 7],
           [1, 3, 2, 1, 3, 9],
           [1, 3, 4, 4, 5, 6]]
    cols = [chr(i+65) for i in data[0] ]
    df = pd.DataFrame(data, columns=cols)

    # this example demonstrates cost trickle down mechanism
    root = pandas_2_tree(cool_tree('root', 57), df, 57)
    print(root.descendants())
    # this sum will be equal to the cost that was passed at the root
    print(sum(root.leaves()))

