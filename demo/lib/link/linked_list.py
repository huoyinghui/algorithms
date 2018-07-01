class Node(object):
    def __init__(self, next=None, value=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return '<Node: value:{}, next={}>'.format(self.value, self.next)



class LinkedList(object):
    """
    [root] -> [node0] -> [node1] -> None
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def head(self):
        return self.root

    def tail(self):
        return self.tailnode

    def append(self, value):
        self.check()

        n = Node(value=value)
        tailnode = self.tail()

        if tailnode is None:
        # 第一次
            head = self.head()
            head.next = n
        else:
            tailnode.next = n

        self.tailnode = n
        self.length += 1

    def check(self):
        if self.maxsize is not None and len(self) < self.maxsize:
            raise Exception('full linklist')

    def check_len(self):
        if len(self) < 1:
            raise Exception('empty linklist')

    def append_left(self, value):
        self.check()
        n = Node(value=value)
        head = self.head()

        n.next = head.next
        head.next = n
        self.length += 1

    def iter_node(self):
        self.check_len()

        cur = self.head().next
        tail_node = self.tail()
        while cur is not tail_node:
            yield cur
            cur = cur.next
        yield tail_node
        

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def pop(self):
        if len(self) < 1:
            raise Exception('empty linklist')

        tail = self.tail()
        value = tail.value

        cur = self.head().next
        while cur is not None and cur.next is not tail:
            cur = cur.next

        self.tailnode = cur
        self.length -= 1
        if self.length == 0:
            self.tailnode = None
        return value

    def pop_left(self):
        self.check_len()

        head = self.head()
        cur = head.next
        value = cur.value
        head.next = cur.next
        self.length -= 1
        if self.length == 0:
           self.tailnode = None

        return value
    
    def find(self, value):
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            else:
                index += 1
    
    def find_right_index(self, index):
        """
        3.求链表倒数第k个节点
        题目描述：输入一个单向链表，输出该链表中倒数第k个节点，链表的倒数第0个节点为链表的尾指针。

        分析：设置两个指针 p1、p2，
        首先:p1 和 p2 都指向 head，
        然后:p2 向前走 k 步，这样 p1 和 p2 之间就间隔 k 个节点，
        最后:p1 和 p2 同时向前移动，直至 p2 走到链表末尾。
        """
        if index >= len(self):
            raise Exception('index err')

        cur = self.head().next
        target = cur

        # target:0 
        # cur:k
        while index > 0 and cur:
            index -= 1
            cur = cur.next
        
        while cur and cur is not self.tailnode:
            # print('index-r:', cur)
            cur = cur.next
            target = target.next

        return target

    def find_mid(self):
        """
        4. 求链表的中间节点
        题目描述：求链表的中间节点，如果链表的长度为偶数，返回中间两个节点的任意一个，若为奇数，则返回中间节点。

        分析：此题的解决思路和第3题「求链表的倒数第 k 个节点」很相似。
        可以先求链表的长度，然后计算出中间节点所在链表顺序的位置。
        但是如果要求只能扫描一遍链表，如何解决呢？
        最高效的解法和第3题一样，通过两个指针来完成。
        用两个指针从链表头节点开始，一个指针每次向后移动两步，一个每次移动一步，
        直到快指针移到到尾节点，那么慢指针即是所求。
        """

        cur = self.head().next
        target = cur

        while cur and cur is not self.tailnode and cur.next is not None:
            cur = cur.next.next
            target = target.next
        
        return target

    def find_circle(self):
        """
        5.题目描述：输入一个单向链表，判断链表是否有环？
        """
        cur = self.head().next
        slow = cur
        while cur and cur.next is not None:
            cur = cur.next.next
            slow = slow.next

            if cur == slow:
                circle_node = cur 
                # 直接打印，由于出现了环，导致递归打印, 递归深度限制 
                print('circle_node_value:', circle_node.value)
                return True
        
        return False

    def clear(self):
        for node in self.iter_node():
            # print('clear:', node)
            node = None
            self.length -= 1
        self.head().next = None
        self.tailnode = None

    def reverse(self):
        head = self.head()
        cur = head.next
        pre_node = None
        next_node = None

        while cur:
            print('reverse:', cur)
            cur = cur.next
            # cur 
            
        return None

def isIntersec(h1: Node, h2: Node):
    # print('----\n', h1, '===\n', h2)
    if (h1 or h2) is None:
        return False

    while h1 and h1.next is not None:
        h1 = h1.next

    while h2 and h2.next is not None:
        h2 = h2.next

    # 殊途同归
    if h2 == h1:
        return True
    return False


def test_isIntersec():
    l1 = LinkedList()
    l2 = LinkedList()

    l1.append(1)
    l1.append(2)
    l1.append(3)

    mid_node = l1.find_mid()

    l2.append('l2:1')
    l2.tailnode.next = mid_node
    
    assert True == isIntersec(l1.head().next, l2.head().next)


# def test_linked_list():
#     ll = LinkedList()
#     ll.append(0)
#     ll.append(1)
#     ll.append(2)

#     assert 2 == ll.find(2)
#     assert len(ll) == 3
#     assert ll.tail().value == 2

#     ll.append_left(-1)
#     assert len(ll) == 4

#     assert 2 == ll.pop()
#     assert 1 == ll.pop()
#     assert 0 == ll.pop()
#     assert -1 == ll.pop()

#     assert len(ll) == 0

#     ll.append(10)
#     ll.append_left(-2)

#     for i in ll:
#         print('\ni:', i)

#     assert -2 == ll.pop_left()
#     assert 10 == ll.pop_left()
#     assert 0 == len(ll)
#     # import pytest

#     ll.append(22)
#     ll.clear()
#     # for i in ll:
#     #     print('\n22:', i)
#     assert len(ll) == 0

#     ll.append(10)
#     ll.append(20)
#     ll.append(30)

#     assert len(ll) == 3
#     assert list(ll) == [10, 20, 30]
#     re_ll = list(ll)
#     re_ll.reverse()
#     # print('re_ll:', re_ll)
#     # assert ll.reverse() == re_ll

#     # 3.求链表倒数第k个节点
#     right_index_node = ll.find_right_index(0)
#     assert right_index_node == ll.tail()
#     assert ll.find_right_index(0).value == 30
#     assert ll.find_right_index(1).value == 20
#     assert ll.find_right_index(2).value == 10

#     # 4.求链表的中间节点
#     index_mid = len(ll)//2
#     print('index_mid', index_mid, ll.find_right_index(index_mid))
#     mid_node = ll.find_mid()
#     print('mid_node', mid_node)
#     ll.append(40)
#     ll.append(50)
#     assert list(ll) == [10, 20, 30, 40, 50]
#     print('mid_node', ll.find_mid())

#     # 5. 判断单链表是否存在环
#     ll.tailnode.next = ll.head().next
#     assert True == ll.find_circle()



if __name__ == '__main__':
    test_isIntersec()
