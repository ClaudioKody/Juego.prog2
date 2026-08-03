from repository.database.connection import MySQLConnection

class UserRepository:
    def __init__(self):
        self.db_connection = MySQLConnection()

    def obtener_o_crear_usuario(self, username):
        """
        Busca al usuario en la base de datos.
        Si existe, devuelve su nivel actual y puntaje máximo.
        Si no existe, lo crea de forma segura con nivel 1 y max_score 0.
        """
        conn = self.db_connection.get_connection()
        if not conn:
            print("Error: No hay conexión a la base de datos.")
            return 1, 0
        
        try:
            cursor = conn.cursor()
            # Verificamos si ya existe el usuario
            cursor.execute("SELECT current_level, max_score FROM usuarios WHERE username = %s", (username,))
            row = cursor.fetchone()
            
            if row:
                level, max_score = row
                print(f"Usuario '{username}' encontrado. Nivel actual: {level}")
                # Manejamos posibles valores NULL en la base de datos
                lvl = level if level is not None else 1
                score = max_score if max_score is not None else 0
                return lvl, score
            else:
                # Insertamos el nuevo usuario asegurando valores por defecto válidos
                cursor.execute(
                    "INSERT INTO usuarios (username, current_level, max_score) VALUES (%s, %s, %s)",
                    (username, 1, 0)
                )
                conn.commit()
                print(f"Nuevo usuario '{username}' registrado con éxito en nivel 1.")
                return 1, 0
                
        except Exception as e:
            print(f"Error al gestionar el usuario en la base de datos: {e}")
            if conn:
                conn.rollback()
            return 1, 0

    def actualizar_progreso(self, username, level, score):
        conn = self.db_connection.get_connection()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE usuarios
                SET current_level = GREATEST(COALESCE(current_level, 1), %s),
                    max_score = GREATEST(COALESCE(max_score, 0), %s)
                WHERE username = %s
            """, (level, score, username))
            conn.commit()
            print(f"Progreso de '{username}' actualizado en la base de datos.")
        except Exception as e:
            print(f"Error al actualizar el progreso: {e}")
            if conn:
                conn.rollback()

    def guardar_historial(self, username, score, level_reached):
        conn = self.db_connection.get_connection()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO historial_partidas (username, score, level_reached)
                VALUES (%s, %s, %s)
            """, (username, score, level_reached))
            conn.commit()
            print("Partida guardada en el historial.")
        except Exception as e:
            print(f"Error al guardar el historial: {e}")
            if conn:
                conn.rollback()