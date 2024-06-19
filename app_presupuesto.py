from pymongo import MongoClient

def obtener_base_de_datos():
    cliente = MongoClient("mongodb://localhost:27017/")
    return cliente["presupuesto_db"]

db = obtener_base_de_datos()
coleccion = db["articulos"]

def agregar_articulo(nombre, monto):
    articulo = {"nombre": nombre, "monto": monto}
    coleccion.insert_one(articulo)
    print("\nArtículo agregado exitosamente\n")

def buscar_articulo(nombre):
    articulo = coleccion.find_one({"nombre": nombre})
    if articulo:
        print(f"\nArtículo encontrado: {articulo}\n")
    else:
        print("\nArtículo no encontrado\n")

def actualizar_articulo(nombre, nuevo_nombre, nuevo_monto):
    resultado = coleccion.update_one({"nombre": nombre}, {"$set": {"nombre": nuevo_nombre, "monto": nuevo_monto}})
    if resultado.matched_count:
        print("\nArtículo actualizado exitosamente\n")
    else:
        print("\nArtículo no encontrado\n")

def eliminar_articulo(nombre):
    resultado = coleccion.delete_one({"nombre": nombre})
    if resultado.deleted_count:
        print("\nArtículo eliminado exitosamente\n")
    else:
        print("\nArtículo no encontrado\n")
        
def main():
    while True:
        print("\nSistema de Gestión de Presupuesto")
        print("1. Agregar artículo")
        print("2. Buscar artículo")
        print("3. Actualizar artículo")
        print("4. Eliminar artículo")
        print("5. Salir")

        opcion = input("\nIngrese su opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del artículo: ")
            monto = float(input("Ingrese el monto del artículo: "))
            agregar_articulo(nombre, monto)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del artículo: ")
            buscar_articulo(nombre)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del artículo a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del artículo: ")
            nuevo_monto = float(input("Ingrese el nuevo monto del artículo: "))
            actualizar_articulo(nombre, nuevo_nombre, nuevo_monto)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del artículo a eliminar: ")
            eliminar_articulo(nombre)
        elif opcion == '5':
            print("\nSaliendo...\n")
            break
        else:
            print("\nOpción inválida, por favor intente de nuevo.\n")

if __name__ == "__main__":
    main()