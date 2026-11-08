from persona import Persona


class Paciente(Persona):
    def __init__(self, dni, nombres, apellidos, fecha_nacimiento, telefono):
        Persona.__init__(self, nombres, apellidos, telefono)
        self._dni = None
        self._fecha_nacimiento = fecha_nacimiento
        self.dni = dni  # pasa por el setter para validar

    # --- DNI ---
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        if len(valor) == 8 and valor.isdigit():
            self._dni = valor
        else:
            raise ValueError("El DNI debe tener 8 dígitos numéricos.")

    # --- Fecha de nacimiento ---
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor):
        self._fecha_nacimiento = valor

    def __str__(self):
        return f"{self.nombres} {self.apellidos} (DNI: {self.dni})"