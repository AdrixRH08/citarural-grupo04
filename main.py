from paciente import Paciente
from medico import Medico
from registrar_cita import RegistrarCita

p1 = Paciente("12345678", "Rosa", "Quispe Huamán", "1990-05-14", "987654321")
m1 = Medico("45678", "Carlos", "Ramírez Soto", "Medicina General", "912345678")

cita1 = RegistrarCita(p1, m1, "2026-11-15", "09:30", "Control de rutina")
print(cita1)

cita1.estado = "atendida"
print(cita1.estado)

# cita1.estado = "perdida" (Colocarlo debería salir error)