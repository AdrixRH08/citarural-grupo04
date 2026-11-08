from paciente import Paciente
from medico import Medico
from registrar_cita import RegistrarCita

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
    print("5. Salir")

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
                print("Registrar cita (pendiente)")
            case "4":
                print("Ver citas (pendiente)")
            case "5":
                print("Hasta luego")
                break
            case _:
                print("Opción inválida, intenta de nuevo.")


main()