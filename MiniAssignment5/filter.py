from functools import reduce

lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
negNum = list(map(lambda x: -x, list(filter((lambda x: x < 0), lst1))))
print(negNum)

lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
print(reduce(lambda x, y: x * y, lst1))

lst1 = ["Netflix", "Hulu", "Sling", "Hbo"]
lst2 = [198, 166, 237, 125]
res = dict(zip(lst1, lst2))
print(dict(res))
