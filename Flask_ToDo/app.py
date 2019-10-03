from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dbsetup.connect import flaskConfig

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = flaskConfig("todo")

db = SQLAlchemy(app)


class Todo(db.Model):
    """docstring for Todo"""
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    return render_template('index.html', incomplete=incomplete, complete=complete)


@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/undo/<id>')
def undo(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = False
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/clear')
def clear():
    clean = Todo.query.filter_by(complete=True).all()
    for n in clean:
        db.session.delete(n)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
