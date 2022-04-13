class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    
    def reverse(self):
        temp = self.head
        self.head = self.tail 
        self.tail = temp
        before = None 
        after = temp.next

        for _ in range(self.length):
            after =  temp.next 
            temp.next = before
            before = temp 
            temp = after 


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


print('*'*100)
my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)

my_ll.print_list()

print('reverse')
my_ll.reverse()
my_ll.print_list()