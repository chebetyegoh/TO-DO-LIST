from flask import request, redirect, render_template, url_for, flash
from todolist import db,app
from todolist.models import Tasks

@app.route('/')
def home():
    todos = Tasks.query.all()
    return render_template('base.html', title='To Do List', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        todo = Tasks(task=request.form['task'], complete=False)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home')) 


@app.route('/delete/<int:task_id>', methods=['GET','POST'])
def delete_task(task_id):
    tasks = Tasks.query.get_or_404(task_id)
    db.session.delete(tasks)
    db.session.commit()
    return redirect(url_for('home'))
    