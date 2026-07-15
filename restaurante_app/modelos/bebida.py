from .producto import Producto


class Bebida(Producto):
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        envase: str
    ):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = tamano
        self.envase = envase

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Tamaño: {self.tamano}\n"
            f"Envase: {self.envase}"
        )
        