# Madi Augustine
# DS5010
# ICE Week 3 In Class Exercise 


class Node: 
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
    def count(self):
        print("in the node that stores", self.data)
        if self.next is None: 
            print('hit base case')
            return 1
        else:
            print("recursive call! calling count with the node storing", self.next)
            return 1 +self.next.count()

    def calculate_price(self):
        return int(self.data.price)