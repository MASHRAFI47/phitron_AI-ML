# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/H

inp = int(input())

for i in range(inp):
    str = input()
    if "010" in str or "101" in str:
        print("Good")
    else:
        print("Bad")