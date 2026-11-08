class Medico:
    def __init__(self, cmp, nombres, apellidos, especialidad, telefono):
        self._cmp = None
        self._nombres = nombres
        self._apellidos = apellidos
        self._especialidad = especialidad
        self._telefono = None
        self.telefono = telefono
        self.cmp = cmp  # pasa por el setter para validar

    # --- CMP ---
    @property
    def cmp(self):
        return self._cmp

    @cmp.setter
    def cmp(self, valor):
        if valor.isdigit() and len(valor) in (5, 6):
            self._cmp = valor
        else:
            raise ValueError("El CMP debe tener 5 o 6 dígitos numéricos.")

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

    # --- Especialidad ---
    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor

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
        return f"Dr(a). {self.nombres} {self.apellidos} - {self.especialidad} (CMP: {self.cmp})"