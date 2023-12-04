file_path = "c:/Users/mrtng/OneDrive/Bureau/AdventOfCode-2023/Day 4/example.txt"
num = 0
total=0
with open(file_path) as f:
    for line in f:
        total_points = 1
        matched_numbers = set()

        lines = line.strip().split("|")
        win = lines[0].split(":")[1]
        picks = lines[1]

        print("Win:", win)
        print("Picks:", picks)

        w = win.split(" ")
        p = picks.split(" ")
        
        for w_num in w:
            for p_num in p:
                if w_num == p_num and w_num not in matched_numbers and w_num != "":
                    matched_numbers.add(w_num)

        print("Matched numbers:", matched_numbers)

        fac = len(matched_numbers)
        num += 1
        if fac > 0:
            total_points = 2 ** (fac - 1)
        else:
            total_points = 0
        total += total_points
        print("Total points of", num, ":", total_points)
        print("Total points:", total)
