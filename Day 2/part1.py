import re
def validate_game(input_string, reds=12, greens=13, blues=14):  
    pattern = r'(\d+) (\w+)'
    matches = re.findall(pattern, input_string)  
    game_parts = [(int(number), color) for number, color in matches]
    for number, color in game_parts:
        if color == 'red' and number > reds:
            return False
        elif color == 'green' and number > greens:
            return False
        elif color == 'blue' and number > blues:
            return False
    return True
i=0
sum=0
file_path = 'c:/Users/mrtng/OneDrive/Bureau/AdventOfCode-2023/Day 2/puzzle.txt'
with open(file_path, 'r') as f:
    for line in f:
        is_valid = validate_game(line)
        i+=1
        if is_valid:
            sum+=i
print(sum)            