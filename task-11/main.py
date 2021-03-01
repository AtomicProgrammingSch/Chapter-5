def magic_number():
    number = 7
    while True:
        print("Please enter your guess:")
        guess = int(input())
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("Well done!")
            return


if __name__ == "__main__":
    magic_number()
