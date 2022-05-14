arraySize = input()                  # Reading input from STDIN
arrayList = list(map(int, input().split()))

absList = abs(arrayList)
absList.sort()
print(absList[0])  