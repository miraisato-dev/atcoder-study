# ABC442 B問題 MusicPlayer

## 問題
URL: https://atcoder.jp/contests/abc442/tasks/abc442_b

## 考察
・状態は2つだけ管理すればよい
・音量 volume
・再生状態 is_playing
・操作ごとに状態を更新する「シミュレーション問題」
・各操作後にvolume >= 3 かつ is_playing == Trueを判定する

## 計算量
・Q 回の操作を1回ずつ処理
・各操作は O(1)

## 学び
・操作3に関しては反転なのでis_playing = not_playingで解決できる（シンプルなTrue／False状態変更方法）
・最初は is_playing が更新されていないミスがあった　状態更新が本質だと気づいた
・状態管理問題では「今の値」「どう更新するか」を明確にすることが重要
・反転（トグル）処理はx = not x
・不要な変数は持たない（count など）
・continue を使うときは「その後の処理も飛ぶ」ことに注意
