class Node:
    def __init__(self, val, n=None):
        self.next = n
        self.val = val
        

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i=0
        current = self.head
        while current and i<=index:
            if not current:
                return -1
            
            if i==index:
                return current.val
            
            current = current.next
            i+=1
            
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        prev = None
        current = self.head
        while current:
            prev, current = current, current.next
            
        if prev:
            prev.next = node
        else:
            self.head = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        i=0
        current = self.head
        while current and i<index:
            if not current:
                return current
            
            if i==index-1:
                node = Node(val, current.next)
                current.next = node
                
            
            current = current.next
            i+=1
            
        if index==0:
            self.addAtHead(val)
        

    def deleteAtIndex(self, index: int) -> None:
        i=0
        prev = None
        current = self.head
        while current and i<index:
            if not current:
                return current
            
            if i==index-1:
                n = current.next
                if n:
                    current.next = n.next
            
            current = current.next
            i+=1
            
        if index==0:
            if self.head:
                self.head = self.head.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)