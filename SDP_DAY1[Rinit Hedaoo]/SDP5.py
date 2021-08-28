# YESHWANTRAO CHAVAN COLLEGE OF ENGINNERING (YCCE)
# ELECTRONICS BRANCH
# REGISTRATION NO. 19010674
# YEAR: 3rd, SEMESTER: 5th
# SECTION A, ROLL NO. 69
# NAME: RINIT HEDAOO
# SDP SESSION DAY 1
# DATE: 28/08/2021

# Q5) Write a program to calculate gross salary from basic sal(HRA=30%, TA=40%, DA=20%)

Basic_Salary = int (input("Enter Basic Salary: "))

DA = (Basic_Salary * 20) / 100
HRA = (Basic_Salary * 30) / 100
TA = (Basic_Salary * 40) / 100
Gross_Salary = Basic_Salary + DA + HRA + TA

print ("\n\nDearness Allowance 40% of Basic Salary: " , DA)
print ("\nHouse Rent 20% of Basic Salary: " , HRA)
print ("\nTravel Allowance 20% of Basic Salary: " , TA)
print ("\nGross Salary :" , Gross_Salary)