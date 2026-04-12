# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/F

inp = input();
inp_split = inp.split()

x_last = int(inp_split[0]) % 10
y_last = int(inp_split[1]) % 10

sum = x_last + y_last

print(sum)