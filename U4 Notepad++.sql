--Equipo:
--Abimael Guadarrama Medina
--Jesús Manuel Núñez Chávez
--Josué Sánchez Domínguez

--CREAR LA BASE DE DATOS
CREATE DATABASE CONTROLESCOLAR;

--CREAR LAS TABLAS CON TODAS LAS RESTRICCIONES DEFINIDAS.
CREATE TABLE LOGIN (
    numCuenta INT AUTO_INCREMENT NOT NULL,
    contrasena VARCHAR(255) NOT NULL DEFAULT "123",
    tipoUsuario ENUM('alumno', 'admin', 'prof') NOT NULL DEFAULT "alumno",
    PRIMARY KEY (numCuenta)
);

CREATE TABLE ALUMNO(
          nombreCompleto VARCHAR(100) NOT NULL,
          genero CHAR(1) NOT NULL DEFAULT 'M',
          nacionalidad VARCHAR(10) NOT NULL DEFAULT 'mexicana',
          curp CHAR(18) NOT NULL,
          fechaNac DATE NOT NULL,
          numCuenta INT NOT NULL,
          FOREIGN KEY (numCuenta) REFERENCES LOGIN(numCuenta) ON DELESTE CASCADE,
          UNIQUE (curp),
          CHECK (CHARACTER_LENGTH(curp) > 17)
     );


CREATE TABLE PROFESOR(
          nombreCompleto VARCHAR(100) NOT NULL,
          genero CHAR(1) NOT NULL DEFAULT 'M',
          nacionalidad VARCHAR(10) NOT NULL DEFAULT 'mexicana',
          curp CHAR(18) NOT NULL,
          fechaNac DATE NOT NULL,
          numCuenta INT NOT NULL,
          FOREIGN KEY (numCuenta) REFERENCES LOGIN(numCuenta) ON DELETE CASCADE,
          UNIQUE (curp),
          CHECK (CHARACTER_LENGTH(curp) > 17)
     );

CREATE TABLE ADMINISTRADOR(
          nombreCompleto VARCHAR(100) NOT NULL,
          genero CHAR(1) NOT NULL DEFAULT 'M',
          nacionalidad VARCHAR(10) NOT NULL DEFAULT 'mexicana',
          curp CHAR(18) NOT NULL,
          fechaNac DATE NOT NULL,
          numCuenta INT NOT NULL,
          FOREIGN KEY (numCuenta) REFERENCES LOGIN(numCuenta) ON DELETE CASCADE,
          UNIQUE (curp),
          CHECK (CHARACTER_LENGTH(curp) > 17)
     );

CREATE TABLE MATERIA (
    idMateria INT AUTO_INCREMENT NOT NULL,
    nombreMateria VARCHAR(50) NOT NULL DEFAULT 'Bases de datos avanzadas',
    fechaInicio DATE NOT NULL DEFAULT '2024-06-15',
    fechaFin DATE NOT NULL DEFAULT '2024-08-15',
    horarioInicio TIME NOT NULL DEFAULT '07:00:00',
    horarioFin TIME NOT NULL DEFAULT '14:00:00', 
    diaClase ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo') NOT NULL DEFAULT 'Lunes',
    PRIMARY KEY (idMateria),
    UNIQUE(nombreMateria, horarioInicio)
);

CREATE TABLE Grupos (
    idGrupo INT AUTO_INCREMENT PRIMARY KEY,
    nombreReferencia VARCHAR(250) NOT NULL,
    idMateria INT NOT NULL,
    idProfesor INT NOT NULL,
    FOREIGN KEY (idMateria) REFERENCES MATERIA(idMateria),
    FOREIGN KEY (idProfesor) REFERENCES PROFESOR(numCuenta),
    UNIQUE (nombreReferencia)
);

CREATE TABLE Grupos_Alumnos (
    idGrupo INT NOT NULL,
    idAlumno INT NOT NULL,
    PRIMARY KEY (idGrupo, idAlumno),
    FOREIGN KEY (idGrupo) REFERENCES Grupos(idGrupo),
    FOREIGN KEY (idAlumno) REFERENCES Alumno(numCuenta)
);

CREATE TABLE ALUMNO_CALIFICACION (
  idCalificacion INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  idGrupo INT NOT NULL,
  idAlumno INT NOT NULL,
  calificacion FLOAT NOT NULL DEFAULT 5.9,
  FOREIGN KEY (idGrupo) REFERENCES Grupos(idGrupo),
  FOREIGN KEY (idAlumno) REFERENCES ALUMNO(numCuenta),
  UNIQUE (idGrupo, idAlumno)
);

--INSERTAR AL MENOS CINCO REGISTROS EN CADA TABLA.
INSERT INTO LOGIN (tipoUsuario)
VALUES
    ('admin'), ('admin'), ('admin'), ('admin'), ('admin'),
    ('prof'), ('prof'), ('prof'), ('prof'), ('prof'),
    ('alumno'), ('alumno'), ('alumno'), ('alumno'), ('alumno');

INSERT INTO ADMINISTRADOR ()
VALUES
    ("María Martínez González", DEFAULT, DEFAULT, "MAMG980927MCMXRR06", "1989-09-27",1),
    ("Juan Martínez López", DEFAULT, DEFAULT, "JMLM940718HMCXRR07", "1994-07-18",2),
    ("Ana García Hernández", DEFAULT, DEFAULT, "AGHM900315MCMXRR08", "1990-03-15",3),
    ("Pedro Rodríguez Pérez", DEFAULT, DEFAULT, "PRPM960527HMCXRR09", "1996-05-27",4),
    ("Lucía Sánchez Martínez", DEFAULT, DEFAULT, "LSMM950320MCMXRR10", "1995-03-20",5);

INSERT INTO PROFESOR ()
VALUES
    ("María Rodríguez Sánchez", DEFAULT, DEFAULT, "ROSM971024MCMXRR04", "1997-10-24",6),
    ("Juan García López", DEFAULT, DEFAULT, "JGLM950708HMCXRR03", "1995-07-08",7),
    ("Ana Martínez Hernández", DEFAULT, DEFAULT, "AMHM930415MCMXRR02", "1993-04-15",8),
    ("Pedro López Pérez", DEFAULT, DEFAULT, "PLPM940527HMCXRR01", "1994-05-27",9),
    ("Lucía Sánchez García", DEFAULT, DEFAULT, "LSGM980320MCMXRR05", "1998-03-20",10);


INSERT INTO ALUMNO ()
VALUES
    ("Jose Sanchez Domínguez", DEFAULT, DEFAULT, "JOSJ030113HMCNMSA6", "2003-12-12",11),
    ("Jeremías Perez Quintos", DEFAULT, DEFAULT, "JERJ030113HMCNMSA6", "2000-01-01",12),
    ("Francisco Hernandez Cortés", DEFAULT, DEFAULT, "FRAJ030113HMCNMSA6", "1998-05-20",13),
    ("Rodolfo Perez Castro", DEFAULT, DEFAULT, "RODJ030113HMCNMSA6", "2002-09-15",14),
    ("Emilia Bobadilla Quintanilla", DEFAULT, DEFAULT, "EMIJ030113HMCNMSA6", "2005-03-10",15);

INSERT INTO MATERIA ()
VALUES
    (NULL,'Base de datos', '2024-06-15', '2024-08-15', '07:00:00', '14:00:00', 'Lunes'),
    (NULL,'Seguridad Informática', '2024-06-20', '2024-08-20', '09:00:00', '16:00:00', 'Martes'),
    (NULL,'Matemáticas Discretas', '2024-06-25', '2024-08-25', '11:00:00', '18:00:00', 'Miércoles'),
    (NULL,'Base de datos', '2024-07-01', '2024-08-01', '13:00:00', '20:00:00', 'Jueves'),
    (NULL,'Seguridad Informática', '2024-07-05', '2024-08-05', '15:00:00', '22:00:00', 'Viernes');

INSERT INTO Grupos () 
VALUES
    (NULL, 'Grupo 1', 1, 6),
    (NULL,'Grupo 2', 2, 7),
    (NULL,'Grupo 3', 3, 8),
    (NULL,'Grupo 4', 4, 9),
    (NULL,'Grupo 5', 5, 10);

INSERT INTO Grupos_Alumnos () 
VALUES
    (1, 11),
    (1, 12),
    (2, 13),
    (2, 11),
    (3, 15);

INSERT INTO ALUMNO_CALIFICACION () 
VALUES
    (NULL, 1, 11, 8.5),
    (NULL, 1, 12, 7.9),
    (NULL, 2, 13, 6.5),
    (NULL, 2, 14, 9.2),
    (NULL, 3, 15, 8.0);
	
	
--AL MENOS CINCO EJEMPLOS DE CONSULTAS ÚTILES PARA EL CLIENTE.

SELECT tipoUsuario FROM LOGIN WHERE numCuenta = 15 AND contrasena = 123;

SELECT * FROM ALUMNO ORDER BY numCuenta;

SELECT * FROM ALUMNO WHERE NUMCUENTA = 14;

SELECT * FROM ALUMNO WHERE curp = "SADJ030113HMCNMSA6";

SELECT nombreCompleto, genero, nacionalidad, CURP, fechaNac FROM alumno WHERE numCuenta = 14;

SELECT * FROM PROFESOR ORDER BY numCuenta;

SELECT nombreCompleto, genero, nacionalidad, CURP, fechaNac FROM profesor WHERE numCuenta = 6;

SELECT * FROM grupos_alumnos WHERE idGrupo = 5 AND idAlumno = 11;

SELECT * FROM ADMINISTRADOR ORDER BY numCuenta;

SELECT * FROM ADMINISTRADOR WHERE NUMCUENTA = 4;

SELECT * FROM GRUPOS ORDER BY idGrupo;

SELECT * FROM GRUPOS WHERE nombreReferencia = "Grupo 1";

SELECT nombreReferencia, idMateria FROM GRUPOS WHERE idGrupo = 1;

SELECT M.nombreMateria AS NombreMateria,AC.idAlumno AS IDAlumno,A.nombreCompleto AS NombreAlumno,AC.calificacion AS Calificacion 
    FROM ALUMNO_CALIFICACION AC 
    JOIN ALUMNO A ON AC.idAlumno = A.numCuenta 
    JOIN Grupos G ON AC.idGrupo = G.idGrupo 
    JOIN MATERIA M ON G.idMateria = M.idMateria 
    WHERE AC.idAlumno = 11;

SELECT GA.idGrupo, A.nombreCompleto
    FROM Grupos_Alumnos GA
    JOIN ALUMNO A ON GA.idAlumno = A.numCuenta;

SELECT GA.idGrupo, A.numCuenta, A.nombreCompleto 
    FROM Grupos_Alumnos GA 
    JOIN ALUMNO A ON GA.idAlumno = A.numCuenta 
    WHERE GA.idGrupo = 1;

SELECT GA.idGrupo, A.numCuenta, A.nombreCompleto 
    FROM Grupos_Alumnos GA 
    JOIN ALUMNO A ON GA.idAlumno = A.numCuenta;

SELECT * FROM MATERIA WHERE nombreMateria = "Seguridad informatica";


	
	