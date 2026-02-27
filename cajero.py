# 1. Configuración inicial
saldo = 1000
numero_operaciones = int(input("¿Cuántas operaciones desea realizar? "))

# 2. Bucle de operaciones
for i in range(numero_operaciones):
    print(f"\n--- Operación {i+1} de {numero_operaciones} ---")
    print("")
    print("1 -> Consultar saldo")
    print("2 -> Retirar dinero")
    print("3 -> Depositar dinero")
    print("")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        print ("")
        print(f"Su saldo actual es: ${saldo}")

    elif opcion == "2":
        monto = float(input("Monto a retirar: "))
        while monto < 0:
            print("Error: El monto no puede ser negativo.")
            monto = float(input("Ingrese un monto positivo: "))
        
        if monto > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${saldo}")