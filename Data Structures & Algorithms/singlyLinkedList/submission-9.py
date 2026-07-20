class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node

        if self.tail == self.head:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        prev = self.head
        i = 0
        while prev.next:
            if i == index:
                to_remove = prev.next
                prev.next = to_remove.next

                if to_remove == self.tail:
                    self.tail = prev
                return True
            prev = prev.next
            i += 1
        return False
    def getValues(self) -> List[int]:
        values = []
        node = self.head.next
        
        while node:
            values.append(node.val)
            node = node.next
        return values