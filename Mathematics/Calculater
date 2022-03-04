# This function adds two numbers

def add(x,y):
    return x + y

# This function subtracts two numbers

def subtract(x,y):
    return x - y

# This function multiplies two number

def multiply(x,y):
    return x * y

# This function devides two number

def devide(x,y):
    return x / y

print("Select Operation,")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Deivide")


while True:

    # take input from the user
    choice = input("Enter Choice(1/2/3/4):")

    # check if choice is one of the four options
    if choice in('1','2','3','4'):
        num1 = float(input("Enter first number ::"))
        num2 = float(input("Enter second number ::"))

    if choice == '1':
        print(num1, '+', num2, '=', add(num1,num2))

    elif choice == '2':
        print(num1, '-', num2, '=', subtract(num1,num2))

    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1,num2))

    elif choice == '4':
        print(num1, '/', num2, '=', divide(num1,num2))

    # check if user wants another calculation
    # break the while loop if answer is no

    next_calculater = input("let's do next calculation? (yes/no): ")
    if next_calculater == "no":
        break

    else:
        print("Invalid Input")
        
