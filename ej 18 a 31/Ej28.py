def mostrar_productos(productos):
  for codigo, producto in productos.items():
    nombre = producto["nombre"]
    precio = producto["precio"]
    print(f"{codigo} - {nombre}: ${precio:.2f}")

def validar_codigo_producto(productos, codigo_ingresado):
  return codigo_ingresado in productos

def obtener_cantidad_producto(codigo_producto, productos):
  while True:
    try:
      cantidad = int(input(f"Ingrese la cantidad de unidades de {productos[codigo_producto]['nombre']}: "))
      if cantidad > 0:
        return cantidad
      else:
        print("Error: La cantidad debe ser un número entero positivo.")
    except ValueError:
      print("Error: Ingrese un número entero válido.")

def calcular_total_producto(codigo_producto, cantidad, productos):
  precio_unitario = productos[codigo_producto]["precio"]
  total_producto = precio_unitario * cantidad
  return total_producto

def generar_factura(productos):
  total_factura = 0
  print("\nFactura:")
  print("-" * 40)
  print(f"| Código | Producto | Cantidad | Precio Unit. | Total |")
  print("-" * 40)

  for codigo_producto, producto in productos.items():
    nombre = producto["nombre"]
    precio_unitario = producto["precio"]
    cantidad = obtener_cantidad_producto(codigo_producto, productos)
    total_producto = calcular_total_producto(codigo_producto, cantidad, productos)

    print(f"| {codigo_producto:>7} | {nombre:<20} | {cantidad:>8} | ${precio_unitario:.2f} | ${total_producto:.2f} |")
    total_factura += total_producto

  print("-" * 40)
  print(f"| TOTAL |          |         |             | ${total_factura:.2f} |")
  print("-" * 40)

# Ejemplo de uso
productos = {
  "A123": {"nombre": "Camisa", "precio": 50.00},
  "B456": {"nombre": "Pantalón", "precio": 75.50},
  "C789": {"nombre": "Zapatillas", "precio": 120.00}
}

generar_factura(productos)
