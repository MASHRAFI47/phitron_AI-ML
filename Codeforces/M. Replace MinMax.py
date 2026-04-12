# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M

inp = int(input())
nums = input()
nums_split = nums.split()

num_list = [int(num) for num in nums_split]

#get min and index

min = num_list[0]; min_index = 0

for i in range(inp):
    x = num_list[i]
    if x < min:
        min = x
        min_index = i
       
       
# get max and index 
max = num_list[0]; max_index = 0

for i in range(inp):
    x = num_list[i]
    if x > max:
        max = x
        max_index = i
        

temp = num_list[min_index]
num_list[min_index] = num_list[max_index]
num_list[max_index] = temp


[print(num, end=" ") for num in num_list]


