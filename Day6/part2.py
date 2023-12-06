with open("Day6/example.txt", "r") as f:
    data = f.read().split("\n")

    time_string = data[0].split(":")[1].strip()
    time_list = time_string.split()

    distance_string = data[1].split(":")[1].strip()
    distance_list = distance_string.split()

    time = int(''.join(time_list))
    distance = int(''.join(distance_list))

   
    def win(t,d):
        total_ways=0
        for i in range(t):
            if(t-i)*i>d:
                total_ways+=1
        return total_ways
    print(win(time,distance))
