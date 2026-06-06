stocklibros = 120
cantidad_prestamos = 0
prestamo_libros = 0


print ("Bienvenido al sistema de gestión de préstamos de la Biblioteca Central")

while True:
    print("\n---Menú principal---")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver libro")
    print("4. Historial de préstamos")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("¡Opción inválida! Por favor, ingresa una opción del menú.")
        continue
    
    if opcion == 1:
        print("Libros disponibles:", stocklibros)
    elif opcion == 2:
        try:
            cantidad_prestamos = int(input("Ingrese la cantidad de libros a prestar: "))
            if cantidad_prestamos <= 0:
                print(" Cantidad inválida, ingrese un número entero")
            elif cantidad_prestamos > stocklibros:
                print("No debe superar el stock disponible")
            else:
            
                prestamo_libros += cantidad_prestamos
                stocklibros -= cantidad_prestamos
                print ("Se han prestado", cantidad_prestamos, "libros.")
        except ValueError:
            print ("¡Cantidad inválida! Debe ingresar un número entero positivo.")
            
    elif opcion == 3:
        try:
            cantidad_devoluciones = int(input("Ingrese la cantidad de libros a devolver: "))
            if cantidad_devoluciones <= 0:
                print("Cantidad inválida, ingrese un número entero")
            elif cantidad_devoluciones > prestamo_libros:
                print("No debe superar la cantidad de libros prestados")
            elif stocklibros + cantidad_devoluciones > 120:
                print("No debe superar el stock de libros (120 libros)")
            else:
                stocklibros += cantidad_devoluciones
                prestamo_libros -= cantidad_devoluciones
                print("Se han devuelto", cantidad_devoluciones, "libros.")
        except ValueError:
            print("¡Cantidad inválida! Debe ingresar un número entero positivo.")
    elif opcion == 4:
        print("\n---Historial de préstamos---")
        print("Libros prestados:", prestamo_libros)
  
    elif opcion == 5:
        print("¡Gracias por utilizar nuestro software, hasta la próxima!")
        break
    else:
        print ("Opción inválida. Por favor, seleccione una opción del menú.")
        