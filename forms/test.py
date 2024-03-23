from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class TestForm(FlaskForm):
    title = StringField('Название теста', validators=[DataRequired()])
    quest = StringField('Вопрос:', validators=[DataRequired()])
    a_1 = RadioField('Вариант ответа 1', validators=[DataRequired()])
    a_2 = RadioField('Вариант ответа 2', validators=[DataRequired()])
    a_3 = RadioField('Вариант ответа 3', validators=[DataRequired()])
    a_4 = RadioField('Вариант ответа 4', validators=[DataRequired()])
    r_a = StringField('Содержание правильного ответа', validators=[DataRequired()])
    ball = IntegerField('Колличество баллов за тест', validators=[DataRequired()])
    submit = SubmitField('Добавить')