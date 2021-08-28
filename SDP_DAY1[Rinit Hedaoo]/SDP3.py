# YESHWANTRAO CHAVAN COLLEGE OF ENGINNERING (YCCE)
# ELECTRONICS BRANCH
# REGISTRATION NO. 19010674
# YEAR: 3rd, SEMESTER: 5th
# SECTION A, ROLL NO. 69
# NAME: RINIT HEDAOO
# SDP SESSION DAY 1
# DATE: 28/08/2021

# Q3) Write a program for swapping two numbers using third variable.

print("Enter values of A & B.....")
A = int (input("Enter value of A:"))
B = int (input("Enter value of B:"))

temp = A
A = B   
B = temp

print("The value of A after swapping: {}".format(A))
print("The value of B after swapping: {}".format(B))