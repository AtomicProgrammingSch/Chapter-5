def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


print(str(factorial(4)))
