n = int(input())

s = 0
for d in range(1, n+1):
  s += (str(d).count("0") + str(d).count("1"))

print(s)