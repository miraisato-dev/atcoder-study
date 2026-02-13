Q = int(input())

volume = 0
is_playing = False

for i in range(Q):
  num = int(input())
  match num:
    case 1:
      volume += 1
    case 2:
      if volume == 0:
        continue
      else:
        volume -= 1
    case 3:
      if is_playing == False:
        is_playing = True
      else:
        is_playing = False
  if volume >= 3 and is_playing == True:
    print("Yes")
  else:
    print("No")
  count += 1
