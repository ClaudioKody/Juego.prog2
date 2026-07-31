
from repository.database.connection import MySQLConnection

class ScoreRepository:
    def __init__(self):
        self.db_connection = MySQLConnection()

    def save_score(self, player_name, score):
        conn = self.db_connection.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO scores (player_name, score) VALUES (%s, %s)"
                cursor.execute(query, (player_name, score))
                conn.commit()
                print(f"Puntaje {score} de {player_name} guardado con éxito.")
            except Exception as e:
                print(f"Error al guardar puntaje: {e}")

    def get_high_scores(self, limit=10):
        conn = self.db_connection.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT player_name, score FROM scores ORDER BY score DESC LIMIT %s"
                cursor.execute(query, (limit,))
                return cursor.fetchall()
            except Exception as e:
                print(f"Error al obtener puntajes altos: {e}")
        return []
