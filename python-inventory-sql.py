import sqlite3

conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL,
                    detalles TEXT NOT NULL)''')


def mostrar_menu():
    print("\nMenú interactivo de inventario:")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def agregar_producto():
    try:
        nombre = str(input("Ingrese el nombre del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        detalles = str(input("Ingrese los detalles del producto: "))

        if not nombre or not detalles or precio <= 0:
            print("Los datos ingresados no son válidos, por favor intente de nuevo.")
        else:
            cursor.execute('INSERT INTO productos (nombre, precio, detalles) VALUES (?, ?, ?)', (nombre, precio, detalles))
            conn.commit()
            print(f"Producto '{nombre}' agregado exitosamente.")
    except ValueError:
        print("Los datos ingresados no son válidos, por favor intente de nuevo.")


def ver_productos():
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    if not productos:
        print("El inventario está vacío.")
    else:
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}, Detalles: {producto[3]}")

def actualizar_producto():
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    nombre = input("Ingrese el nuevo nombre del producto: ")
    precio = float(input("Ingrese el nuevo precio del producto: "))
    detalles = input("Ingrese los nuevos detalles del producto: ")
    cursor.execute('UPDATE productos SET nombre = ?, precio = ?, detalles = ? WHERE id = ?', (nombre, precio, detalles, id_producto))
    conn.commit()
    print(f"Producto con ID {id_producto} actualizado exitosamente.")

def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    conn.commit()
    print(f"Producto con ID {id_producto} eliminado exitosamente.")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        ver_productos()
    elif opcion == '3':
        actualizar_producto()
    elif opcion == '4':
        eliminar_producto()
    elif opcion == '5':
        print("Saliendo del programa. ¡Adiós!")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")

conn.close()
