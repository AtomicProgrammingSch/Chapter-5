def passed(score):
    if score >= 50:
        if score >= 80:
            return "You passed, well done!"
        return "You passed!"
    elif score < 0:
        return "You can not have a negative score!"
    else:
        if score <= 20:
            return "You need to try harder!"
        return "You failed!"


print("Please enter the score as an integer:")
str_score = input()
score = 0
try:
    score = int(str_score)
except ValueError:
    print("The score must be entered as an integer")
    exit(1)

msg = passed(score)
print(msg)
