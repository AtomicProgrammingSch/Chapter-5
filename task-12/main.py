def magic_number():
    number = 7
    guesses = 5
    guessed = False
    while guesses != 0:
        print("Please enter your guess:")
        guess = int(input())
        if guess > number:
            print("Too high!")
            guesses -= 1
        elif guess < number:
            print("Too low!")
            guesses -= 1
        else:
            print("Well done!")
            guessed = True
            break
    if not guessed:
        print("you have gotten your maximum chances")
        return


if __name__ == "__main__":
    magic_number()
