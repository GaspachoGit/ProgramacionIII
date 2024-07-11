tipoHamburguesa = input("¿Qué tipo de hamburguesa desea? (V para vegetariana, NV para no vegetariana): ")

if tipoHamburguesa == "V":
    print("Ingredientes disponibles para hamburguesa vegetariana: calabaza, soja, lechuga, queso, tomate")
    ingrediente = input("Elija un ingrediente adicional: ")
    ingredientes = ["lechuga", "queso", "tomate", ingrediente]
    esVegetariana = True
elif tipoHamburguesa == "NV":
    print("Ingredientes disponibles para hamburguesa no vegetariana: carne vacuna, carne de pollo, lechuga, queso, tomate")
    ingrediente = input("Elija un ingrediente adicional: ")
    ingredientes = ["lechuga", "queso", "tomate", ingrediente]
    esVegetariana = False
else:
    print("Opción no válida.")

if tipoHamburguesa == "V" or tipoHamburguesa == "NV":
    tipo = "vegetariana" if esVegetariana else "no vegetariana"
    print(f"La hamburguesa elegida es {tipo} y lleva los siguientes ingredientes: {', '.join(ingredientes)}")
