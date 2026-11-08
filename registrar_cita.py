class RegistrarCita:
    def __init__(self, paciente, medico, fecha, hora, motivo, estado="pendiente"):
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._hora = hora
        self._motivo = motivo
        self._estado = None
        self.estado = estado  # pasa por el setter para validar

    # --- Paciente ---
    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, valor):
        self._paciente = valor

    # --- Médico ---
    @property
    def medico(self):
        return self._medico

    @medico.setter
    def medico(self, valor):
        self._medico = valor

    # --- Fecha ---
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    # --- Hora ---
    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, valor):
        self._hora = valor

    # --- Motivo ---
    @property
    def motivo(self):
        return self._motivo

    @motivo.setter
    def motivo(self, valor):
        self._motivo = valor

    # --- Estado ---
    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        match valor:
            case "pendiente" | "atendida" | "cancelada":
                self._estado = valor
            case _:
                raise ValueError("Estado inválido. Use: pendiente, atendida o cancelada.")

    def __str__(self):
        return (
            f"Cita [{self.estado}] - {self.fecha} {self.hora}\n"
            f"  Paciente: {self.paciente}\n"
            f"  Médico: {self.medico}\n"
            f"  Motivo: {self.motivo}"
        )