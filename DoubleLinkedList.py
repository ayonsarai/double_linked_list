#Sarai Ayon 
#4/16/2024
#CS240 Data Structures HW 1: Linked Lists
#Double Linked List 

from typing import List
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = Node(data)
            node.next = new_node
            new_node.prev = node

file_path = r"C:\Users\Sarai Ayon\OneDrive - Whatcom Community College\Spring 2024\CS240 Database Structure & Algorithms\Week 2 Linked List\numbers-2.txt"

linked_list = DoublyLinkedList()

with open(file_path, 'r') as f:
    for num in f.read().split():
        linked_list.append(int(num))
