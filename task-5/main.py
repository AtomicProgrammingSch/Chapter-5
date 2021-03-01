def calc_score(string):
    vowels = [["a", 5], ["e", 4], ["i", 3], ["o", 2], ["u", 1]]
    total = 0
    for i in string:
        for j in range(len(vowels)):
            if i == vowels[j][0]:
                total += vowels[j][1]
    return total


print("Please enter your word:")
word = input()
score = calc_score(word)
print("The score for the word '{}' is {}".format(word, str(score)))
