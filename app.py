from crypt import methods
from flask import Flask, render_template, request, redirect
import scrip_sql


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/experiences/')
def experiences():
    return render_template('experiences.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/alojamiento/', methods=['GET', 'POST'])
def alojamiento():
    rooms = scrip_sql.select_room()
    return render_template('base.html', rooms=rooms)

@app.route('/reserva/', methods=['GET', 'POST'])
def reserva():
    return render_template('reserva.html')

@app.route('/usuarios/', methods=['GET', 'POST'])
def usuarios():
    users = scrip_sql.select_users()
    return render_template('usuarios.html', users=users)

@app.route('/administradores/', methods=['GET', 'POST'])
def administradores():
    adminds = scrip_sql.select_administradores()
    return render_template('administradores.html', adminds=adminds)


@app.route('/crear_user/', methods=['POST'])
def crear_user():
    user = request.form.to_dict()
    check = 0
    for key, value in user.items():
        if value == '':
            check = 1
    if check == 0:
        scrip_sql.insert_user(user=user)
        id = scrip_sql.select_one_user(user['name'],
                                  user['last_name'],
                                  user['identificacion'])
        id = id[0][0]
        scrip_sql.insert_final_user(id)
    return redirect('/usuarios/')

@app.route("/crear_room/", methods=['POST'])
def crear_room():
    new_room = request.form.to_dict()
    check = 0
    for key, value in new_room.items():
        if value == '':
            check = 1
    if check == 0:
        scrip_sql.insert_room(new_room)
    return redirect('/alojamiento/')

@app.route('/crear_admind/', methods=['POST'])
def crear_admind():
    admind = request.form.to_dict()
    check = 0
    for key, value in admind.items():
        if value == '':
            check = 1
    if check == 0:
        scrip_sql.insert_user(admind)
        id = scrip_sql.select_one_user(admind['name'],
                                  admind['last_name'],
                                  admind['identificacion'])
        id = id[0][0]
        scrip_sql.insert_admind(id)
    return redirect('/administradores/')

@app.route('/delete_room/', methods=['POST'])
def delete():
    room = request.form.to_dict()
    print(room)
    return redirect('/alojamiento/')
