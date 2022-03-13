pos,n2,n3 = input().split(",")
pos,n2,n3 = int(pos),int(n2),int(n3)

m = []

#find at least pos-n multiples of each number 2 and 3
for i in [n2, n3]:
  for j in range(1, pos+1):
    t = i*j
    if t not in m:
      m.append(t)

#sort 
n = sorted(m)
#print(n)

print(n[pos-1])


