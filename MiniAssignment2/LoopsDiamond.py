# diamond
rows = int(input("Enter The Number Of Rows: "))
columns = 2 * rows - 1
i = 0
while i < rows:
    j = 0
    while j < columns:
        if (columns // 2) - i <= j <= (columns // 2) + i:
            print("*", end="")
        else:
            print(" ", end="")

        j += 1
    print(" ")
    i += 1

i = 0
while i < rows:
    j = 0
    while j < columns:
        if i <= j <= columns - 1 - i:
            print("*", end="")
        else:
            print(" ", end="")

        j += 1
    print(" ")
    i += 1

# hollow triangle
row = int(input('Enter number of rows required: '))

for i in range(row):
    for j in range(row - i):
        print(' ', end='')  # printing space required and staying in same line

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == row - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
