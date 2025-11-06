from . import db
from datetime import datetime

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    completado = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Tarea {self.titulo}>'
