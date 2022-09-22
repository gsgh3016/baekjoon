import math

m, n = map(int, input().split())

sieve = [True] * n

sqrt_n = int(math.sqrt(n))
for i in range(2, sqrt_n + 1):
  if sieve[i] == True:           # i가 소수인 경우 
    for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
      sieve[j] = False

    # 소수 목록 산출
for i in range(m,n):
  if sieve[i]:
    print(i)
