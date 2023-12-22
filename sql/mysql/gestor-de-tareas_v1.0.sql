-- Active: 1703272465031@@127.0.0.1@3306@gestordetareas

CREATE DATABASE gestordetareas;

use gestordetareas;

-- ----------------------
-- Creación de Tablas
-- ----------------------

CREATE TABLE Usuario(
    username VARCHAR(40) PRIMARY KEY,
    nombre VARCHAR(60) NOT NULL,
    userpassword VARCHAR(60) NOT NULL,
    genero VARCHAR(20),
    telefono VARCHAR(10),
    email VARCHAR(40)
);

CREATE TABLE Clasificacion(
    idCl SERIAL PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(120) NOT NULL
);

CREATE TABLE Proyecto(
    idP SERIAL PRIMARY KEY,
    username VARCHAR(40) NOT NULL, 
    nombre VARCHAR(40) NOT NULL,
    estado VARCHAR(15) NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    fechaCreacion DATE NOT NULL,
    CONSTRAINT fk_proyecto_usuario
    FOREIGN KEY (username) REFERENCES Usuario(username)
);
drop TABLE proyecto;
CREATE TABLE Tarea (
    idT SERIAL PRIMARY KEY,
    username VARCHAR(60) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(150) NOT NULL,
    prioridad VARCHAR(20) NOT NULL,
    idP BIGINT UNSIGNED NOT NULL, #solo funciona si es bigint usigned, no int ni integer 
    idCl INTEGER NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    CONSTRAINT fk_tarea_usuario
    FOREIGN KEY (username) REFERENCES Usuario(username),
    CONSTRAINT fk_tarea_proyecto
    FOREIGN KEY (idP) REFERENCES Proyecto(idP)
);
drop Table tarea;

CREATE TABLE Comentario(
    idC SERIAL PRIMARY KEY,
    username VARCHAR(40) not NULL,
    idT BIGINT UNSIGNED NOT NULL,  #solo funciona si es bigint usigned, no int ni integer 
    descripcion VARCHAR(150) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT fk_comentario_usuario
    FOREIGN KEY (username) REFERENCES Usuario(username),
    CONSTRAINT fk_comentario_tarea
    FOREIGN KEY (idT) REFERENCES Tarea(idT)
);


-- ----------------------
-- Inserción de Datos
-- ----------------------
INSERT INTO Usuario(username, nombre, userpassword, genero, telefono, email) 
VALUES('mudis', 'martin', 'Kazooie10', 'masculino', '4571054513', 'martin25180@rocketmail.com');

INSERT INTO Clasificacion(nombre, descripcion)
VALUES('Ejemplo clasificacion', 'Este es un ejemplo para la bd sobre clasificaicion')

INSERT INTO Proyecto(username, nombre, estado, descripcion, fechacreacion)
VALUES ('mudis', 'Proyecto quimera', 'Iniciado', 'Este proyecto es para crear una quimera Bv', now())


INSERT INTO Tarea(username, nombre, descripcion, prioridad, idP, idCl, fecha_inicio, fecha_fin)
VALUES ('mudis', 'primer tarea', 'Ejemplo de tarea', 'baja', 1, 1, '2023-01-01', '2023-01-10');


INSERT INTO Comentario(username, idT, descripcion, fecha)
VALUES('mudis', '1', 'Esta tarea ta muy rara >:V', now());


-- ----------------------
-- Modificación de Datos
-- ----------------------

UPDATE ...

-- ----------------------
-- Eliminación de Datos
-- ----------------------

DELETE FROM ...

-- ----------------------
-- Eliminación de Tablas
-- ----------------------

DROP TABLE Usuario;
DROP TABLE clasificacion;
DROP TABLE Tarea;
DROP TABLE Proyecto;
DROP TABLE Comentario;
