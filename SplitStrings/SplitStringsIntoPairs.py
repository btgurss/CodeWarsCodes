def solution(s):
    count = 0
    for char in s:
        count += 1
    count2 = 0
    newArray = []
    while count2 < count:
        letter1 = s[count2]
        count2 += 1
        try:
            letter2 = s[count2]
            count2 += 1
        except:
            letter2 = "_"
        combinedLetters = letter1 + letter2
        newArray.append(combinedLetters)
    return newArray

letters = "hjfidns"
print(solution(letters))