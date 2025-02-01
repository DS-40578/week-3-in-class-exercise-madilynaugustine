# Madi Augustine
# DS5010
# ICE Week 3 In Class Exercise 

from Node import Node 

"""
ICE Part 4: More time getting used to linked chains
find_loop
Goal: Returns true or false depending on if there is a loop within the linked chain 
(true if loop, otherwise false)
Referenced the "Floyd Cycle Finding Algorithm"
https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/
Algorithm states there is a fast pointer and a slow pointer
Fast pointer needs to move quicker than the slow, if they catch each other a loop exists, 
if it never catached and it reaches none, there is no loop  
Dr. Domino reviewed this with me too
"""

def find_loop(node):
    slow_pointer = node
    fast_pointer = node  
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True #since they caught each other the loop exists   
    return False #fast_pointer reached the end, so the loop does not exist 

#no loop testing
tail_good = Node("D", None)
m1_good = Node("A", tail_good)
m2_good = Node("B", m1_good)
head_good = Node("A", m2_good)

#loop testing
tail_bad = Node("D", None)
m1_bad = Node("A", tail_bad)
m2_bad = Node("B", m1_bad)
head_bad = Node("C", m2_bad)
tail_bad.next= head_bad

#print statements showing the function works correctly 
x = find_loop(m2_good)
print(x)
y= find_loop(m2_bad)
print (y)