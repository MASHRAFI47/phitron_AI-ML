#https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/K

inp = int(input())

num = int(input())

sum = 0
while num > 0:
    x = num % 10
    sum += x
    num //= 10
    
print(sum)
    
    