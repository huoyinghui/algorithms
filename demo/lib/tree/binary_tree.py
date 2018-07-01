class BinTreeNode(object):
    def __init__(self, data=None, left=None, right=None, is_root=False):
        self.data = data
        self.left = left
        self.right = right
        self.is_root = is_root

    def root(self):
        return self.is_root


class BinTree(object):
    def __init__(self, root=None):
        self.root = root
    
    @classmethod
    def build_from(cls, node_list):
        node_dict = {}
        root = None

        for node_data in node_list:
            data = node_data.get('data', None)
            node_dict[data] = BinTreeNode(data)
        
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                print('find root node:', node)
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)
    
    def trav(self):
        """
        先(根)序遍历: 先处理根，之后是左子树，然后是右子树
        中(根)序遍历: 先处理左子树，之后是根，最后是右子树
        后(根)序遍历: 先处理左子树，之后是右子树，最后是根
        """
        pass
    def pre_order_trav(self, subtree):
        if subtree is None:
            return 
        print(subtree.data)
        self.pre_order_trav(subtree.left)
        self.pre_order_trav(subtree.right)

    def mid_order_trav(self, subtree):
        if subtree is None:
            return 
        self.mid_order_trav(subtree.left)
        print(subtree.data)
        self.mid_order_trav(subtree.right)

    def after_order_trav(self, subtree):
        if subtree is None:
            return 
        self.after_order_trav(subtree.left)
        self.after_order_trav(subtree.right)
        print(subtree.data)

    def reverse(self, subtree):
        """
        递归交换左右节点
        """

        if subtree is not None:
            return
        
        subtree.left, subtree.right = subtree.right, subtree.left
        # 递归左子树
        self.reverse(subtree.left)
        # 递归右子树
        self.reverse(subtree.right)

node_list = [
    {'data':'A', 'left':'B', 'right':'C', 'is_root':True},
    {'data':'B', 'left':'D', 'right':'E', 'is_root':False},
    {'data':'C', 'left':'F', 'right':'G', 'is_root':False},
    {'data':'D', 'left':None, 'right':None, 'is_root':False},
    {'data':'E', 'left':'H', 'right':None, 'is_root':False},
    {'data':'F', 'left':None, 'right':None, 'is_root':False},
    {'data':'G', 'left':'I', 'right':'J', 'is_root':False},
    {'data':'H', 'left':None, 'right':None, 'is_root':False},
    {'data':'I', 'left':None, 'right':None, 'is_root':False},
    {'data':'J', 'left':None, 'right':None, 'is_root':False},
]


def test_tree():
    t = BinTree.build_from(node_list)
    print(t)

    print('root-left-right:\n')
    t.pre_order_trav(t.root)
    print('left-root-right:\n')
    t.mid_order_trav(t.root)
    print('left-right-root:\n')
    t.after_order_trav(t.root)
    assert 1

def main():
    pass

if __name__ == '__main__':
    main()
    
