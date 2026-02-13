# ループ使用
n, k = map(int, input().split())

count = 0
total = 0 # 食べた豆の個数
while total < k:
  total += n
  n += 1
  count += 1
print(count - 1)


# 別解：等差数列公式使用
# n, k = map(int, input().split()) # n = 0年目に食べる豆の個数 k = x年後の食べた豆の累計個数

# 求めたい物 ＝ x 年後
# 最初の年（０年後）　＝　N
# x 年後　＝　N + x
# 項数 = x + 1(0年目から始まっているから)
# 和 =（最小値＋最大値）* 個数 / 2
# total = (n + (n + x
