while True:
  n = int(input())

  if n == 0:
    break

  cnt = 0

  for i in range(n,2*n):
      if i==1: #1은 소수가 아니므로 제외
          continue
      for j in range(2,int(i**0.5)+1):
          if i%j==0: #약수가 존재하므로 소수가 아님
              break   #더이상 검사할 필요가 없으므로 멈춤
      else:
          cnt += 1
          
  if n == 1:
    print(n)
    
  else:
    print(cnt)
    
# 왜 시간 초과가 될까...
    