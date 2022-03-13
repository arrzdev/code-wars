p = int(input())

estacionamento = []

ordem = []

for _ in range(p):
  act, matricula = input().split(" - ")


  if act == "aceitarCarro" and len(estacionamento) != 5:
    estacionamento.append(matricula)

  elif act == "sairCarro":
    estacionamento.remove(matricula)

  if matricula not in ordem:
    ordem.append(matricula)

#filter with the correct order
estacionamento = list(filter(lambda x: x in estacionamento, ordem))

print(len(estacionamento))
for mat in estacionamento:
  print(mat)
