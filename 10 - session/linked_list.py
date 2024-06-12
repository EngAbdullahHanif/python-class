class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None



class SinglyLinkedList:

    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if not None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        






my_linkedlist = SinglyLinkedList()
my_linkedlist.append(5)  
my_linkedlist.append(8)   



















class SinglyLinkedList:
    # head: pointer to the first node
    # append: add a new node to the end of the list
    # print_list: print all the nodes in the list

    def __init__(self):
        self.head = None



    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
sll = SinglyLinkedList()
# sll.append(1)
# sll.append(2)
# sll.append(3)
# sll.print_list()  # Output: 1 -> 2 -> 3 -> None







class PageNode:
    def __init__(self, url):
        self.url = url 
        self.prev = None
        self.next = None

# my_prev = 4
# current = 5
# my_next = 6

# print(my_prev) # 4
# print(current) # 5
# print(current) # 6
       
class BrowserHistory:

    def __init__(self):
        self.head = None
        self.current = None # tail or end

    def visit(self, url):
        new_page = PageNode(url) # Z

        if not self.head:
            self.head = new_page
            self.current = new_page
            print(f"Visited: {self.current.url}")
            return
        
        self.current.next = new_page
        new_page.prev = self.current
        self.current = new_page
        print(f"Visited: {self.current.url}")
            

    def back(self):
        if self.current.prev:
            self.current = self.current.prev
            print(f"Back to: {self.current.url}")
        else:
            print("No back history available")

    def forward(self):
        if self.current.next:
            self.current = self.current.next
            print(f"Forward to: {self.current.url}")
        else:
            print("No forward history available")

# Example usage
browser = BrowserHistory()
browser.visit("google.com")
browser.visit("github.com")
browser.visit("stackoverflow.com")
browser.back()  # Output: Back to: github.com
browser.back()  # Output: Back to: google.com
browser.forward()  # Output: Forward to: github.com
browser.forward()  # Output: Forward to: stackoverflow.com



# x = 5 
# my_array = [1, 2, 3, 4, 5]
# my_object = {
#     "name": "John",
#     "age": 30
# }

# my_stack = []
# my_stack.append(1)

# my_queue = []
# my_queue.append(1)

# my_linkedlist = SinglyLinkedList()
# my_linkedlist.append(1)

# my_double_linkedlist = DoublyLinkedList()
# my_double_linkedlist.append(1)
