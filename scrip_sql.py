import sqlite3


def conexion_db():
    try:
        conn = sqlite3.connect('database.db')
        return conn
    except:
        print("Error in conection to databse")

def select_room():
    query = "SELECT habitaciones.id, habitaciones.ubicacion, user.name, user.last_name \
        FROM habitaciones \
        INNER JOIN administrador \
        ON habitaciones.id_administrador=administrador.id \
        INNER JOIN user \
        ON administrador.id=user.id \
        ORDER BY habitaciones.id;"
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query)
    rooms = cursor.fetchall()
    return rooms

def insert_room(room):
    """Insert room in table habitaciones"""
    query = "INSERT INTO habitaciones (ubicacion, id_administrador) \
        VALUES ('{}', {});".format(room['ubicacion'], room['id_administrador'])
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    conexion.close()

def insert_user(user):
    """Insert user to table"""
    query = "INSERT INTO user (identificacion, name, last_name, Email, password) \
        VALUES ('{}', '{}', '{}', '{}', '{}');".format(user['identificacion'],
        user['name'], user['last_name'], user['email'], user['password'])
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    conexion.close()

def select_users():
    """Select all users"""
    query = "SELECT final_user.id_user, user.identificacion, user.Name, user.last_name, user.Email \
            FROM final_user \
            INNER JOIN user \
            ON final_user.id_user=user.id;"
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query)
    rooms = cursor.fetchall()
    return rooms

def select_administradores():
    """Selecy Administradores by table"""
    query = "SELECT administrador.id, user.identificacion, user.name, user.last_name, user.Email \
            FROM administrador \
            INNER JOIN user ON administrador.id_user=user.id;"
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query)
    adminds = cursor.fetchall()
    return adminds

def select_one_user(name, last_name, identificacion):
    """Select only one user"""
    query = "SELECT id FROM user \
            WHERE identificacion='{}' \
            AND name='{}' \
            AND last_name='{}';".format(identificacion, name, last_name)
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query)
    id = cursor.fetchall()
    return id

def insert_final_user(id):
    """Insert final user"""
    query = "INSERT INTO final_user(id_user, id_administrador, id_superadministrador) \
            VALUES ({}, {}, {});".format(id, 1, 2)
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    conexion.close()

def insert_admind(id):
    """Insert administrador"""
    query = "INSERT INTO administrador (id_user, id_superadministrador) \
            VALUES ({}, {});".format(id, 1)
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    conexion.close()
