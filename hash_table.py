from typing import Any, Optional

class Node:
    def __init__(self, key: int, value: Any) -> None:
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size: int) -> None:
        self.size = size
        self.table = [None]*size
    
    #def _hash_function(self, key: int) -> int: return hash(key)%self.size
    
    def _hash_function(self, key: int) -> int:
        if isinstance(key,str):
            return sum(ord(c) for c in key)%self.size
        elif isinstance(key,int):
            return key%self.size
        else:
            raise TypeError("Invalid key input !")
    
    def insert(self, key: int, value: Any) -> None:
        index: int = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            node: Any = self.table[index]
            while node.next:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key,value)

    def get(self, key: int) -> Optional[Any]:
        index: int = self._hash_function(key)
        node: Any = self.table[index]
        while Node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key: int) -> None:
        index: int = self._hash_function(key)
        node: Any = self.table[index]
        prev: Any = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                return
            prev = node
            node = node.next
    
    def display(self) -> None:
        for index, node in enumerate(self.table):
            print(f"Bucket {index}: ",end="")
            while node:
                print(f'({node.key}, {node.value})->',end ="")
                node = node.next
            print(None)
           

if __name__ == "__main__":

    hash_table = HashTable(10)
    hash_table.insert("apple",5)
    hash_table.insert("banana",7)
    hash_table.insert("orange",3)
    

    hash_table.display()

    print(hash_table.get("banana"))
    
        
    