import sys

# 에라토스테네스의 체
primes = [True] * 1000001
primes[0] = False
primes[1] = False

for i in range(2, int(len(primes)**0.5)+1):
    if primes[i]:
        for j in range(i+i,  1000001, i):
            primes[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    found = False
    for j in range(3,(n//2)+1,2):
        k = n - j
        if primes[j] and primes[k]:
            found = True
            print(n,"=",j,"+",k)
            break
    if found == False:
        print("Goldbach's conjecture is wrong.")