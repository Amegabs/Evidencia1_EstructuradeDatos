def pedir_nombres():
    """Funcion que pide el nombre"""
    while True:
        nombre = input("Nombre(s): ").strip()
        if nombre == "":
            return None
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("ERROR, INGRESA EL NOMBRE CORRECTAMENTE. SOLO LETRAS.")


def pedir_apellidos():
    """Funcion que pide el apellido"""
    while True:
        apellido = input("Apellido(s): ").strip()
        if apellido == "":
            return None
        if apellido.replace(" ", "").isalpha():
            return apellido
        print("ERROR, INGRESA EL APELLIDO CORRECTAMENTE. SOLO LETRAS.")


def pedir_cupo():
    """Funcion que pide el cupo de las salas"""
    while True:
        cupo = input("Cupo de la sala: ").strip()
        if cupo == "":
            return None
        if cupo.isdigit():
            valor = int(cupo)
            if valor > 0:
                return cupo
            print("ERROR, el cupo debe ser mayor a 0.")
        else:
            print("ERROR, INGRESA EL NUMERO DE CUPO CORRECTAMENTE. SOLO NUMEROS.")


def registrar_reservacion():
    """Funcion que registrara una nueva reservacion en alguna sala disponible"""
try:
            if not Clientes:
                print("Primero debe registrar clientes.")
                return Reservaciones, clave_reservaciones
            if not Salas:
                print("Primero debe registrar salas.")
                return Reservaciones, clave_reservaciones
            
            #clientes
            print("\nClientes Registrados:")
            for ID_Cliente, datos in Clientes.items():
                print(f"{ID_Cliente}. {datos[0]} {datos[1]}")

            while True:
                ID_Cliente = int(input("Ingrese la Clave del Cliente:  [Presione ENTER para cancelar]"))
                try:
                    ID_Cliente = int(input("Ingrese la clave del cliente: "))
                    if ID_Cliente not in Clientes:
                        print("Cliente no encontrado. Intente de nuevo")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar un numero valido.")
                    return Reservaciones, clave_reservaciones
            #pruebas de valores






            #Salas
            print("\nSalas Registradas:")
            for ID_Salas, datos in Salas.items():
                print(f"{ID_Salas}. {datos[0]} {datos[1]}")
            try:
                ID_Salas = int(input("Ingrese la clave de la Sala: "))
            except ValueError:
                print("Debe ingresar un Numero valido.")
                return Reservaciones, clave_reservaciones
            while True:
                if ID_Salas not in Salas:
                    print("Sala no encontrada / no existente.")
                    continue
                break
            
            #fechas
            Fecha_STR = input("Ingrese la Fecha del evento: (DD-MM-AAAA)")
            try:
                Hoy = datetime.date.today()
                FechaEvento = datetime.datetime.strptime(Fecha_STR, "%d-%m-%Y").date()
                FechaAnticipada = (FechaEvento - Hoy).days

                if FechaAnticipada < 2:
                    print("La reservacion debe ser Mayor a 2 dias con Anticipacion")
                    return Reservaciones, clave_reservaciones
            except ValueError:
                    print("Formato de fecha Incorrecto, use DD-MM-AAAA")
                    return Reservaciones, clave_reservaciones

            Turno = input("Que turno desea? (Mañana/Tarde/Noche): ").lower().strip()
            if Turno not in ["mañana", "tarde", "noche"]:
                print("Turno invalido")
                return Reservaciones, clave_reservaciones
            
            #checar
            Reservaciones[clave_reservaciones] = {
                "Cliente": ID_Cliente,
                "Sala": ID_Salas,
                "Fecha":FechaEvento,
                "Turno":Turno,
            }
            print(f"Reserva realizada con exito con una clave de: {clave_reservaciones}")
            clave_reservaciones += 1

            #Validar que no se sobrepongan las fechas...
            for Reserva in Reservaciones.values():
                if Reserva["Sala"] == ID_Salas and Reserva["Fecha"] == FechaEvento and Reserva["Turno"] == Turno:
                    print("Esta Sala ya esta reservada en esta Fecha y Turno")
                    return Reservaciones, clave_reservaciones


    except Exception as Error:
            print("Ocurrio un error inesperado. {Error}")
    return Reservaciones, clave_reservaciones


def editar_reservacion():
    """Funcion que editara el nombre de la reservacion seleccionada por un rango de fechas"""


def consultar_reservacion():
    """Funcion que consultara las reservaciones existentes para una fecha especifica"""


def registrar_cliente(Clientes, clave_clientes):
    """Funcion que registrara a un nuevo cliente"""
    while True:
        try:
            print("Ingresa los datos del cliente:")
            nombre_cliente = pedir_nombres()
            if nombre_cliente is None:
                print("Registro cancelado.")
                continuar = input(
                    "¿Deseas intentar agregar otro cliente? (s para Si/cualquier otra tecla para No): "
                ).lower()
                if continuar != "s":
                    break
                continue

            apellido = pedir_apellidos()
            if apellido is None:
                print("Registro cancelado.")
                continuar = input(
                    "¿Deseas intentar agregar otro cliente? (s para Si/cualquier otra tecla para No): "
                ).lower()
                if continuar != "s":
                    break
                continue

            Clientes[clave_clientes] = {"Nombre": nombre_cliente, "Apellido": apellido}
            print(f"Cliente Agregado Exitosamente con ID {clave_clientes}.")
            clave_clientes += 1

            continuar = input(
                "¿Deseas agregar otro cliente? (s para Si/cualquier otra tecla para No): "
            ).lower()
            if continuar != "s":
                break

        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}.")
            break
    return Clientes, clave_clientes


def registrar_sala(Salas, clave_salas):
    """Funcion que registrara una nueva sala"""
    while True:
        try:
            print("Ingresa los datos de la sala:")
            nombre_sala = pedir_nombres()
            if nombre_sala is None:
                print("Registro cancelado.")
                continuar = input(
                    "¿Deseas intentar agregar otra sala? (s para Si/cualquier otra tecla para No): "
                ).lower()
                if continuar != "s":
                    break
                continue

            cupo_sala = pedir_cupo()
            if cupo_sala is None:
                print("Registro cancelado.")
                continuar = input(
                    "¿Deseas intentar agregar otra sala? (s para Si/cualquier otra tecla para No): "
                ).lower()
                if continuar != "s":
                    break
                continue

            Salas[clave_salas] = {"Nombre": nombre_sala, "Cupo": cupo_sala}
            print(f"Sala agregada exitosamente con ID {clave_salas}.")
            clave_salas += 1

            continuar = input(
                "¿Deseas agregar otra sala? (s para Si/cualquier otra tecla para No): "
            ).lower()
            if continuar != "s":
                break
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
            break
    return Salas, clave_salas


def main(
    Reservaciones, clave_reservaciones, Clientes, clave_clientes, Salas, clave_salas
):
    while True:
        print("\nMENU PRINCIPAL.")
        print("Opciones disponibles: ")
        print("1. Registrar nueva reservacion.")
        print("2. Editar nombre de reservacion.")
        print("3. Consultar reservaciones.")
        print("4. Registrar nuevo cliente.")
        print("5. Registrar nueva sala.")
        print("6. Salir.\n")
        opcion = input("Selecciona la opcion que necesites (1-6): ").strip()
        if opcion.isdigit():
            if opcion == "1":
                registrar_reservacion()
            elif opcion == "2":
                editar_reservacion()
            elif opcion == "3":
                consultar_reservacion()
            elif opcion == "4":
                Clientes, clave_clientes = registrar_cliente(Clientes, clave_clientes)
            elif opcion == "5":
                Salas, clave_salas = registrar_sala(Salas, clave_salas)
            elif opcion == "6":
                break
            else:
                print("ERROR, INGRESA UNA OPCION VALIDA (1-6).")
        else:
            print("ERROR, INGRESA UNA OPCION VALIDA (1-6).")
    return (
        Reservaciones,
        clave_reservaciones,
        Clientes,
        clave_clientes,
        Salas,
        clave_salas,
    )


if __name__ == "__main__":
    Reservaciones = dict()
    clave_reservaciones = 1

    Clientes = dict()
    clave_clientes = 1

    Salas = dict()
    clave_salas = 1

    (
        Reservaciones,
        clave_reservaciones,
        Clientes,
        clave_clientes,
        Salas,
        clave_salas,
    ) = main(
        Reservaciones, clave_reservaciones, Clientes, clave_clientes, Salas, clave_salas
    )

