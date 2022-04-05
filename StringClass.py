from itertools import permutations
from collections import Counter


class StringClass:
    def __init__(self, inpt):
        self.string = inpt

    def length(self):
        return len(self.string)

    def tolist(self):
        return list(self.string)


class SearchCommonElements(StringClass):
    def commonElements(self):
        d = dict(Counter(list(self.string)))
        res = []
        for j in d:
            if d[j] >= 2:
                res.append(j)
        return res


class PairsPossible(StringClass):

    def pair(self):
        self.perm = permutations(list(self.string))
        li = []
        for i in self.perm:
            li.append(i)
            print(list(i), end=" ")

    def show(self):
        return self.li


print(" Enter your number string")
userinput = input()
objstringclass = StringClass(userinput)
print("Length of string is: ", objstringclass.length())
print("String converted to list: ", objstringclass.tolist())
objpairpossible = PairsPossible(userinput)
print("All possible pairs are: ")
objpairpossible.pair()
objsearchcommonelements = SearchCommonElements(userinput)
print()
print("Common elements are: ", objsearchcommonelements.commonElements())
