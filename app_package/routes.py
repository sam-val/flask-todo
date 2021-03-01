from app_package import app, db
from flask import render_template, request, Markup, flash, redirect, url_for
from flask_login import login_required, logout_user, login_user, current_user
from app_package.models import Task, User
from app_package.forms import TaskForm, LoginForm
title = "No title"

@app.route('/',methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    form = TaskForm()
    title = "Index"
    tasks = current_user.tasks.order_by(Task.date_added).all()
    if form.validate_on_submit():
        name = form.name.data
        task = Task(name=name, user_id=current_user.id)
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

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    title = "Login Page"
    if form.validate_on_submit():
        try: 
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                message = Markup(f"Invalid Username or Password.")
                flash(message)
                return redirect(url_for('login'))
            else:
                login_user(user=user, remember=form.remember_me.data)
                return redirect(url_for('index'))
        except Exception as e:
            message = Markup(f"Error updating task: {e}")
            flash(message)
            return redirect(url_for('login'))
    
    return render_template("login.html", title=title, form=form) 

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
