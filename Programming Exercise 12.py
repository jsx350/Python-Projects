#Assigns values for both numbers and displays the greater of the two numbers
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

#Asks the user to input both numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

#Assigns a value for the maximum number
maximum = max(number1, number2)

#Prints the output of the function
print(maximum, "is the greater number")