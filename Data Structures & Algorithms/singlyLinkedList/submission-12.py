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
            i+=1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node

        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        prev = self.head
        while i< index and prev.next:
            i += 1
            prev = prev.next
        if prev and prev.next:
            if prev.next == self.tail:
                self.tail = prev
            prev.next = prev.next.next
            return True
        return False
    def getValues(self) -> List[int]:
        values = []
        node = self.head.next
        
        while node:
            values.append(node.val)
            node = node.next
        return values