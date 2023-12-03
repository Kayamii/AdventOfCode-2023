import re
def max_line(input_string): 
    pattern = r'(\d+) (\w+)'
    matches = re.findall(pattern, input_string)
    game_parts = [(int(number), color) for number, color in matches]
    max_red=0
    max_green=0
    max_blue=0
    for number, color in game_parts:
        if color == 'red' and number > max_red:
            max_red=number
        if color == 'green' and number > max_green:
            max_green=number
        if color == 'blue' and number > max_blue:
            max_blue=number
    return max_red*max_green*max_blue                

file_path = 'c:/Users/mrtng/OneDrive/Bureau/AdventOfCode-2023/Day 2/puzzle.txt'
sum=0
with open(file_path, 'r') as f:
    for line in f:
        max= max_line(line)
        sum+=max
    print(sum)   
           
