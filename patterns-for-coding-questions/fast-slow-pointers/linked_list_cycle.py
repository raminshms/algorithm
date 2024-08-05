class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def hasCycle(head: ListNode):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
