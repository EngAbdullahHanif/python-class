# Exercise: Finding the Missing Number

# Problem Statement:
# You are given an array of integers from 1 to n, with one number missing. Write a Python function to find and return the missing number.

my_array = [1, 2, 3, 4, 5, 6, 8, 9, 10]

def find_missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)


print(find_missing_number(my_array))


#  You are a teacher at a high school, and you have recently conducted an exam for a class of students. Each student's exam grade is represented by a tuple (student_name, score), where student_name is a string representing the student's name, and score is an integer representing the exam score (out of 100). Your task is to sort the students' exam grades based on their scores in ascending order. If two or more students have the same score, they should be sorted alphabetically by their names. Write a Python function to solve this problem.


students = [("Alice", 75), ("Bob", 90), ("Carol", 85), ("David", 85), ("Eve", 75)]

