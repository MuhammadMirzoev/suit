from data.jobs import Jobs
from flask import Flask, render_template
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

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

# Контакты
@app.route("/contacts")
def contact():
    session = db_session.create_session()
    menu = session.query(Jobs).all()
    return render_template('contacts.html')

def main():
    db_session.global_init("db/site_data.db")
    app.run()


if __name__ == '__main__':
    main()
