def decimal_a_binario(numero):
  if numero == 0:
    return "0"
  binario = ""
  while numero > 0:
    residuo = numero % 2
    binario = str(residuo) + binario
    numero //= 2
  return binario

def binario_a_decimal(binario):
  if not binario.isdigit():
    raise ValueError("El valor ingresado no es un número binario.")
  decimal = 0
  exponente = 0
  for digito in reversed(binario):
    decimal += int(digito) * (2**exponente)
    exponente += 1
  return decimal





numero_decimal = 10
binario = decimal_a_binario(numero_decimal)
print(f"{numero_decimal} en binario es: {binario}")

numero_binario = "1010"
decimal = binario_a_decimal(numero_binario)
print(f"{numero_binario} en decimal es: {decimal}")
