class Producto:
  """Representa un producto en el inventario con nombre, precio y cantidad."""
  
  def __init__(self, nombre: str, precio: float, cantidad: int):
    """Inicializa un producto con validaciones básicas."""
    if nombre == "":
      raise ValueError("El nombre del producto no puede estar vacío.")
    if precio < 0:
      raise ValueError("El precio no puede ser negativo.")
    if cantidad < 0:
      raise ValueError("La cantidad no puede ser negativa.")
    self.nombre = nombre
    self.precio = precio 
    self.cantidad = cantidad
  
  
  def actualizar_precio(self, precio):
    """Actualiza el precio del producto con validación."""
    if precio < 0:
      raise ValueError("El precio no puede ser negativo.")
    self.precio = precio
  
  def actualizar_cantidad(self, cantidad):
    """Actualiza la cantidad del producto con validación."""
    if cantidad < 0:
      raise ValueError("La cantidad no puede ser negativa.")
    self.cantidad = cantidad
    
  def calcular_valor_total(self):
    """Calcula el valor total del producto (precio * cantidad)."""
    return self.precio * self.cantidad
  
  def __str__(self):
    """Retorna una representación en string del producto."""
    return (f"El producto contiene la siguiente información:\n"
                f"  Nombre: {self.nombre}\n"
                f"  Precio: {self.precio:.2f}\n"
                f"  Cantidad: {self.cantidad}")
    
class Inventario:
  """Gestiona una colección de productos."""
  
  def __init__(self):
    """Inicializa un inventario vacío."""
    self.productos = []
    
  def agregar_producto(self, producto):
    """Añade un producto al inventario."""
    self.productos.append(producto)
    
  def buscar_producto(self, nombre):
    """Busca un producto por nombre (case-insensitive)."""
    for i in range(0, len(self.productos)):
      if nombre.lower() == self.productos[i].nombre.lower():
        return self.productos[i]
    return None
  
  def calcular_valor_inventario(self):
    """Calcula el valor total de todos los productos en el inventario."""
    valor_total = 0
    
    for i in range(0, len(self.productos)):
      valor_total += self.productos[i].calcular_valor_total()
    
    return valor_total 
  
  def listar_productos(self):
    """Imprime todos los productos del inventario."""
    for i in range(0, len(self.productos)):
      print(self.productos[i].__str__())
      
      
def menu_principal(inventario):
  """Muestra el menú principal y gestiona las opciones del usuario."""
  valor = 0
  while valor != 5:
    print("1. Agregar producto \n2. Buscar producto\n3. Listar productos\n4. Calcular valor total del inventario\n5. Salir")
    
    try:
      valor = int(input())
    except ValueError:
      print("Error: Por favor, introduce un número entero para la opcion.")
      continue
    
    # Opción 1: Agregar producto
    if valor == 1:
      try:
        print("Introduce el nombre de tu producto:")
        nombre = input() 
                
        print("Introduce el precio de tu producto(Con decimales si lo necesitas):")
        precio = float(input())
                
        print("Introduce la cantidad de tu producto:")
        cantidad = int(input())
              
        producto = Producto(nombre, precio, cantidad)
        inventario.agregar_producto(producto)
                
      except ValueError as e:
        print(f" Error al agregar producto: {e}")
      
    # Opción 2: Buscar producto
    if valor == 2:
      print("Introduce el nombre de tu producto que desea buscar:")
      nombre = str(input())
      result = inventario.buscar_producto(nombre)
      if result == None:
        print("No existe un producto con ese nombre")
      else:
        print(result)
    
    # Opción 3: Listar todos los productos
    if valor == 3:
      inventario.listar_productos()
    
    # Opción 4: Calcular valor total del inventario
    if valor == 4:
      print("El coste total del inventario es " + str(inventario.calcular_valor_inventario()))

if __name__ == "__main__":
  # Punto de entrada del programa
  inventario = Inventario()
  menu_principal(inventario)