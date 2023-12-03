import regex as re

file_path = "example.txt"

result = 0

num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
    
}
 

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)


        for i in range(len(numbers)):
            if numbers[i].isnumeric() == False:
                numbers[i] = num_map.get(numbers[i])
        
        code = str(numbers[0]) + str(numbers[-1])

        result += int(code)

print(result)