

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = [x + y for x in list1 for y in list2]
print(res)

listA = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
listToBeAdded = ["h", "i", "j"]
listA[2][1][2].extend(listToBeAdded)
print(listA)

dict1 = {"ten": 10, "Twenty": 20, "Thirty": 30}

dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
for key, value in dict2.items():
    dict3[key] = value
print(dict3)

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sampleDict['location'] = sampleDict.pop('city')
print(sampleDict)

Dic = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
DicList = list(Dic.items())
print(DicList)
