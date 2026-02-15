# ABC445 A問題

## 問題
URL: https://atcoder.jp/contests/abc445/tasks/abc445_a

## 考察
・文字列 S が与えられる
・先頭文字 S[0] と末尾文字 S[-1] を比較すればよい
・文字列はそのままインデックスアクセスできるため変換不要
・一致すれば Yes、しなければ No

## 計算量
O(1)　定数時間

## 学び
・Python の文字列は iterable かつ index access が可能
・末尾要素は S[-1] で取得できる
・先頭・末尾の取得は O(1)の計算量
