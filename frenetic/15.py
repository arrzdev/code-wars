alunos, tinta = input().split(",")
tinta = int(tinta)

p = 0
for index, digit in enumerate(alunos):
  tinta -= int(digit)
  
  if tinta == 0:
    print(index + 1)
    break

