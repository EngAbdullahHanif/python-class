

# Problem: Valid Parentheses
# Problem: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

my_string = '()'
my_string = '[]'
my_string = '{]'


my_string = '([)]'
my_string = '{[]}'


first_condition = '()'
second_condition = '[]'
third_condition = '{}'

# if my_string == first_condition or my_string == second_condition or my_string == third_condition:
#     print('True')
# else:
#     print('False')

# my_string = '{]'
# my_string = 'sdjf'
# my_string = '){}[][]{[}]'

# my_name = {'name': 'Hanif'}

my_string = '()'
my_string = ')('

my_stack = []
my_dict = {'(': ')', '[': ']', '{': '}'}

for char in my_string:
    if char in my_dict.keys():
        print("opening bracket added")
        my_stack.append(char)
    elif char in my_dict.values():
        if len(my_stack) == 0:
            print('False, empty stack')
            break
        else:
            last_open = my_stack.pop() # '('    
            # if '('
            if my_dict[last_open] == char:
                print('True, it is valid')
                break


keys = ['(', '[', '{']
values = [')', ']', '}']















# Stack
# stack functions:
# push
# pop
# peek
# isEmpty
# size

# my_array = []
# my_array.append('a')
# my_array.append('b')
# my_array.append('c')

# print(my_array)
# print('length of my_array: ', len(my_array))

# stack.pop()




class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()
    
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        # if len(self.stack) == 0:
        #     return True
        # else:
        #     return False

        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

    



stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')

# print("stack.pop(): ", stack.pop())
# print("stack.peek(): ", stack.peek())

# stack.pop()
# stack.peek()
# print(stack.isEmpty())
# print(stack.size())




# Queue
# queue functions:
# enqueue
# dequeue
# peek
# isEmpty
# size

class Queue():
    def dequeue(self):
        if self.isEmpty():
            return None
        # return self.items[0].pop()
        return self.items.pop(0)

    
    # def enqueue(self, item):
    #     self.queue.append(item)

    # def dequeue(self):
        #     if self.is_empty():

        #         return "Q is empty"

        #         return Self.queue.dequeue()

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            # return self.queue.pop(0)
            return self.queue[0].pop()

    pass

my_queue = [1, 2, 3, 4, 5, 7]


