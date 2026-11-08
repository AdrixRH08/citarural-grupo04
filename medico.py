from persona import Persona


class Medico(Persona):
    def __init__(self, cmp, nombres, apellidos, especialidad, telefono):
        Persona.__init__(self, nombres, apellidos, telefono)
        self._cmp = None
        self._especialidad = especialidad
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

    # --- Especialidad ---
    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor

    def __str__(self):
        return f"Dr(a). {self.nombres} {self.apellidos} - {self.especialidad} (CMP: {self.cmp})"