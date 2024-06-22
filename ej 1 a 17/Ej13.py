contraseñaReal = "password123"
intentosMaximos = 3
intentosRealizados = 0

while intentosRealizados < intentosMaximos:
    contraseñaIngresada = input("Ingrese la contraseña: ")
    intentosRealizados += 1
    
    if contraseñaIngresada == contraseñaReal:
        print("FELICITACIONES")
        break
    
    if intentosRealizados < intentosMaximos:
        print("Contraseña incorrecta. Intenta de nuevo.")
    else:
        print("CONTRASEÑA BLOQUEADA")
