#coding:utf-8
from flask import request, flash, url_for, redirect, render_template, abort, session
from functools import wraps
import os
import secrets
from blogapp import app, db, Todo

ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'blog')


def csrf_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method in ('POST', 'PUT', 'DELETE', 'PATCH'):
            token = session.get('csrf_token')
            if not token or token != request.form.get('csrf_token'):
                abort(403)
        return f(*args, **kwargs)
    return decorated_function


@app.before_request
def generate_csrf_token():
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(16)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    todos = db.session.execute(
        db.select(Todo).order_by(Todo.pub_date.desc())
    ).scalars().all()
    return render_template('index.html', todos=todos)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        token = session.get('csrf_token')
        if not token or token != request.form.get('csrf_token'):
            abort(403)
        if request.form['username'] != ADMIN_USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != ADMIN_PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('new'))
        flash(error)
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('index'))


@app.route('/new', methods=['GET', 'POST'])
@login_required
@csrf_required
def new():
    if request.method == 'POST':
        todo = Todo(request.form['title'], request.form['text'])
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html')


@app.route('/todos/<int:todo_id>', methods=['GET', 'POST'])
@login_required
@csrf_required
def show_or_update(todo_id):
    todo_item = db.get_or_404(Todo, todo_id)
    if request.method == 'GET':
        return render_template('view.html', todo=todo_item)
    todo_item.title = request.form['title']
    todo_item.text = request.form['text']
    todo_item.done = ('done.%d' % todo_id) in request.form
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/todos/<int:todo_id>/delete', methods=['POST'])
@login_required
@csrf_required
def delete_todo(todo_id):
    todo_item = db.get_or_404(Todo, todo_id)
    db.session.delete(todo_item)
    db.session.commit()
    flash('Todo deleted successfully.')
    return redirect(url_for('index'))
