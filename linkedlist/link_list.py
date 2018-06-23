class Node(object):
    """
    单个节点元素
    """
    def __init__(self, value=None, pre=None, nextnode=None):
        self.value = value
        self.nextnode = nextnode
        self.pre = pre


class LinkedList(object):
    def __init__(self, maxsize=20):
        self.maxsize = maxsize
        self.root = Node(value='root')
        self.length = 0
        self.tailnode = None
    
    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('linklist full')

        node = Node(value=value, nextnode=None)

        tailnode = self.tailnode or self.root
        node.nextnode = tailnode.nextnode
        node.pre = tailnode
        tailnode.nextnode = node
        
        
        self.tailnode = node
        self.length += 1

    def append_left(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('linklist full')

        node = Node(value=value, nextnode=None)
        header = self.root
        node.nextnode = header.nextnode
        header.nextnode = node
        self.length += 1

    def iter_node(self):
        curnode = self.root.nextnode

        while curnode:
            yield curnode
            curnode = curnode.nextnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    
    def remove(self, value):
        """
        curP: next = cur.next
        cur
        curN: pre = cur.pre
        """
        # 首尾需要考虑
        curP = self.root
        for node in self.iter_node():
            curN = node.nextnode
            if node.value == value:
                curP.nextnode = node.nextnode
                curN.pre = node.pre
                self.length -= 1
            else:
                curP = node

    def find(self, value):
        index = 0
        for node in self.iter_node():
            index += 1
            if node.value == value:
                return index

    def pop(self):
        if len(self) <= 0:
            raise Exception('link empty')
            # return None

        value = self.tailnode.value
        print('v:', self.tailnode.value, 'pre', self.tailnode.pre)
        tailnode_pre = self.tailnode.pre
        if not tailnode_pre:
            return None
        tailnode_pre.nextnode = None
        self.tailnode = tailnode_pre
        self.length -= 1
        return value

    def pop_left(self):
        header = self.root
        node = header.nextnode
        if not node:
            return None

        value = node.value
        node_next = node.nextnode
        if node_next:
            node_next.pre = header

        header.nextnode = node_next
        self.length -= 1 
        return value


    def empty(self):
        return len(self) == 0

    def clear(self):
        pass

def test_link_list():
    lk = LinkedList()
    lk.append(20)
    lk.append(30)
    lk.append(40)
    lk.append(50)
    lk.append(60)
    lk.append_left(10)
    lk.append(70)
    assert len(lk) == 7
    lk.remove(50)
    assert len(lk) == 6
    lk.append_left(1)
    lk.append_left(0)
    assert len(lk) == 8
    for item in lk:
        print(item)

    index = lk.find(70)
    assert index == 8
    index = lk.find(1)
    assert index == 2

    # item = lk.pop()
    # assert item == 70
    # assert len(lk) == 7

    for _ in range(len(lk)):
        value = lk.pop_left()
        # value = lk.pop()
        print('pop_left:', value, 'len:', len(lk))

    assert lk.empty() == True

    for i in range(3):
        lk.append_left(i)


    assert len(lk) == 3
    for item in lk:
        print(item)

    for _ in range(len(lk)):
        value = lk.pop()
        print('pop :', value, len(lk))


if __name__ == '__main__':
    test_link_list()