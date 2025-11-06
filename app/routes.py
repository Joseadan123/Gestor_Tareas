from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Tarea

main = Blueprint('main', __name__)

@main.route('/')
def home():
    tareas = Tarea.query.order_by(Tarea.fecha_creacion.desc()).all()
    total = len(tareas)
    completadas = len([t for t in tareas if t.completado])
    return render_template('index.html', tareas=tareas, total=total, completadas=completadas)

@main.route('/agregar', methods=['POST'])
def agregar():
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')

    if titulo:
        nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion)
        db.session.add(nueva_tarea)
        db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/completar/<int:id>')
def completar(id):
    tarea = Tarea.query.get_or_404(id)
    tarea.completado = not tarea.completado
    db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/eliminar/<int:id>')
def eliminar(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('main.home'))
