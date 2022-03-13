rows, caracter = input().split(",")

if caracter not in ["!","?","%","&","@",">"]:
  print("false")
else:
  for i in range(int(rows), 0, -1):
    print(caracter*i)