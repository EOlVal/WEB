from flask import Flask, render_template, request, redirect, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data import db_session
from data.users import User
from data.tests import Tests
from data.results import Results
from forms.user import RegisterForm
from forms.login import LoginForm
from forms.test import TestForm
import datetime

app = Flask(__name__)
app.debug = False

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
y_or_n = ""
cur_sh = 0


def main():
    db_session.global_init("db/blogs.db")

    @login_manager.user_loader
    def load_user(user_id):
        db_sess = db_session.create_session()
        return db_sess.query(User).get(user_id)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/all_tests")
    def all_tests():
        db_sess = db_session.create_session()
        user = db_sess.query(User)
        global y_or_n, cur_sh
        if cur_sh == 0:
            y_or_n = 'Нет'
        db_sess = db_session.create_session()
        tests = db_sess.query(Tests)

        return render_template("all_tests.html", tests=tests, y_or_n=y_or_n, user=user)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            user = db_sess.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect("/")
            return render_template('login.html',
                                   message="Неправильный логин или пароль",
                                   form=form)
        return render_template('login.html', title='Авторизация', form=form)

    @app.route('/rules', methods=['GET', 'POST'])
    def rules():
        return render_template('rules.html', title='Правила')

    @app.route('/p_s', methods=['GET', 'POST'])
    def p_s():
        return render_template('p_s.html', title='Present Simple')

    @app.route('/p_c', methods=['GET', 'POST'])
    def p_c():
        return render_template('p_c.html', title='Present Continuous')

    @app.route('/current_test/<test_id>', methods=['GET', 'POST'])
    def current_test(test_id):
        global y_or_n, cur_sh
        db_sess = db_session.create_session()
        tests = db_sess.query(Tests).filter(test_id == Tests.id)

        if request.method == 'GET':
            return render_template('current_test.html', tests=tests, title='Test')

        elif request.method == 'POST':
            for item in tests:
                if request.form['answer'] == item.r_a:
                    cur_sh = 1
                    y_or_n = 'Верно'
                    results = Results(result=item.ball, date=datetime.datetime.now(), user_id=current_user.id,
                                      test_id=item.id)
                    db_sess.add(results)
                    db_sess.commit()
                    return render_template("index.html", tests=tests, y_or_n=y_or_n)
                else:
                    y_or_n = 'Неверно'
                    return render_template("index.html", tests=tests, y_or_n=y_or_n)

            return render_template("index.html", tests=tests, y_or_n="Нет")

    @app.route('/result', methods=['GET', 'POST'])
    def result():
        db_sess = db_session.create_session()
        results = db_sess.query(Results).filter(current_user.id == Results.user_id)
        ball = 0
        tests_kol = []
        date = []
        for i in results:
            ball += i.result
            tests_kol.append(i.id)
            date.append(f'{i.date}')
        date_res = date[-1]
        kol = tests_kol[-1]
        return render_template('result.html', results=results, ball=ball, kol=kol, date_res=date_res)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect("/")

    @app.route('/news', methods=['GET', 'POST'])
    @login_required
    def add_news():
        form = TestForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            tests = Tests(title=form.title.data, quest=form.quest.data, a_1=form.a_1.data,
                          a_2=form.a_2.data, a_3=form.a_3.data, a_4=form.a_4.data,
                          r_a=form.r_a.data, ball=form.ball.data)
            db_sess.add(tests)
            db_sess.commit()
            return redirect('/')
        return render_template('news.html', title='Добавление теста',
                               form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def reqister():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Пароли не совпадают")
            db_sess = db_session.create_session()
            if db_sess.query(User).filter(User.email == form.email.data).first():
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Такой пользователь уже есть")
            user = User(
                name=form.name.data,
                email=form.email.data,
                about=form.about.data,
                status=1
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            return redirect('/login')
        return render_template('register.html', title='Регистрация', form=form)

    app.run()


if __name__ == '__main__':
    main()
