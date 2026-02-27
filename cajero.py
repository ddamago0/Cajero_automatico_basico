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