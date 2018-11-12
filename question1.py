import random
validList = ["1","2","3"]
print(len(validList))
divby18List = []
correctNumbers = []
for i in range(10000000, 99999999):
    valid = True
    if i % 18 != 0:
        valid = False
    if valid:
        print("Divisible by 18!")
        divby18List.append(i)
        for counter in range (0,8):
            if str(i)[counter] not in validList:
                valid = False
    print(i, valid, len(correctNumbers))
    if valid:
        print("Valid number found!")
        correctNumbers.append(i)
print(divby18List)
print(len(correctNumbers))
print(correctNumbers)
