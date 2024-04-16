from evento import Evento

class examen (Evento):
    def __init__(self, fecha, descripcion, asignatura):
        super().__init__(fecha, descripcion)
        self.asignatura = asignatura

    def __str__(self):
        return f"{super().__str__()} - Examen de {self.materia}"

class TrabajoPractico(Evento):
    def __init__(self, fecha, descripcion, asignatura):
        super().__init__(fecha, descripcion)
        self.asignatura = asignatura

    def __str__(self):
        return f"{super().__str__()} - Trabajo práctico de {self.asignatura}"

class ReunionEstudio(Evento):
    def __init__(self, fecha, descripcion, lugar):
        super().__init__(fecha, descripcion)
        self.lugar = lugar

    def __str__(self):
        return f"{super().__str__()} - Reunión de estudio en {self.lugar}"
