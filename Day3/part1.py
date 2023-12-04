with open("c:/Users/mrtng/OneDrive/Bureau/AdventOfCode-2023/Day3/example.txt") as f:
    lines = f.read().strip().split("\n")

l = len(lines)
c = len(lines[0])
print(l,"  ",c)
def check_symb(i, j):
    return 0 <= i < l and 0 <= j < c and lines[i][j] != "." and not lines[i][j].isdigit()

sum = 0

for i, line in enumerate(lines):
    j = 0

    while j < l:
        if line[j].isdigit():
            start = j
            num = ""

            while j < c and line[j].isdigit():
                num += line[j]
                j += 1

            num = int(num)

            if (check_symb(i, start-1) or check_symb(i, j) or
                any(check_symb(i-1, k) or check_symb(i+1, k) for k in range(start-1, j+1))):
                sum += num
        else:
            j += 1


print(sum)
