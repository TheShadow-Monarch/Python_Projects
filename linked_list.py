from typing import Any, Optional, NoReturn

class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def middle(self) -> Optional[Any]:
        slow: Any = self.head
        fast: Any = self.head

        if self.head is not None:
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
        return slow.data if slow else None
    
    def print_list(self) -> None:
        current: Any = self.head
        while current:
            print(current.data,end = "->")
            current = current.next
        print("None")
    
    def append(self, data) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self,data) -> None:
        new_node: Any = Node(data)
        new_node.next, self.head = self.head, new_node

    def delete(self,data) -> None:
        if self.head is None:
            return
        if self.head.data == data :
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next    

    def is_cycle(self) -> bool:
        tortoise: Any = self.head
        hare: Any = self.head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False
    
    def find_cycle_start(self) -> Optional[Any]:
        tortoise: Any = self.head
        hare: Any = self.head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                break
        
        tortoise = self.head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        
        return hare

if __name__ == "__main__":
    pass