# ABC444 B問題

## 問題
URL: https://atcoder.jp/contests/abc444/tasks/abc444_b

## 考察
・1から N までの整数を全探索する
・各整数について桁和を求める
・桁和が K と一致するものをカウントする
・N ≤ 10^5 なので全探索で大丈夫

## 計算量
・各 i (1〜N) に対して桁和を計算する
・桁数を D とすると O(ND)
・N ≤ 10^5 で D は最大6なので実質 O(N)

## 学び
・一行目：for文、二行目：ジェネレータ文
(int(d) for d in str(i))
と
for d in str(i):
    int(d)は
    同じ
・まだ慣れないが覚える
