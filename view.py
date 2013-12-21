from flask import Flask, request, flash, url_for, redirect, render_template, abort,session
from functools import wraps
from blog.blogapp import app
from blog.data import Todo,db

@app.route('/')
def index():
    return render_template('index.html',
        todos=Todo.query.order_by(Todo.pub_date.desc()).all()
    )


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logged = session.get('logged_in', None)
        if not logged:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != "admin":
            error = 'Invalid username'
        elif request.form['password'] != "blog":
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
def new():
    if request.method == 'POST':
            todo = Todo(request.form['title'], request.form['text'])
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('new.html')





@app.route('/todos/<int:todo_id>', methods = ['GET' , 'POST'])
def show_or_update(todo_id):
    todo_item = Todo.query.get(todo_id)
    if request.method == 'GET':
        return render_template('view.html',todo=todo_item)
    todo_item.title = request.form['title']
    todo_item.text  = request.form['text']
    todo_item.done  = ('done.%d' % todo_id) in request.form
    db.session.commit()
    return redirect(url_for('index'))
