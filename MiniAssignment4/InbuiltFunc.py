func = lambda a, b, c, x: a * x ** 2 + b * x + c

print(func(1, 2, 3, 4))


lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

countOfa = list(map(lambda x:x.count("a"),lst1))
countOfA = list(map(lambda x:x.count("A"),lst1))

print(countOfa)
print(countOfA)
