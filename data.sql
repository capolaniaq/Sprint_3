DROP TABLE IF EXISTS user;

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	identificacion VARCHAR(45),
	Name VARCHAR(45),
	last_name varchar(45),
	Email VARCHAR(45),
	password VARCHAR(45)
);

DROP TABLE IF EXISTS superadministrador;

CREATE TABLE superadministrador(
	id_user INTEGER,
	FOREIGN KEY(id_user) REFERENCES user(id)
);

DROP TABLE IF EXISTS administrador;

CREATE TABLE administrador (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER,
    id_superadministrador INTEGER,
    FOREIGN KEY(id_user) REFERENCES user(id),
    FOREIGN KEY(id_superadministrador) REFERENCES superadministrador(id)
);

DROP TABLE IF EXISTS final_user;

CREATE TABLE final_user (
	id_user INTEGER PRIMARY KEY AUTOINCREMENT,
	id_administrador INT,
	id_superadministrador INT,
	FOREIGN KEY (id_user) REFERENCES user(id),
	FOREIGN KEY (id_administrador) REFERENCES administrador (id),
	FOREIGN KEY (id_superadministrador) REFERENCES superadministrador (id)
);

DROP TABLE IF EXISTS payment;

CREATE TABLE payment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    metodo VARCHAR(45)
);

DROP TABLE IF EXISTS reservation;

CREATE TABLE reservation (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_payment INTEGER,
    id_user    INTEGER,
    FOREIGN KEY (id_payment) REFERENCES payment (id),
    FOREIGN KEY (id_user) REFERENCES final_user (id)
);

DROP TABLE IF EXISTS habitaciones;

CREATE TABLE habitaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ubicacion VARCHAR(45),
    id_administrador INTEGER,
    id_reservation INTEGER,
    id_payment INTEGER,
    id_user INTEGER,
    FOREIGN KEY(id_administrador) REFERENCES administrador(id),
    FOREIGN KEY(id_reservation) REFERENCES reservation(id),
    FOREIGN KEY(id_payment) REFERENCES payment(id),
    FOREIGN KEY(id_user) REFERENCES final_user(id)
);

INSERT INTO user (identificacion, name, last_name, Email, password) VALUES ('1026291584', 'Carlos', 'Polania', 'capolaniaq@correo.udistrital.edu.co', 'ca82882828');
INSERT INTO user (identificacion, name, last_name, Email, password) VALUES ('12123453', 'Andres', 'Willinton', 'awillinton@gmail.com', 'va82882828');
INSERT INTO user (identificacion, name, last_name, Email, password) VALUES ('12234321', 'Cristian', 'Polania', 'cpolania@gmail.com', '12345678');
INSERT INTO user (identificacion, name, last_name, Email, password) VALUES ('12234321', 'edgar', 'Polania', 'epolaniachavez@gmail.com', '12345678');
INSERT INTO user (identificacion, name, last_name, Email, password) VALUES ('12234321', 'marly', 'Gaitan', 'marlygaitan@outblock.com', '12345678');
INSERT INTO user (identificacion, name, last_name, Email, password) VALUES ('12234321', 'Cristian', 'Polania', 'cpolania@gmail.com', '12345678');

INSERT INTO superadministrador (id_user) VALUES (1);
INSERT INTO superadministrador (id_user) VALUES (2);

INSERT INTO administrador (id, id_user, id_superadministrador) VALUES (1, 3, 1);
INSERT INTO administrador (id, id_user, id_superadministrador) VALUES (2, 4, 1);

INSERT INTO final_user (id_user, id_administrador, id_superadministrador) VALUES (5, 1, 1);
INSERT INTO final_user (id_user, id_administrador, id_superadministrador) VALUES (6, 1, 1);

INSERT INTO payment (id, metodo) VALUES (1, 'NEQUI');
INSERT INTO payment (id, metodo) VALUES (2, 'PAYPALL');
INSERT INTO payment (id, metodo) VALUES (3, 'EFECTIVO');

INSERT INTO reservation (id, id_payment, id_user) VALUES (1, 1, 1);
INSERT INTO reservation (id, id_payment, id_user) VALUES (2, 1, 2);
INSERT INTO reservation (id, id_payment, id_user) VALUES (3, 2, 1);

INSERT INTO habitaciones (id, ubicacion, id_administrador) VALUES (1, 'BOGOTA', 1);
INSERT INTO habitaciones (id, ubicacion, id_administrador) VALUES (2, 'LA CALERA', 1);
INSERT INTO habitaciones (id, ubicacion, id_administrador) VALUES (3, 'CALI', 1);
INSERT INTO habitaciones (id, ubicacion, id_administrador) VALUES (4, 'MEDELLIN', 2);