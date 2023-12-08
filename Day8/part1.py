file_path="Day8/example.txt"
steps,_,*rest = open(file_path, "r").read().splitlines()

path={}
for line in rest:
    key, value = line.split(" = ")
    path[key] = value[1:-1].split(", ")

#calculate the steps from AAA to reach ZZZ l in steps for left and r for right
stept=0
now="AAA"
while now!="ZZZ":
    stept+=1
    # Print out the steps string and the value of stept
    #print(f"Steps: {steps}, Step count: {stept}")
    #try:
    now=path[now][0 if steps[0]=="L" else 1]
    #except IndexError:
        #print(f"IndexError: Index {stept} out of range for 'steps'")
       # break
    steps=steps[1:]+steps[0]
print(stept)
