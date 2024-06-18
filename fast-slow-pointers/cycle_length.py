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
            return calculateCycleLength(slow)

    return False


def calculateCycleLength(head: ListNode):
    current = head
    length = 0

    while True:
        current = current.next
        length += 1
        if current == head:
            break

    return length
