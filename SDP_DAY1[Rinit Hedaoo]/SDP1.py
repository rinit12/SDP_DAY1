# YESHWANTRAO CHAVAN COLLEGE OF ENGINNERING (YCCE)
# ELECTRONICS BRANCH
# REGISTRATION NO. 19010674
# YEAR: 3rd, SEMESTER: 5th
# SECTION A, ROLL NO. 69
# NAME: RINIT HEDAOO
# SDP SESSION DAY 1
# DATE: 28/08/2021

# Q1) Write A program to Add, Multiply, Divide, Subtract basically a simple calculator.

def add(P, Q):    
   return P + Q   

def subtract(P, Q):   
   return P - Q   

def multiply(P, Q):   
   return P * Q

def divide(P, Q):   
   return P / Q    

print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
choice = input("Please enter choice (a/ b/ c/ d): ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if choice == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif choice == 'b':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif choice == 'c':    
   print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))    

elif choice == 'd':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))    

else:    
   print ("Invalid input") 