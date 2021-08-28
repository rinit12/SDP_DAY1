# YESHWANTRAO CHAVAN COLLEGE OF ENGINNERING (YCCE)
# ELECTRONICS BRANCH
# REGISTRATION NO. 19010674
# YEAR: 3rd, SEMESTER: 5th
# SECTION A, ROLL NO. 69
# NAME: RINIT HEDAOO
# SDP SESSION DAY 1
# DATE: 28/08/2021

# Q8) Write a program to convert height from feet & inches to centimeters

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
 
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
 
print("Your height is : %d cm." % h_cm)