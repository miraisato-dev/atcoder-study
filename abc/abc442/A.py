s = input()

dot_count = 0

for i in s:
  match i:
    case "i" | "j":
      dot_count += 1
print(dot_count)
