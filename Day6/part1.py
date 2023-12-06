with open("Day6/example.txt", "r") as f:
    data = f.read().split("\n")

    time_string = data[0].split(":")[1].strip()
    time_list = time_string.split()

    distance_string = data[1].split(":")[1].strip()
    distance_list = distance_string.split()

    time = []
    distance = []
    for i in time_list:
        time.append(int(i))
    print(time)
    for i in distance_list:
        distance.append(int(i))
    print(distance)    
    
    def win(t,d):
        total_ways=0
        for i in range(t):
            if(t-i)*i>d:
                total_ways+=1
        return total_ways
    for t,d in zip(time,distance):
        print(win(t,d))

    result =1
    for t,d in zip(time,distance):
        result*=win(t,d)
    print(result)            
