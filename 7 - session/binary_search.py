numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
second_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
third_numbers = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
# target = 4
# target = 5
target = 17


def binary_search(numbers, target):
    left = 0 # left pointer
    right = len(numbers) - 1 # right pointer

    while left <= right:
        midpoint = (left + right) // 2

        # print(f'Midpoint: {midpoint}')
        # print(f'value of midpoint: {numbers[midpoint]}')

        if numbers[midpoint] == target:
            # print("Target found: ", target)
            # print(f'Target: {target} found')
            print(f'Target: {target} found at index {midpoint}')
            return midpoint
        elif numbers[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1

    print(f'Target: {target} not found')
    return None




        
    

binary_search(third_numbers, target)





