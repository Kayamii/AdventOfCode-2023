seeds, *parts = open("c:/Users/mrtng/OneDrive/Bureau/AdventOfCode-2023/Day5/example.txt").read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

for block in parts:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for i in seeds:
        for dest, source, length in ranges:
            if source <= i < source + length:
                new.append(i - source + dest)
                break
        else:
            new.append(i)
    seeds = new

print(min(seeds))