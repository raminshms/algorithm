class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def print_list(self):
        temp = self
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()


def reverse(head: ListNode):
    previous, current, next = None, head, None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def test():
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(10)

    head.print_list()

    res = reverse(head)
    res.print_list()


test()
