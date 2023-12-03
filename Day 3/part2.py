with open("c:/Users/mrtng/OneDrive/Bureau/AdventOfCode-2023/Day 3/example.txt") as f:
    data = f.read()
    lines = data.strip().split("\n")

l = len(lines)
c = len(lines[0])

valids = [[[] for _ in range(c)] for _ in range(l)]

def check_symb(i, j, num):
    if not (0 <= i < l and 0 <= j < c):
        return False

    if lines[i][j] == "*":
        valids[i][j].append(num)
    return lines[i][j] != "." and not lines[i][j].isdigit()

sum = 0

for i, line in enumerate(lines):
    start = 0
    j = 0

    while j < l:
        start = j
        num = ""
        while j < l and line[j].isdigit():
            num += line[j]
            j += 1

        if num == "":
            j += 1
            continue

        num = int(num)

       
        check_symb(i, start-1, num) or check_symb(i, j, num)

        for k in range(start-1, j+1):
            check_symb(i-1, k, num) or check_symb(i+1, k, num)

for i in range(l):
    for j in range(c):
        nums = valids[i][j]
        if lines[i][j] == "*" and len(nums) == 2:
            sum += nums[0] * nums[1]

print(sum)
