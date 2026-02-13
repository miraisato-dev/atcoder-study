n, k = map(int, input().split()) # n = 以下の正整数, k = 桁和

count = 0

for i in range(1, n + 1):
  digit_sum = sum(int(d) for d in str(i))
  if digit_sum == k:
    count += 1

print(count)
