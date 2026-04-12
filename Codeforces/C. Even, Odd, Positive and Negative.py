# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/C

n = int(input())

inp = input()
inp_split = inp.split()


even = 0; odd = 0; positive = 0; negative = 0;

for i in range(n):
    x = int(inp_split[i])

    if x % 2 == 0:
        even += 1
    else:
        odd += 1

    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1


print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)

