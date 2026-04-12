# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/E

inp = int(input())
numbers = input()
num_split = numbers.split()

min = int(num_split[0]); 
index = 1

for i in range(inp):
    x = int(num_split[i])
    if x < min:
        min = x
        index = i+1
        
print(min, index)
    

