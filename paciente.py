class Paciente:
    def __init__(self, dni, nombres, apellidos, fecha_nacimiento, telefono):
        self._dni = None
        self._nombres = nombres
        self._apellidos = apellidos
        self._fecha_nacimiento = fecha_nacimiento
        self._telefono = telefono
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

    # --- Nombres ---
    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, valor):
        self._nombres = valor

    # --- Apellidos ---
    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self._apellidos = valor

    # --- Fecha de nacimiento ---
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor):
        self._fecha_nacimiento = valor

    # --- Teléfono ---
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    def __str__(self):
        return f"{self.nombres} {self.apellidos} (DNI: {self.dni})"