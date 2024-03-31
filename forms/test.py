from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class TestForm(FlaskForm):
    title = StringField('Тема теста:', validators=[DataRequired()])
    quest = StringField('Вопрос:', validators=[DataRequired()])
    a_1 = StringField('Вариант ответа 1:')
    a_2 = StringField('Вариант ответа 2:')
    a_3 = StringField('Вариант ответа 3:')
    a_4 = StringField('Вариант ответа 4:')
    r_a = StringField('Содержание правильного ответа:')
    ball = IntegerField('Колличество баллов за тест:')
    submit = SubmitField('Добавить')
