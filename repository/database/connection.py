
import mysql.connector
from patterns.singleton.database_connection import DatabaseConnection

class MySQLConnection(DatabaseConnection):
    def __init__(self):
        super().__init__()
        if not self.connection:
            try:
                # Configuración de la conexión a MySQL
                # Reemplazar con tus credenciales reales
                self.connection = mysql.connector.connect(
                    host="localhost",
                    user="your_user",
                    password="your_password",
                    database="your_database"
                )
                if self.connection.is_connected():
                    print("Conexión a MySQL establecida con éxito.")
                    self.create_score_table()
            except mysql.connector.Error as err:
                print(f"Error al conectar a MySQL: {err}")
                self.connection = None

    def create_score_table(self):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS scores (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        player_name VARCHAR(255) NOT NULL,
                        score INT NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                self.connection.commit()
                print("Tabla 'scores' verificada/creada.")
            except mysql.connector.Error as err:
                print(f"Error al crear la tabla 'scores': {err}")

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a MySQL cerrada.")

