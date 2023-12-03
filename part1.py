def extract_calibration_values(line):
    first_digit = 0
    last_digit = 0      
    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break

    for char in reversed(line):
        if char.isdigit():
            last_digit = int(char)
            break

    calibration_value = int(str(first_digit) + str(last_digit))
    return calibration_value    

def sum_of_digits():
    total = 0
    with open('example.txt') as f:
        for line in f:
            calibration_value = extract_calibration_values(line)
            total += calibration_value
    return total
   
def main():
    total_sum = sum_of_digits()
    print(total_sum)

main()
