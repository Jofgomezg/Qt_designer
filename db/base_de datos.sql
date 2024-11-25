drop database qt_designer;
-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS qt_designer;
USE qt_designer;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(64) NOT NULL
);