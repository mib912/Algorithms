import sys
input = sys.stdin.readline

n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))

dp = [0] * (n+1)
dp[1] = wine[1] # 1번째는 첫잔 마시는게 최대

if n > 1:
    dp[2] = wine[1] + wine[2] # 2번째는 첫번째 잔 + 두번째 잔 마시는게 최대

# i번째 와인을 마시고 i-2까지 마신 양
# i번째를 마시지 않음 
# i, i-1번째를 마시고 i-3번째 까지 마신 양 
for i in range(3, n+1):
    dp[i] = max(dp[i-2] + wine[i], dp[i-1], dp[i-3]+wine[i-1]+wine[i]) 
    

print(dp[n])