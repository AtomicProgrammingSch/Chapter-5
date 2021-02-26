def highest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print("Please enter your first number:")
num1 = float(input())
print("Please enter your second number:")
num2 = float(input())
print("The biggest number you entered is: " + str(highest(num1, num2)))
