from tracemalloc import stop


n = int(input())
goal = int(input())
current_gas = int(input())


stops = []
for _ in range(n-2):
  km, gas = input().split(",")
  km, gas = int(km), int(gas)

  stops.append((km, gas))

#find
stopped_for_gas = 0
while True:
  if current_gas >= goal:
    print(stopped_for_gas)
    break
  else:
    #filter possible stops
    temp_stops = list(filter(lambda x: current_gas >= x[0], stops))
    if len(temp_stops) == 0:
      print(-1)
      break

    #print(temp_stops[-1])

    #stop and add gas
    stopped_for_gas += 1
    current_gas += temp_stops[-1][1] 

    #remove it
    stops.remove(temp_stops[-1])
