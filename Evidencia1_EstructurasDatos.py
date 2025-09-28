import datetime

def pedir_nombres():
    """Funcion que pide el nombre"""
    while True:
        nombre = input("Nombre(s): ")
        if nombre == "":
            return None
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("ERROR, INGRESA EL NOMBRE CORRECTAMENTE. SOLO LETRAS.")


def pedir_apellidos():
    """Funcion que pide el apellido"""
    while True:
        apellido = input("Apellido(s): ")
        if apellido == "":
            return None
        if apellido.replace(" ", "").isalpha():
            return apellido
        print("ERROR, INGRESA EL APELLIDO CORRECTAMENTE. SOLO LETRAS.")


def pedir_cupo():
    """Funcion que pide el numero de telefono"""
    while True:
        cupo = input("Cupo de la sala: ")
        if cupo == "":
            return None
        if cupo.isdigit():
            return cupo
        print("ERROR, INGRESA EL TELEFONO CORRECTAMENTE. SOLO NUMEROS.")


#yo el master meiker:
def registrar_reservacion(Reservaciones, clave_reservaciones, Clientes, Salas):
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
                Entrada = input("Ingrese la Clave del Cliente [ENTER para cancelar]:").strip()
                if Entrada == "":
                    print("Operacion Cancelada...")
                    return Reservaciones, clave_reservaciones
                
                try:
                    ID_Cliente = int(Entrada)
                except ValueError:
                    print("Debe ingresar un numero valido")
                    continue
                if ID_Cliente not in Clientes:
                    print("Cliente no encontrado. Intente de nuevo")
                    continue
                break
            #pruebas de valores




            #Salas
            print("\nSalas Registradas:")
            for ID_Salas, datos in Salas.items():
                print(f"{ID_Salas}. {datos[0]} (Cupo: {datos[1]})")

            while True:
                Entrada = input("Ingrese la clave de la sala (ENTER para cancelar): ").strip()
                if Entrada == "":
                    print("Operación cancelada.")
                    return Reservaciones, clave_reservaciones
                try:
                    ID_Salas = int(Entrada)
                    if ID_Salas not in Salas:
                        print("Sala no encontrada. Intente de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar un Numero valido")

            
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

            Turno = input("Que turno desea? (Matutino/Vespertino/Nocturno): ").lower().strip()
            if Turno not in ["matutino", "vespertino", "nocturno"]:
                print("Turno invalido")
                return Reservaciones, clave_reservaciones
            
            #Name???
            while True:
                NombreEvento = input("Ingrese el Nombre de su Evento: ").strip()
                if NombreEvento == "":
                    print("Este registro no se puede quedar en Blanco, vuelva a intentarlo.")
                    continue
                else:
                    break

            #Validar que no se sobrepongan las fechas...
            for Reserva in Reservaciones.values():
                if Reserva["Sala"] == ID_Salas and Reserva["Fecha"] == FechaEvento and Reserva["Turno"] == Turno:
                    print("Esta Sala ya esta reservada en esta Fecha y Turno")
                    return Reservaciones, clave_reservaciones
            
            #checar
            Reservaciones[clave_reservaciones] = {
                "Cliente": ID_Cliente,
                "Sala": ID_Salas,
                "Fecha":FechaEvento,
                "Turno":Turno,
                "Evento": NombreEvento
            }
            print(f"Reserva realizada con exito con una clave de: {clave_reservaciones}")
            clave_reservaciones += 1
            return Reservaciones, clave_reservaciones

    except Exception as Error:
        print(f"Ocurrio un error inesperado: {Error}")
        return Reservaciones, clave_reservaciones




#gabs
def editar_reservacion():
    """Funcion que editara el nombre de la reservacion seleccionada por un rango de fechas"""
    if not Reservaciones:
        print("No existen reservaciones registradas.")
        return Reservaciones

    try:
        fecha_inicio_str = input("Ingresa la fecha de inicio: ")
        fecha_fin_str = input("Ingresa la fecha de fin:  ")

        fecha_inicio_str = datetime.datetime.strptime(fecha_inicio_str, "%d-%m-%Y").date()
        fecha_fin_str = datetime.datetime.strptime(fecha_fin_str, "%d-%m-%Y").date()

        print("\nReservaciones en el rango dado: ")
        encontrados = []
        for clave, datos in Reservaciones.items():
            if fecha_fin_str <= datos["Fecha"] <= fecha_fin_str:
                print(f"Clave: {clave} | Cliente: {datos['Cliente']} | "
                      f"Sala: {datos['Sala']} | Fecha: {datos['Fecha']} | "
                      f"Turno: {datos['Turno']} | Evento: {datos.get('Evento','(sin nombre)')}")
                encontrados.append(clave)

        if not encontrados:
            print("No se encontraron reservaciones en ese rango.")
            return Reservaciones
        
        while True:
            try:
                clave_edit = int(input("Ingrese la clave de la reservación que desea editar: "))
                if clave_edit not in encontrados:
                    print("Clave inválida, intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Debe ingresar un número válido.")

        nuevo_nombre = input("Ingrese el nuevo nombre del evento: ")
        Reservaciones[clave_edit]["Evento"] = nuevo_nombre
        print("Nombre del evento actualizado con éxito.")

    except ValueError:
        print("Error en el formato de fechas, use DD-MM-AAAA.")

    return Reservaciones
#gabs
def consultar_reservacion():
    """Funcion que consultara las reservaciones existentes para una fecha especifica"""
    if not Reservaciones:
        print("No existen reservaciones registradas.")
        return

    try:
        fecha_str = input("Ingrese la fecha a consultar (DD-MM-AAAA): ")
        fecha = datetime.datetime.strptime(fecha_str, "%d-%m-%Y").date()

        print(f"\nReservaciones para la fecha {fecha}:")
        print("{:<10} {:<20} {:<20} {:<12} {:<10} {:<15}".format(
            "Clave", "Cliente", "Sala", "Fecha", "Turno", "Evento"
        ))
        print("-" * 110)

        encontrados = False
        for clave, datos in Reservaciones.items():
            if datos["Fecha"] == fecha:

                nombre_Cliente = Clientes.get(datos["Cliente"], [f"ID {datos['Cliente']}"])[0]
                nombre_Sala = Salas.get(datos["Sala"], [f"ID {datos['Sala']}"])[0]
                                              
                print("{:<10} {:<20} {:<20} {:<12} {:<10} {:<15}".format(
                    clave, nombre_Cliente, nombre_Sala,
                    datos["Fecha"].strftime("%d-%m-%Y"),
                    datos["Turno"], datos.get("Evento", "(sin nombre)")
                ))
                encontrados = True

        if not encontrados:
            print("No hay reservaciones para esa fecha.")

    except ValueError:
        print("Formato incorrecto, use DD-MM-AAAA.")  

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
                else:
                    continue

            apellido = pedir_apellidos()
            if apellido is None:
                print("Registro cancelado.")
                continuar = input(
                    "¿Deseas intentar agregar otro cliente? (s para Si/cualquier otra tecla para No): "
                ).lower()
                if continuar != "s":
                    break
                else:
                    continue

            datos_cliente = [nombre_cliente, apellido]
            Clientes[clave_clientes] = datos_cliente
            print("Cliente Agregado Exitosamente")
            clave_clientes += 1

            continuar = input(
                "¿Deseas agregar otro cliente? (s para Si/cualquier otra tecla para No): "
            ).lower()
            if continuar != "s":
                break

        except ValueError:
            print("Ocurrio un error inesperado.")
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
                else:
                    continue

            cupo_sala = pedir_cupo()
            if cupo_sala is None:
                print("Registro cancelado.")
                continuar = input(
                    "¿Deseas intentar agregar otra sala? (s para Si/cualquier otra tecla para No): "
                ).lower()
                if continuar != "s":
                    break
                else:
                    continue

            datos_salas = [nombre_sala, cupo_sala]
            Salas[clave_salas] = datos_salas
            print("Sala agregada exitosamente.")
            clave_salas += 1

            continuar = input(
                "¿Deseas agregar otra sala? (s para Si/cualquier otra tecla para No): "
            ).lower()
            if continuar != "s":
                break
        except ValueError:
            print("Ocurrio un error inesperado.")
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
        opcion = input("Selecciona la opcion que necesites (1-6): ")
        if opcion.isdigit():
            if opcion == "1":
                Reservaciones, clave_reservaciones = registrar_reservacion(
                    Reservaciones, clave_reservaciones, Clientes, Salas
                )
            elif opcion == "2":
                editar_reservacion()
            elif opcion == "3":
                consultar_reservacion()
            elif opcion == "4":
                Clientes, clave_clientes = registrar_cliente(Clientes, clave_clientes)
            elif opcion == "5":
                Salas, clave_salas = registrar_sala(Salas, clave_salas)
            elif opcion == "6":
                print("Saliendo...")
                break
            else:
                print("ERROR, INGRESA UNA OPCION VALIDA")
        else:
            print("ERROR, INGRESA UNA OPCION VALIDA")
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
        clave_salas
    ) = main(
        Reservaciones, clave_reservaciones, Clientes, clave_clientes, Salas, clave_salas
    )





