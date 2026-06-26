def menu():
    while True:
        print("=== MI PRIMER MENÚ ===")
        print("1. SUMA")
        print("2. RESTA")
        print("3. HOLA")
        print("4. ADIOS")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("Sumando")
        elif opcion == 2:
            print("Restando")
        elif opcion == 3:
            print("Saludando")
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Ingrese una opción válida")

menu()