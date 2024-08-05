class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def middleNode(head: ListNode):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
