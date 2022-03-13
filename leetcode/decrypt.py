encrypted,k = input().split(",")
k = int(k)

def decrypt_aux(encrypted):
  temp_decrypted = ""

  for caracter in encrypted:
    temp_decrypted += caracter

  return temp_decrypted

#run
decrypted = ""
for index, caracter in enumerate(encrypted):
  if caracter.isalpha():
    decrypted += caracter
  elif caracter.isdigit():
    #clean up digits in segment to re-runned
    segment = encrypted[:index]
    cleaned_segment = "".join([char for char in segment if char.isalpha()])

    decrypted += decrypt_aux(cleaned_segment)

print(decrypted[k-1])