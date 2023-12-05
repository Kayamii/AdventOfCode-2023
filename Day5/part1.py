with open("Day5/example.txt") as f:
    lines = f.read().strip().split("\n")
    part = lines[0].split(":")
    title = part[0]
    rest = part[1].split(' ')
    rest.remove(rest[0])
    print(title)
    print(rest)
    seeds = {}
    for word in rest:
        seeds[word] = seeds.get(word, 0) + 1

    for seed, count in seeds.items():
        print(seed)


