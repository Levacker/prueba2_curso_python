# Sistema de Inventario - Prueba Técnica 2

## Descripción

Este proyecto corresponde a la **segunda prueba técnica de Python** del Máster de Python. Implementa un sistema de gestión de inventario utilizando Programación Orientada a Objetos (POO).

## Características

El sistema permite:

- ✅ **Agregar productos** al inventario con validaciones
- 🔍 **Buscar productos** por nombre (búsqueda case-insensitive)
- 📋 **Listar todos los productos** del inventario
- 💰 **Calcular el valor total** del inventario

## Estructura del Proyecto

El proyecto está compuesto por dos clases principales:

### `Producto`
Representa un producto individual con los siguientes atributos:
- `nombre`: Nombre del producto (str)
- `precio`: Precio unitario (float)
- `cantidad`: Cantidad en stock (int)

### `Inventario`
Gestiona una colección de productos y proporciona métodos para manipularlos.

## Requisitos

- Python 3.6 o superior

## Uso

Para ejecutar el programa:

```bash
python sistema_inventario.py
```

El programa mostrará un menú interactivo con las siguientes opciones:

1. Agregar producto
2. Buscar producto
3. Listar productos
4. Calcular valor total del inventario
5. Salir

## Validaciones

El sistema incluye validaciones para:
- Nombres de productos no vacíos
- Precios no negativos
- Cantidades no negativas
- Entrada de datos con manejo de errores

## Autor

Desarrollado como parte del Máster de Python

## Repositorio

[https://github.com/Levacker/prueba2_curso_python.git](https://github.com/Levacker/prueba2_curso_python.git)

