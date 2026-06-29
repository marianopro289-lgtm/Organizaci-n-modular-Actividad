from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self, nombre: str):
       
        self.nombre = nombre

       
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

  
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)


    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

   
    def mostrar_productos(self):
        print("\n========== PRODUCTOS ==========")
        for producto in self.productos:
            print(producto)
            print("-" * 35)

   
    def mostrar_clientes(self):
        print("\n========== CLIENTES ==========")
        for cliente in self.clientes:
            print(cliente)
            print("-" * 35)


    def total_productos(self):
        return len(self.productos)


    def total_clientes(self):
        return len(self.clientes)
