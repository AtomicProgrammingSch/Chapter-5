def find_grade(score):
    if score > 100:
        return False
    elif score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    elif score >= 30:
        return "D"
    elif score < 0:
        return False
    else:
        return "U"


print("Please enter the score: ")
score_str = input()
score = 0
try:
    score = int(score_str)
except ValueError:
    print("The score must be an integer")
    exit(1)
grade = find_grade(score)
if not grade:
    print("The score you entered is invalid!")
    exit(1)

print("The grade for the score of {} is {}".format(score, grade))
