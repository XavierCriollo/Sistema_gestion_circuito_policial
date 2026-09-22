import sqlite3


class BaseDatos:

    def __init__(self, nombre_db="circuito_policial.db"):
        self.__nombre_db = nombre_db

    def conectar(self):
        return sqlite3.connect(self.__nombre_db)

    # --------------------------------------------------
    # CREAR TABLA
    # --------------------------------------------------

    def crear_tabla_servidores(self):
        conexion = self.conectar()
        cursor = conexion.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS servidores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                identificacion TEXT UNIQUE NOT NULL,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                grado TEXT NOT NULL,
                estado TEXT NOT NULL
            )
            """
        )

        conexion.commit()
        conexion.close()

        print("Tabla de servidores preparada correctamente.")

    # --------------------------------------------------
    # GUARDAR SERVIDOR
    # --------------------------------------------------

    def guardar_servidor(
        self,
        identificacion: str,
        nombre: str,
        tipo: str,
        grado: str,
        estado: str
    ) -> bool:

        conexion = self.conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO servidores
                (identificacion, nombre, tipo, grado, estado)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    identificacion,
                    nombre,
                    tipo,
                    grado,
                    estado
                )
            )

            conexion.commit()

            print(
                f"Servidor {nombre} guardado "
                f"correctamente en SQLite."
            )

            return True

        except sqlite3.IntegrityError:
            print(
                f"No se pudo guardar. La identificación "
                f"{identificacion} ya existe en SQLite."
            )

            return False

        finally:
            conexion.close()

    # --------------------------------------------------
    # CONSULTAR SERVIDORES
    # --------------------------------------------------

    def consultar_servidores(self):

        conexion = self.conectar()
        cursor = conexion.cursor()

        cursor.execute(
            """
            SELECT identificacion, nombre, tipo, grado, estado
            FROM servidores
            """
        )

        servidores = cursor.fetchall()

        conexion.close()

        return servidores