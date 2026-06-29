from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante("Sabores del Ecuador")


producto1 = Producto("Pizza Familiar", 12.50, 10, True)
producto2 = Producto("Hamburguesa Especial", 8.75, 20, True)


cliente1 = Cliente("María López", 20, "maria@gmail.com", True)
cliente2 = Cliente("Carlos Pérez", 28, "carlos@gmail.com", False)


restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)


print("=" * 45)
print(f"RESTAURANTE: {restaurante.nombre}")
print("=" * 45)

restaurante.mostrar_productos()
restaurante.mostrar_clientes()


print("\n========== RESUMEN ==========")
print(f"Total de productos registrados: {restaurante.total_productos()}")
print(f"Total de clientes registrados: {restaurante.total_clientes()}")
