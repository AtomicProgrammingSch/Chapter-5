def largest(num1, num2, num3):
    largest = num1
    if largest < num2:
        largest = num2
    if largest < num3:
        largest = num3
    return largest


try:
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))
    num3 = float(input("Please enter your third number: "))
    print("The largest number you entered was: " + str(largest(num1, num2, num3)))
except ValueError:
    print("You must input a number!")
    exit(1)
