import numpy as np
import random

# ROWS - each student(student0,student1,student2,student3)
# COLS - each test(test0,test1,test2)
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

student1 = grades[1]

student0_test1 = grades[0,1]

# : quential value? upper bound is not included
students0_1 = grades[0:2]

students1and3 = grades[[1,3]]

# to select students 1 and 3 but only test2
students1and3_test2 = grades[[1,3],2]

all_students_test0 = grades[:,0]

all_students_test1_2 = grades[:,1:3]

all_students_test0and2 = grades[:,[0,2]]


# Exercise
# Array of 12 random grades in the range 60-100, than reshape the result into a 3 by 4 array
# culculate result

grades = np.random.randint(60,101,12).reshape(3,4)

grades.mean()

# average by col
grades.mean(axis=0)

# average by row
grades.mean(axis=1)

numbers = np.arange(1,6)
# shallow copy
numbers_view = numbers.view()

numbers[1] *= 10
numbers_view[1] /= 10

numbers_slice = numbers[0:3]
numbers[1] *= 20

# DEEP COPIES
numbers_copy = numbers.copy()
numbers[1] *= 10

grades = np.array([[87, 96, 70], [100, 87, 90]])

#reshape method produces a shallow copy
grades_reshaped = grades.reshape(1,6)

grades.resize(1,6)

# Flatten creates a deep copy
flattended = grades.flatten()

# Ravel creates a shallow copy
reveled = grades.ravel()

reveled[0] = 100

flattended[1] = 100

grades = np.array([[87, 96, 70], [100, 87, 90]])

grades.T

grades2 = np.array([[94, 77, 90],[100, 81, 82]])

h_grades = np.hstack((grades, grades2))
v_grades = np.vstack((grades, grades2))

print()