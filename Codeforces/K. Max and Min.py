# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/KS

inp = input()
inp_split = inp.split()

x = int(inp_split[0])
y = int(inp_split[1])
z = int(inp_split[2])

max = x
min = x

if y < min:
    min = y
if z < min: 
    min = z

if y > max:
    max = y
if z > max:
    max = z

print(min, max)