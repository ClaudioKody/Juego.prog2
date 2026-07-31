
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self):
        if not self.initialized:
            # Aquí se inicializaría la conexión a la base de datos
            # Por ahora, es solo un placeholder
            print("DatabaseConnection: Inicializando conexión a la base de datos...")
            self.connection = None # Placeholder para la conexión real
            self.initialized = True

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection:
            print("DatabaseConnection: Cerrando conexión a la base de datos...")
            self.connection.close()
            self.connection = None

