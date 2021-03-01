def passed(score):
    if score >= 50:
        return "You passed!"
    elif score < 0:
        return "You can not have a negative score!"
    else:
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
