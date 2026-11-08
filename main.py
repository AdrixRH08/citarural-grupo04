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


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                print("Registrar paciente (pendiente)")
            case "2":
                print("Registrar médico (pendiente)")
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