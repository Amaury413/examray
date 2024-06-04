CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    contraseña VARCHAR(100),
);

CREATE TABLE Tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    descripcion TEXT,
    estado VARCHAR(50),
    fecha_creacion DATE,
    fecha_limite DATE,
    id_usuario INT,
    id_proyecto INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id)
);

-- CREATE TABLE Proyectos (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     nombre VARCHAR(100),
--     descripcion TEXT,
--     fecha_creacion DATE,
--     id_usuario INT,
--     FOREIGN KEY (id_usuario) REFERENCES Usuarios(id)
-- );

