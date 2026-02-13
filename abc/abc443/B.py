n, k = map(int, input().split())

count = 0
total = 0 # 食べた豆の個数
while total < k:
  total += n
  n += 1
  count += 1
print(count - 1)
