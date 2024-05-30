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
sll.append(1)
sll.append(2)
sll.append(3)
sll.print_list()  # Output: 1 -> 2 -> 3 -> None







# class PageNode:
#     def __init__(self, url):
#         self.url = url
#         self.next = None
#         self.prev = None

# class BrowserHistory:
#     def __init__(self):
#         self.current = None

#     def visit(self, url):
#         new_page = PageNode(url)
#         if self.current:
#             self.current.next = new_page
#             new_page.prev = self.current
#         self.current = new_page

#     def back(self):
#         if self.current and self.current.prev:
#             self.current = self.current.prev
#             print(f"Back to: {self.current.url}")

#     def forward(self):
#         if self.current and self.current.next:
#             self.current = self.current.next
#             print(f"Forward to: {self.current.url}")

# # Example usage
# browser = BrowserHistory()
# browser.visit("google.com")
# browser.visit("github.com")
# browser.visit("stackoverflow.com")
# browser.back()  # Output: Back to: github.com
# browser.back()  # Output: Back to: google.com
# browser.forward()  # Output: Forward to: github.com
