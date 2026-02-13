# ABC442 A問題

## 問題
URL: https://atcoder.jp/contests/abc442/tasks/abc442_a

## 考察
・文字列を 1 文字ずつ確認する
・文字が "i" または "j" なら 1 を加算
・それ以外なら 0

## 計算量
・文字列長を N とすると O(N)

## 学び
・文字列(str)は list に変換しなくても iterable
・c in "ij" で複数条件を簡潔に書ける
  ・sum(c in "ij" for c in s) という書き方が可能
**sum(c in "ij" for c in s)は下記の略**
total = 0
for c in s:
    if c in "ij":
        total += 1
    else:
        total += 0

print(total)
****
・match文はこの課題には少しやり過ぎ、もっと簡潔に書く方法がある
