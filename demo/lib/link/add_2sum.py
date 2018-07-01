from linked_list import Node, LinkedList


def add2sum(left: Node, right: Node) -> Node:
    head = Node(0)
    cur = head
    sum = 0

    while left or right:
        sum //= 10
        if left:
            sum += left.value
            left = left.next
        
        if right:
            sum += right.value
            right = right.next

        cur.next = Node(sum % 10)
        cur = cur.next

    if sum // 10 == 1:
        cur.next = Node(1)
    
    return head.next

    
def main():
    pass

if __name__ == '__main__':
     main()
    