# YESHWANTRAO CHAVAN COLLEGE OF ENGINNERING (YCCE)
# ELECTRONICS BRANCH
# REGISTRATION NO. 19010674
# YEAR: 3rd, SEMESTER: 5th
# SECTION A, ROLL NO. 69
# NAME: RINIT HEDAOO
# SDP SESSION DAY 1
# DATE: 28/08/2021

# Q9) Write a program to reverse a three number 123 = 321

number = int(input("Enter the integer number: "))   
revs_number = 0  
  
while (number > 0):  
   remainder = number % 10  
   revs_number = (revs_number * 10) + remainder  
   number = number // 10  
  
  
print("The reverse number is : {}".format(revs_number))  