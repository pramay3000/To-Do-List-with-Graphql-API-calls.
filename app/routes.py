# app/routes.py
from flask import render_template
import app
from app.forms import AddTaskForm, DeleteTaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

@app.route('/', methods=['GET', 'POST'])
def index():
    add_task_form = AddTaskForm()
    delete_task_form = DeleteTaskForm()

    if add_task_form.validate_on_submit():
        # Logic to handle adding task
        pass

    if delete_task_form.validate_on_submit():
        # Logic to handle deleting task
        pass

    return render_template('index.html', add_task_form=add_task_form, delete_task_form=delete_task_form)
