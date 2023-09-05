"""
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.
"""




"""
# mission failed
def narcissistic(value):
    ls = 0
    x = str(value)
    my_list = list(x)
    print(my_list)
    z = 0
    for i in range(0,10):
        for j in my_list:
            result = 0
            if len(my_list) == 1:    
                 result += int(j)**i
                 print(result, end=" ") 
                 if int(result) == int(value):
                    break
                 
            if len(my_list) >1:
                z += int(j)**i
                
                if  int(z) == int(value):
                    break  
        print("của Z:",z)  
             
        if int(result) == int(value):
                    return print(True,f'{value} is narcissistic')
                    break
        if int(z) == int(value):
                    
                    return print(True,f'{value} is narcissistic')
                    break
        z = 0   
           
        if i == 9:
                return print(False,f'{value} is not narcissistic')
   

narcissistic(7)
print()
narcissistic(371)
print()
narcissistic(3571)
"""

def narcissistic(value):
    # convert number to string to count number of digits
    num_str = str(value)
    num_digits = len(num_str)
    # compute sum of digits raised to the power of num_digits
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    # compare digit_sum to original number
    return digit_sum == value
#giải quyết

#ngắn nhất
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))