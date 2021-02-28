from app_package import app, db
from flask import render_template, request, Markup, flash, redirect, url_for

from app_package.models import Task

title = "No title"

@app.route('/',methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    title = "Index"
    tasks = Task.query.order_by(Task.date_added).all()
    if request.method == 'POST':
        name = request.form['task_name']
        task = Task(name=name)
        try:
            db.session.add(task)
            db.session.commit()
        except Exception as e:
            message = Markup(f"Error adding new task: {e}")
            flash(message)
        finally:
            return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks, title=title)

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
    title = "Updating Page"
    target_task = Task.query.get_or_404(id)
    if request.method == 'POST':
        try:
            target_task.name = request.form['task_name']
            db.session.commit()
        except Exception as e:
            message = Markup(f"Error updating task: {e}")
            flash(message)
        return redirect(url_for('index'))
    return render_template('update.html', task=target_task, title=title)

@app.route('/login')
def login():
    pass




