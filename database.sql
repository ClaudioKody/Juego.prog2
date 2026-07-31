-- Creación de la base de datos para el juego tipo Galaga/Xevious
CREATE DATABASE IF NOT EXISTS juego_prog2;
USE juego_prog2;

-- Tabla para almacenar los puntajes (Persistencia)
CREATE TABLE IF NOT EXISTS scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(50) NOT NULL,
    score INT NOT NULL,
    date_achieved TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para configuración o ítems guardados
CREATE TABLE IF NOT EXISTS game_config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    setting_key VARCHAR(50) UNIQUE NOT NULL,
    setting_value VARCHAR(50) NOT NULL
);
