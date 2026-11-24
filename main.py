from paciente import Paciente
from medico import Medico
from registrar_cita import RegistrarCita as Cita

# Listas donde se guardarán los datos mientras el programa esté abierto
pacientes = []
medicos = []
citas = []


def mostrar_menu():
    print("\n=== CITARURAL - Centro de Salud ===")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Registrar cita")
    print("4. Ver citas")
    print("5. Cambiar estado de una cita")
    print("6. Buscar persona por código")
    print("7. Buscar médicos por especialidad")
    print("8. Salir")

def registrar_paciente():
    print("\n--- Registrar paciente ---")

    while True:
        dni = input("DNI (8 dígitos): ")
        if len(dni) == 8 and dni.isdigit():
            break
        print("Error: el DNI debe tener exactamente 8 dígitos numéricos. Intenta de nuevo.")

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de nacimiento (AAAA-MM-DD): ")

    while True:
        telefono = input("Teléfono (9 dígitos): ")
        if len(telefono) == 9 and telefono.isdigit():
            break
        print("Error: el teléfono debe tener exactamente 9 dígitos numéricos. Intenta de nuevo.")

    paciente = Paciente(dni, nombres, apellidos, fecha_nacimiento, telefono)
    pacientes.append(paciente)
    print(f"Paciente registrado: {paciente}")
    print(f"Total de pacientes: {len(pacientes)}")

def registrar_medico():
    print("\n--- Registrar médico ---")

    while True:
        cmp = input("CMP (5 o 6 dígitos): ")
        if cmp.isdigit() and len(cmp) in (5, 6):
            break
        print("Error: el CMP debe tener 5 o 6 dígitos numéricos. Intenta de nuevo.")

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    especialidad = input("Especialidad: ")
    while True:
        telefono = input("Teléfono (9 dígitos): ")
        if len(telefono) == 9 and telefono.isdigit():
            break
        print("Error: el teléfono debe tener exactamente 9 dígitos numéricos. Intenta de nuevo.")

    medico = Medico(cmp, nombres, apellidos, especialidad, telefono)
    medicos.append(medico)
    print(f"Médico registrado: {medico}")
    print(f"Total de médicos: {len(medicos)}")

def elegir_de_lista(lista, titulo):
    print(f"\n{titulo}")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

    while True:
        eleccion = input("Elige un número: ")
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(lista):
            return lista[int(eleccion) - 1]
        print("Error: elige un número de la lista. Intenta de nuevo.")

def registrar_cita():
    print("\n--- Registrar cita ---")

    if len(pacientes) == 0:
        print("Primero debes registrar al menos un paciente.")
        return
    if len(medicos) == 0:
        print("Primero debes registrar al menos un médico.")
        return

    paciente = elegir_de_lista(pacientes, "Pacientes registrados:")
    medico = elegir_de_lista(medicos, "Médicos registrados:")
    fecha = input("Fecha (AAAA-MM-DD): ")
    hora = input("Hora (HH:MM): ")
    motivo = input("Motivo de la consulta: ")

    cita = Cita(paciente, medico, fecha, hora, motivo)
    citas.append(cita)
    print("\nCita registrada:")
    print(cita)
    print(f"Total de citas: {len(citas)}")

def ver_citas():
    print("\n--- Lista de citas ---")

    if len(citas) == 0:
        print("Todavía no hay citas registradas.")
        return

    for i, cita in enumerate(citas, start=1):
        print(f"\nCita {i}")
        print(cita)

    print(f"\nTotal de citas: {len(citas)}")

def cambiar_estado_cita():
    print("\n--- Cambiar estado de una cita ---")

    if len(citas) == 0:
        print("Todavía no hay citas registradas.")
        return

    cita = elegir_de_lista(citas, "Citas registradas:")
    print(f"\nEstado actual: {cita.estado}")
    print("1. pendiente")
    print("2. atendida")
    print("3. cancelada")

    while True:
        opcion = input("Elige el nuevo estado (1-3): ")
        match opcion:
            case "1":
                cita.estado = "pendiente"
                break
            case "2":
                cita.estado = "atendida"
                break
            case "3":
                cita.estado = "cancelada"
                break
            case _:
                print("Error: elige 1, 2 o 3. Intenta de nuevo.")

    print(f"Estado actualizado: {cita.estado}")

def buscar_persona_por_codigo():
    print("\n--- Buscar persona por código ---")
    print("1. Buscar paciente por DNI")
    print("2. Buscar médico por CMP")

    opcion = input("Selecciona el tipo de búsqueda: ")

    if opcion == "1":
        codigo = input("Ingrese el DNI del paciente: ")

        resultado = list(filter(
            lambda paciente: paciente.dni == codigo,
            pacientes
        ))

        if resultado:
            print("\nPaciente encontrado:")
            print(resultado[0])
            print(f"Fecha de nacimiento: {resultado[0].fecha_nacimiento}")
            print(f"Teléfono: {resultado[0].telefono}")
        else:
            print("No se encontró ningún paciente con ese DNI.")

    elif opcion == "2":
        codigo = input("Ingrese el CMP del médico: ")

        resultado = list(filter(
            lambda medico: medico.cmp == codigo,
            medicos
        ))

        if resultado:
            print("\nMédico encontrado:")
            print(resultado[0])
            print(f"Teléfono: {resultado[0].telefono}")
        else:
            print("No se encontró ningún médico con ese CMP.")

    else:
        print("Opción inválida.")

def buscar_medicos_por_especialidad():
    print("\n--- Buscar médicos por especialidad ---")

    if len(medicos) == 0:
        print("Todavía no hay médicos registrados.")
        return

    especialidad = input("Ingrese la especialidad que desea buscar: ")

    resultado = list(filter(
        lambda medico: medico.especialidad.lower() == especialidad.lower(),
        medicos
    ))

    if resultado:
        print(f"\nMédicos encontrados en {especialidad}:")

        for medico in resultado:
            print(f"\n{medico}")
            print(f"Teléfono: {medico.telefono}")

        print(f"\nTotal de médicos encontrados: {len(resultado)}")

    else:
        print(f"No se encontraron médicos de la especialidad: {especialidad}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                registrar_paciente()
            case "2":
                registrar_medico()
            case "3":
                registrar_cita()
            case "4":
                ver_citas()
            case "5":
                cambiar_estado_cita()
            case "6":
                buscar_persona_por_codigo()
            case "7":
                buscar_medicos_por_especialidad()
            case "8":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida, intenta de nuevo.")

main()