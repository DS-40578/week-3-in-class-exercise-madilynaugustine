# Madi Augustine
# DS5010
# ICE Week 3 In Class Exercise 

from Node import Node 
from Book import Book

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node 

    def __str__(self):
        return_str =""
        current = self.head 
        while current is not None:
            return_str += str(current) + " "
            current = current.next
        return return_str
    
    def find(self, target_value):
        current = self.head 
        while current is not None:
            if current.data == target_value:
                return current
            current = current.next
        return None

    """
    ICE Part 1: #1
    to_list
    Goal: Return a list of all data attributes from each object 
    Written in class and with others in class
    """
    def to_list(self): 
        current_list = [ ]
        current = self.head 
        while current is not None:
            current_list.append(current.data)
            current = current.next 
        return (current_list)
    """
    ICE Part 1: #3
    find_last_index
    Goal: Returns the index of the lowest occurance of the target value 
    Written in class and with others in class
    """
    def find_last_index(self, target):
        current = self.head
        index_needed = -1
        index_start = 0
        while current is not None:
            if current.data == target:
                index_needed = index_start
            current = current.next
            index_start += 1
        return index_needed
    
    def count(self):
        return self.head.count()
    
    def iterative_count(self):
        current_list = self.head
        current = 0
        while current is not None:
            counter += 1 
            current = current.next
            return counter 

    """
    ICE: Modified slightly from class, since mine was not working
    Used the same idea as the iterative counter above 
    """
    def calculate_price(self):
        book_cost = 0
        current = self.head
        while current is not None:
            book_cost += current.calculate_price()
            current = current.next
        return book_cost 
        
    
    def iterative_filter(self, predicate):
        """
        Parameter-predicate: lambda that takes in a Node object and returns True/False 
        """
        current = self.head
        new_ll = LinkedList()
        while current is not None: 
            if predicate(current) == True:
                new_ll.add_to_front(current.data)
            current = current.next
        return new_ll
    
        
    def add(self, data, next):
        new_node = Node(data, next)
        self.head = new_node

    def __str__(self):
        books = []
        current = self.head
        while current is not None:
            books.append(str(current.data))
            current = current.next
        return ", ".join(books)

ll = LinkedList()
ll.add_to_front("D")
ll.add_to_front("A")
ll.add_to_front("B")
ll.add_to_front("A")
# testing to make sure ICE Part 1 #1 works correctly 
list_representation = ll.to_list()
print(list_representation) 

#testing to make sure ICE Part 1 #3 works correctly
print(ll.find_last_index("A")) #expected value is 2, which is correctly identified 


print(ll.count())

#You can not test both Book and Part 1 and Part 2 of the ICE at the same time 
#Comment this in and the above out to demonstrate that book works too 
# ll.add_to_front(Book("Lake of Souls", False))
# ll.add_to_front(Book("Intro to Python", True))
# ll.add_to_front(Book("Data Science in Python", False))
# ll.add_to_front(Book("Linear Algebra for Dummies", True))
# ll.add_to_front(Book("Into the Heart of the Sea", False))
# ll.add_to_front(Book("Destroy All Humans", True))

# print(ll.calculate_price())

# paperback = lambda node:True if node.data.is_paperback else False 

# new_ll = ll.iterative_filter(paperback)

# print(new_ll)

