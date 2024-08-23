inventario=[]
def menu_principal():
    # Muestra el menu principal
    while True:
        print("Menú Principal")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Vender Producto")
        print("4. Salir")
        
        opcion=input("Seleccione una opcion: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opcion invalida, Por favor intente otra vez")
       

def agregar_producto():
    # Agrega un nuevo producto al inventario
    
    nombre=input("Ingrese el nombre del producto: ")
    precio=float(input("Ingrese el precio del producto: "))
    cantidad=int(input("Ingrese la cantidad del producto: "))
    
    producto={"nombre": nombre, "precio": precio, "stock": cantidad}
    inventario.append(producto)
    
    print(f"Producto {nombre} agregado al inventario")
    
def mostrar_inventario():
    # Muestra todos los productos del inventario
    
    if len(inventario)==0:
        print("El inventario esta vacio")
    else:
        print("Presentando Inventario")
        for producto in inventario:
            print(f"Nombre: {producto["nombre"]}, Precio: {producto["precio"]:.02f}, Stock: {producto["stock"]} ")

def vender_producto():
    # Vende un producto, actualiza el inventario, muestra el total de la venta
    
    nombre=input("Ingrese el nombre del producto que desea vender: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            cantidad=int(input(f"¿Cuantas unidades de {nombre} desea vender?: "))
            if cantidad <= producto["stock"]:
                producto["stock"] -= cantidad
                total = cantidad * producto["precio"]
                print(f"Venta realizada, Total: ${total:.02f}")
                if producto["stock"] == 0:
                    print(f"El producto {nombre} se ha agotado.")
                    
                return
            else:
                print("No hay suficiente Stock en Inventario")
                return
            
            
            
menu_principal()
    