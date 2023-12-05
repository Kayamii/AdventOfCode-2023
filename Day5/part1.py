file_path = "c:/Users/mrtng/OneDrive/Bureau/AdventOfCode-2023/Day5/example.txt"

with open(file_path) as file:
    file_content = file.read()

seeds_part, *parts = file_content.split("\n\n")
seeds_string = seeds_part.split(":")[1]
seeds = list(map(int, seeds_string.split()))

for block in parts:
    ranges = []
    lines = block.splitlines()[1:]

    for line in lines:
        range_values = list(map(int, line.split()))
        ranges.append(range_values)

    new_seeds = []

    for seed in seeds:
        for dest, source, length in ranges:
            if source <= seed < source + length:
                transformed_seed = seed - source + dest
                new_seeds.append(transformed_seed)
                break
        else:
            new_seeds.append(seed)

    seeds = new_seeds

print(min(seeds))
