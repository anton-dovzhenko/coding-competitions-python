class Node:

    def __init__(self, v):
        self.v = v
        self.next = None
        self.prev = None

    def __repr__(self):
        return 'Node (%s)' % self.v


class Solution:

    def findTheWinner(self, n, k):
        head = Node(1)
        p = head
        for i in range(2, n + 1):
            node = Node(i)
            node.prev = p
            p.next = node
            p = node
        head.prev = p
        p.next = head

        while head.next is not None:
            for i in range(k - 1):
                head = head.next

            p = head.prev
            n = head.next
            if p is not None and n != p:
                p.next = n
                n.prev = p
                head = n
            else:
                return n.v


print(Solution().findTheWinner(5, 2))
print(Solution().findTheWinner(6, 5))



