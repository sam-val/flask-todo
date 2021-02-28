from app_package import app, db
from flask import render_template, request, Markup, flash, redirect, url_for

from app_package.models import Task
from app_package.forms import TaskForm
title = "No title"

@app.route('/',methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = TaskForm()
    title = "Index"
    tasks = Task.query.order_by(Task.date_added).all()
    if form.validate_on_submit():
        name = form.name.data
        task = Task(name=name)
        try:
            db.session.add(task)
            db.session.commit()
        except Exception as e:
            message = Markup(f"Error adding new task: {e}")
            flash(message)
        finally:
            return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks, title=title, form=form)

@app.route('/delete/<int:id>')
def delete(id):
    target_task = Task.query.get_or_404(id)
    try:
        db.session.delete(target_task)
        db.session.commit()
    except Exception as e:
        message = Markup(f"Error deleting task: {e}")
        flash(message)

    return redirect(url_for('index'))
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    form = TaskForm()
    title = "Updating Page"
    target_task = Task.query.get_or_404(id)
    if form.validate_on_submit():
        try:
            # target_task.name = request.form['task_name']
            target_task.name = form.name.data 
            db.session.commit()
        except Exception as e:
            message = Markup(f"Error updating task: {e}")
            flash(message)
        return redirect(url_for('index'))
    return render_template('update.html', task=target_task, title=title, form=form)

@app.route('/login')
def login():
    pass

