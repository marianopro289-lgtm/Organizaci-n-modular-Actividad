class Cliente:
    def __init__(self, nombre: str, edad: int, correo: str, vip: bool):
       
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.vip = vip

    def __str__(self):
        tipo = "VIP" if self.vip else "Regular"
        return (
            f"Cliente: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Correo: {self.correo}\n"
            f"Tipo: {tipo}"
        )
