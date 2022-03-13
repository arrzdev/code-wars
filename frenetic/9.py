n = input()

c = ""
best = 0

for caracter in n:
  t = n.count(caracter)
  if t > best:
    best = t
    c = caracter

print(c)