class Evento:
    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.fecha}: {self.descripcion}"