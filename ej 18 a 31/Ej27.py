def comparar_rimas(palabra1, palabra2):
  palabra1 = palabra1.lower().strip()
  palabra2 = palabra2.lower().strip()

  ultima_rima1 = palabra1[-3:]
  ultima_rima2 = palabra2[-3:]

  if ultima_rima1 == ultima_rima2:
    return "Riman"
  elif ultima_rima2[-2:] == palabra1[-2:]:  # Coinciden las dos últimas letras
    return "Riman un poco"
  else:
    return "No riman"


def main():
  palabra1 = input("Ingrese la primera palabra: ")
  palabra2 = input("Ingrese la segunda palabra: ")
  resultado_rima = comparar_rimas(palabra1, palabra2)
  print(palabra1[-2:])
  print(f"Las palabras '{palabra1}' y '{palabra2}' {resultado_rima}.")

if __name__ == "__main__":
  main()


#Este me costó un huevo profe