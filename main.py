from data.jobs import Jobs
from flask import Flask, render_template, request, redirect
from data import db_session
from data.users import User
from flask_sqlalchemy import SQLAlchemy
from time import sleep

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

images = [
    {
        'url': 'static/img/alien_1.png',
        'alt': 'Картинка 1',
        'caption': 'Описание первой картинки'
    },
    {
        'url': 'static/img/alien_2.jpg',
        'alt': 'Картинка 2',
        'caption': 'Описание второй картинки'
    },
    {
        'url': 'static/img/VECTOR.png',
        'alt': 'Картинка 3',
        'caption': 'Описание третьей картинки'
    }
]


# О ВЫСТАВКЕ
@app.route("/")
@app.route("/index")
@app.route("/about")
def index():
    session = db_session.create_session()
    menu = session.query(Jobs).all()
    return render_template("index.html")


# ДЕЛОВАЯ ПРОГРАММА
@app.route("/work_program")
def work_program():
    session = db_session.create_session()
    menu = session.query(Jobs).all()
    return render_template("work_program.html")


# ЭКСПОНЕНТЫ
@app.route("/exponents")
def exponents():
    session = db_session.create_session()
    menu = session.query(Jobs).all()
    return render_template("exponents.html")


# Фотогалерея
@app.route("/photos")
def photo():
    session = db_session.create_session()
    menu = session.query(Jobs).all()
    return render_template('gallery.html', images=images)

    # Программа


@app.route("/program")
def program():
    session = db_session.create_session()
    menu = session.query(Jobs).all()
    return render_template('program.html')


from flask import Flask, request, render_template
import smtplib
import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('contacts.db')


# Контакты
@app.route("/contacts")
def contact():
    session = db_session.create_session()
    menu = session.query(Jobs).all()
    return render_template('contacts.html')


@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Сохраняем данные в базу данных
    connection = sqlite3.connect('instance/contacts.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO ask (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    connection.commit()
    connection.close()

    def delayed(self):
        sleep(3)

    return """<h1>Ваша заявка будет рассмотрена в скором времени</h1>
    <input type="button" onclick="history.back();" value="Назад"/>"""

# Закрываем подключение к базе данных в конце программы
conn.close()


def main():
    db_session.global_init("db/site_data.db")
    app.run()


if __name__ == '__main__':
    main()
