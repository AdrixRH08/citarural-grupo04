class Persona:
    def __init__(self, nombres, apellidos, telefono):
        self._nombres = nombres
        self._apellidos = apellidos
        self._telefono = None
        self.telefono = telefono  # pasa por el setter para validar

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

    # --- Teléfono ---
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if len(valor) == 9 and valor.isdigit():
            self._telefono = valor
        else:
            raise ValueError("El teléfono debe tener 9 dígitos numéricos.")

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"