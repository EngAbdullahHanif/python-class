unsorted_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# divide the nubmers into two lists
list1 = unsorted_numbers[0:5]
list2 = unsorted_numbers[5:11]
# or
list1 = unsorted_numbers[:len(unsorted_numbers)//2]
list2 = unsorted_numbers - list1


items = [8, 7]

if items[1] < items[0]:
    items[0], items[1] = items[1], items[0]

if items[1] > items[0]:
    items[0], items[2] = list2[0], list2[0]


