n = int(input())

m = 0
s_list = []

for i in range(n):
  s = (input())
  s_list.append(s)
  if m < len(s):
    m = len(s)
for k in s_list:
  if len(k) < m:
    dot = (m - len(k)) // 2
    t = "." * dot + k + "." * dot
    print(t)
  else:
    print(k)
