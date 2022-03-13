
n1, n2, k = input("").split(",")


both = n1+n2
pp = ""

for _ in range(int(k)):
  max = 0
  for index, digit in enumerate(both):
    if int(digit) > int(max):
      max = digit
      new_both = (both)[index+1:]

  both = new_both
  pp += str(max)

print(pp)

        

