# Sistema de Restaurante

## Nombre del estudiante

**Nombre:** Josue Batallas

## Descripción del proyecto

 Se desarrollo un sistema básico de gestión para un restaurante. El sistema permite registrar y listar productos, bebidas y clientes mediante un menú ejecutado desde la consola.


# Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

---

# Responsabilidad de cada clase

## Producto

Es un producto general del restaurante y almacena información como código, nombre, categoría y precio.

## Bebida

Hereda de la clase Producto e incorpora información específica de una bebida, como tamaño y tipo de envase.

## Cliente

Se representa la información de un cliente registrado, incluyendo identificación, nombre y correo electrónico.

## Restaurante

Administra el registro, listado de productos y clientes. También verifica que no existan códigos o identificaciones duplicadas.

## main.py

Es el punto de inicio del programa. Muestra el menú interactivo, solicitar la información al usuario y llamar a los métodos del servicio Restaurante.

---

# Relación entre Producto y Bebida

La clase Bebida hereda de la clase Producto porque una bebida representa un tipo específico de producto.

Una bebida puede utilizar todas las características de un producto y añadir información adicional sin modificar la estructura del sistema.

---

# Principios SOLID aplicados

## SRP

Cada clase tiene una única responsabilidad.

- Producto representa productos.
- Bebida representa bebidas.
- Cliente representa clientes.
- Restaurante administra la información.
- main.py controla la interacción con el usuario.

## OCP

El sistema puede ampliarse agregando nuevas clases derivadas de Producto sin modificar la lógica principal de Restaurante.

## LSP

Los objetos de la clase Bebida pueden utilizarse como objetos de tipo Producto sin afectar el funcionamiento del programa.

---

# Instrucciones de ejecución

1. Abrir el proyecto en Visual Studio Code.
2. Abrir la terminal.
3. Ubicarse en la carpeta del proyecto.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

5. Utilizar el menú interactivo para registrar y listar productos, bebidas y clientes.

---

# Reflexión

Este programa me ayudo a entender el desarrollo de aplicaciones más organizadas. Esta aplicación me ayudo a distribuir correctamente las responsabilidades de cada clase, sin afectar el funcionamiento existente.