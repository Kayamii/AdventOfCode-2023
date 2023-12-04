file_path = "c:/Users/mrtng/OneDrive/Bureau/AdventOfCode-2023/Day4/example.txt"
mapp = {}

with open(file_path) as f:
    lines = f.read().strip().split("\n")
    mapp = {i: 1 for i in range(len(lines))}

    for i, line in enumerate(lines):
        parts = line.split(":")
        x = parts[1].strip()
        groups = x.split(" | ")
        a = list(map(int, groups[0].split()))
        b = list(map(int, groups[1].split()))

        j = sum(1 for i in b if i in a)

        for n in range(i + 1, i + j + 1):
            mapp[n] = mapp.get(n, 0) + mapp[i]
print(sum(mapp.values()))
