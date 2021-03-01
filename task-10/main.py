def print_upto(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)


up_to = int(input("Please enter the number you want to print up to: "))
print_upto(up_to)
