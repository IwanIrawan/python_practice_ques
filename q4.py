# code a function to calculate the sum and diff of the numbers based on what the user wants

a = int(input("Enter first number"))
b = int(input("Enter second number"))
operation = str(input("Enter your desired operation"))

def operations(a, b, operation):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    else:
        print('This program currently supports only sum and difference operations')

result = operations(a,b,operation)          
print(result) 