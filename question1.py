import random
validList = ["1","2","3"]
divby18List = []
for j in range(0,8):
    print(j)
correctNumbers = []
for i in range(10000000, 99999999):
    valid = True
    if i % 18 != 0:
        valid = False
    if valid:
        print("Divisible by 18!")
        divby18List.append(i)
        for counter in range (0,7):
            if str(i)[counter] not in validList:
                valid = False
    print(i, valid, len(validList))
    if valid:
        print("Valid number found!")
        validList.append(i)
print(len(validList))
print(validList)
print(divby18List)