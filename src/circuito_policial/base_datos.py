import sqlite3


class BaseDatos:

    def __init__(self, nombre_base_datos="circuito_policial.db"):
        self.__nombre_base_datos = nombre_base_datos

    # --------------------------------------------------
    # CREAR TABLA
    # --------------------------------------------------

    def crear_tabla_servidores(self):
        conexion = sqlite3.connect(self.__nombre_base_datos)
        cursor = conexion.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS servidores (
                identificacion TEXT PRIMARY KEY,
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
    # CREATE - GUARDAR SERVIDOR
    # --------------------------------------------------

    def guardar_servidor(
        self,
        identificacion: str,
        nombre: str,
        tipo: str,
        grado: str,
        estado: str
    ):
        conexion = sqlite3.connect(self.__nombre_base_datos)
        cursor = conexion.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO servidores (
                    identificacion,
                    nombre,
                    tipo,
                    grado,
                    estado
                )
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
                f"Servidor {nombre} guardado correctamente en SQLite."
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
    # READ - LISTAR SERVIDORES
    # --------------------------------------------------

    def listar_servidores(self):
        conexion = sqlite3.connect(self.__nombre_base_datos)
        cursor = conexion.cursor()

        cursor.execute(
            """
            SELECT
                identificacion,
                nombre,
                tipo,
                grado,
                estado
            FROM servidores
            ORDER BY identificacion
            """
        )

        servidores = cursor.fetchall()

        conexion.close()

        return servidores

    # --------------------------------------------------
    # READ - BUSCAR SERVIDOR
    # --------------------------------------------------

    def buscar_servidor(self, identificacion: str):
        conexion = sqlite3.connect(self.__nombre_base_datos)
        cursor = conexion.cursor()

        cursor.execute(
            """
            SELECT
                identificacion,
                nombre,
                tipo,
                grado,
                estado
            FROM servidores
            WHERE identificacion = ?
            """,
            (identificacion,)
        )

        servidor = cursor.fetchone()

        conexion.close()

        return servidor

    # --------------------------------------------------
    # UPDATE - ACTUALIZAR SERVIDOR
    # --------------------------------------------------

    def actualizar_servidor(
        self,
        identificacion: str,
        nombre: str,
        tipo: str,
        grado: str,
        estado: str
    ):
        conexion = sqlite3.connect(self.__nombre_base_datos)
        cursor = conexion.cursor()

        cursor.execute(
            """
            UPDATE servidores
            SET
                nombre = ?,
                tipo = ?,
                grado = ?,
                estado = ?
            WHERE identificacion = ?
            """,
            (
                nombre,
                tipo,
                grado,
                estado,
                identificacion
            )
        )

        conexion.commit()

        if cursor.rowcount == 0:
            print(
                f"No se pudo actualizar. La identificación "
                f"{identificacion} no existe en SQLite."
            )

            conexion.close()
            return False

        conexion.close()

        print(
            f"Servidor {identificacion} actualizado "
            f"correctamente en SQLite."
        )

        return True

    # --------------------------------------------------
    # DELETE - ELIMINAR SERVIDOR
    # --------------------------------------------------

    def eliminar_servidor(self, identificacion: str):
        conexion = sqlite3.connect(self.__nombre_base_datos)
        cursor = conexion.cursor()

        cursor.execute(
            """
            DELETE FROM servidores
            WHERE identificacion = ?
            """,
            (identificacion,)
        )

        conexion.commit()

        if cursor.rowcount == 0:
            print(
                f"No se pudo eliminar. La identificación "
                f"{identificacion} no existe en SQLite."
            )

            conexion.close()
            return False

        conexion.close()

        print(
            f"Servidor {identificacion} eliminado "
            f"correctamente de SQLite."
        )

        return True