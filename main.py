intentos = 3

while intentos > 0:

    user = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if user == "pepe" and contraseña == "5555":
        print("Acceso Correcto")
        break

    else:
        intentos -= 1
        print(f"Acceso Incorrecto. Le quedan {intentos} intentos.")
        