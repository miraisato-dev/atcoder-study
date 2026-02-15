n = int(input())
S = [input() for _ in range(n)]

m = max(len(s) for s in S)

for s in S:
    dot = (m - len(s)) // 2
    print("." * dot + s + "." * dot)
