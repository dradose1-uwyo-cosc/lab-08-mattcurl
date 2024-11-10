# Matthew Curl
# UWYO COSC 1010
# 11/10/2024
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to: Googled "How to count instances of a value in a string in python" 
# Got: https://www.simplilearn.com/tutorials/python-tutorial/count-in-python#:~:text=If%20you%20have%20a%20large,a%20list%20or%20a%20tuple. 
# Googled "Value Error Handling"
# Got: https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples
# Braeden Kirby


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
# create a function that will try to convert to int
def Convert_num(string):
    try:
        int_num = int(string)
        return int_num
    # if not then split the float and check for negative
    except ValueError:
        num_for_check = string.split(".")
        isNeg = False
        if "-" in string:
            isNeg = True
            string = string.replace("-","")
            #check if float is float and convert it
        if "." in string and (num.isdigit() for num in num_for_check) and len(num_for_check) == 2:
            if isNeg == True:
                f_num = -1*float(string)
                return f_num
            else:
                f_num = float(string)
                return f_num
            #make int if neg too
        elif (num.isdigit() for num in num_for_check) and isNeg == True:
            int_num = -1 * int(string)
            return int_num
        else:
            
            return False
    # call it in a while loop to check it
while True:
    string = input("Please input a number to convert to an int or float:(say exit to exit)")
    if string.lower() == "exit":
        break
    converted = Convert_num(string)
    if converted == False:
        print (f"Your converted number is Invalid. Please try again.")
    else:
        print (f"Your converted number is {converted}")
        
   

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
# set up function and convert to numbers
def y_list(m,b,x1,x2):
    n_m = Convert_num(m)
    n_b = Convert_num(b)
    n_x1 = Convert_num(x1)
    n_x2 = Convert_num(x2)
    y_vals = []
    # check all values
    if n_m == False or n_b == False or n_x1 == False or n_x2 == False:
        return False
    if n_x1 > n_x2:
        return False
    if ("." not in x1) and ("." not in x2):
        # run calculation if conditions are satisfied
        for x in range(n_x1, n_x2 + 1):
            y = n_m * x + n_b
            y_vals.append(y)
        
        return y_vals


    else: 
        return False
    # call in a input to give the user the values
while True: 
    string = input("Please input m , b , lower x and upper x with a space in between each value(with the later two being integers)(say exit to exit)")
    if string.lower() == "exit":
        break
    m, b, x1, x2 = string.split()
    
    list = y_list(m , b, x1, x2)
    if list == False:
        print("Your inputs are not correct. Try again.")
    else:
        print(f"Your list from {x1} to {x2} has the y values of {list}")

    

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
    # make a square root func
def sqr_root(x):
    if x < 0:
        return None
    return x ** .5
# define func and convert
def quad_calc(a, b, c):
    a = Convert_num(a)
    b = Convert_num(b)
    c = Convert_num(c)
    # run calculations
    inside = b**2 - 4 * a * c
    root = sqr_root(inside)
    if root == None:
        return False
    root_1 = (-b + root)/(2*a)
    root_2 = (-b - root)/(2*a)
    return root_1, root_2
# call in a input while loop to give user values
while True: 
    string = input("Please input a, b, c to enter into quadractic formula with space between each value(say exit to exit)")
    if string.lower() == "exit":
        break
    a, b, c = string.split()
    
    quads = quad_calc(a, b, c)
    
    if quads == False:
        print("Your inputs led to a complex negative square. Try again.")
    else:
        print(f"Your inputs gave the roots {quads[0]} and {quads[1]}")    