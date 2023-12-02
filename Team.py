T = []
n = int(input())
for i in range(n):
  j = input().split()
  if j.count('1') >= 2:
      T.append(1)

print(sum(T))
