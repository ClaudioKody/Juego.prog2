import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from patterns.singleton.database_connection import DatabaseConnection

# Cargamos las variables del archivo .env
load_dotenv()

class MySQLConnection(DatabaseConnection):
    _instance = None

    def __new__(cls):
        # Aseguramos el patrón Singleton de forma robusta
        if cls._instance is None:
            cls._instance = super(MySQLConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def __init__(self):
        super().__init__()
        # Intentamos conectar solo si no está conectada ya
        if not self.connection or not self.connection.is_connected():
            self._conectar()

    def _conectar(self):
        try:
            # Obtenemos las credenciales desde el archivo .env con valores por defecto de seguridad
            host = os.getenv("DB_HOST", "localhost")
            user = os.getenv("DB_USER", "root")
            password = os.getenv("DB_PASSWORD", "")
            database = os.getenv("DB_NAME", "juego_prog2")

            # Configuración de la conexión con timeout de seguridad (5 segundos)
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                connection_timeout=5  # Evita que se congele el juego si XAMPP/MySQL falla
            )
            
            if self.connection.is_connected():
                print("Conexión a MySQL establecida con éxito mediante .env.")
                
        except Error as err:
            print(f"Error al conectar a MySQL: {err}")
            self.connection = None

    def get_connection(self):
        # Verificamos que la conexión siga viva antes de devolverla
        try:
            if self.connection and self.connection.is_connected():
                return self.connection
            else:
                self._conectar()
                return self.connection
        except Error:
            self._conectar()
            return self.connection

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a MySQL cerrada.")
            self.connection = None