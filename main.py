import sys
import hashlib
import mysql.connector
import base64
import pandas as pd
import matplotlib.pyplot as plt
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from pymongo import MongoClient, errors
from datetime import datetime
import threading
import time
from Gui.Qt_Designer import Ui_MainWindow

#services.msc
#Borrar = Borra datos de ambas bases
#BorrarMongo = Borra datos de Mongo
#BorrarSql = Borrar datos de MySQL

# Declaración de variables globales
mysql_available = False
mongodb_available = False
last_sync_time = None  # Para controlar la sincronización

# Función para sincronizar los datos bidireccionalmente
def sync_data_between_databases():
    global last_sync_time

    current_time = datetime.now()

    # Verificar si ha pasado suficiente tiempo desde la última sincronización
    if last_sync_time is None or (current_time - last_sync_time).total_seconds() > 10:
        print("Sincronizando datos entre MySQL y MongoDB...")
        sync_data_from_mongodb()
        sync_data_from_mysql()
        last_sync_time = current_time
    else:
        print("La sincronización ya se realizó recientemente.")

# Sincronizar datos desde MongoDB a MySQL
def sync_data_from_mongodb():
    global mysql_available, mongodb_available
    if mysql_available and mongodb_available:
        try:
            # Sincronizar usuarios
            usuarios = mongo_users.find({})
            for usuario in usuarios:
                cursor.execute(
                    "REPLACE INTO usuarios (usuario, contrasena) VALUES (%s, %s)",
                    (usuario["usuario"], usuario["contrasena"])
                )
            conn.commit()

            # Sincronizar datos de usuarios
            datos = mongo_data.find({})
            for dato in datos:
                cursor.execute(
                    "REPLACE INTO datos_usuario (nombre, apellido, edad, cedula, imagen) VALUES (%s, %s, %s, %s, %s)",
                    (dato["nombre"], dato["apellido"], dato["edad"], dato["cedula"], dato["imagen"])
                )
            conn.commit()

            print("Datos sincronizados desde MongoDB a MySQL.")
        except (errors.PyMongoError, mysql.connector.Error) as err:
            print(f"Error al sincronizar datos desde MongoDB a MySQL: {err}")
            mysql_available = False

# Sincronizar datos desde MySQL a MongoDB
def sync_data_from_mysql():
    global mongodb_available
    if mysql_available and mongodb_available:
        try:
            # Sincronizar usuarios
            cursor.execute("SELECT usuario, contrasena FROM usuarios")
            usuarios = cursor.fetchall()
            for usuario in usuarios:
                mongo_users.update_one(
                    {"usuario": usuario[0]},
                    {"$set": {"usuario": usuario[0], "contrasena": usuario[1], "timestamp": datetime.now()}},
                    upsert=True
                )

            # Sincronizar datos de usuarios
            cursor.execute("SELECT nombre, apellido, edad, cedula, imagen FROM datos_usuario")
            datos = cursor.fetchall()
            for dato in datos:
                mongo_data.update_one(
                    {"cedula": dato[3]},
                    {"$set": {
                        "nombre": dato[0], "apellido": dato[1], "edad": dato[2],
                        "cedula": dato[3], "imagen": dato[4], "timestamp": datetime.now()
                    }},
                    upsert=True
                )

            print("Datos sincronizados desde MySQL a MongoDB.")
        except (errors.PyMongoError, mysql.connector.Error) as e:
            print(f"Error al sincronizar datos desde MySQL a MongoDB: {e}")
            mongodb_available = False

# Conexión a la base de datos MySQL
def connect_mysql():
    global mysql_available, conn, cursor
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="qt_designer"
        )
        cursor = conn.cursor()
        mysql_available = True
        print("MySQL conectado exitosamente.")

        # Si MongoDB también está disponible, sincronizar
        if mongodb_available:
            sync_data_between_databases()
    except mysql.connector.Error as err:
        print(f"Error al conectar a MySQL: {err}")
        mysql_available = False

# Conexión a la base de datos MongoDB
def connect_mongodb():
    global mongodb_available, mongo_client, mongo_db, mongo_users, mongo_data
    try:
        mongo_client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        mongo_client.server_info()  # Verificar conexión
        mongo_db = mongo_client["qt_designer_backup"]
        mongo_users = mongo_db["usuarios"]
        mongo_data = mongo_db["datos_usuario"]
        mongodb_available = True
        print("MongoDB conectado exitosamente.")

        # Si MySQL también está disponible, sincronizar
        if mysql_available:
            sync_data_between_databases()
    except (errors.ServerSelectionTimeoutError, errors.ConnectionFailure) as err:
        print(f"Error al conectar a MongoDB: {err}")
        mongodb_available = False

connect_mysql()
connect_mongodb()

# Clase principal
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Configurar el banner inicial (Validación)
        self.toolBox.setCurrentIndex(0)

        # Conectar los botones a sus funciones
        self.Boton_Registro.clicked.connect(self.registrar_usuario)
        self.BotonVerificar.clicked.connect(self.verificar_usuario)
        self.Cargar.clicked.connect(self.cargar_imagen)
        self.Registrar.clicked.connect(self.registrar_datos_usuario)
        self.Consultar.clicked.connect(self.consultar_datos)

        # Hilo para escuchar la consola y borrar datos cuando sea necesario
        self.console_thread = threading.Thread(target=self.listen_console, daemon=True)
        self.console_thread.start()

    def registrar_usuario(self):
        global mysql_available, mongodb_available  # Declarar variable global

        usuario = self.Usuario.text()
        contrasena = self.Registro_Contrasena_2.text()
        hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

        try:
            if mysql_available:
                cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (%s, %s)", (usuario, hash_contrasena))
                conn.commit()
                QMessageBox.information(self, "Registro", "Usuario registrado en MySQL.")
                self.respaldo_usuario(usuario, hash_contrasena)  # Respaldar en MongoDB
            else:
                raise mysql.connector.errors.OperationalError
        except mysql.connector.errors.IntegrityError as e:
            QMessageBox.warning(self, "Error", f"El usuario '{usuario}' ya está registrado. Por favor, elige otro nombre de usuario.")
        except (mysql.connector.errors.OperationalError, mysql.connector.errors.InterfaceError) as e:
            print(f"Error al registrar usuario en MySQL: {e}")
            mysql_available = False
            if mongodb_available:
                self.respaldo_usuario(usuario, hash_contrasena)

    def respaldo_usuario(self, usuario, hash_contrasena):
        global mongodb_available  # Declarar variable global
        if mongodb_available:
            try:
                mongo_users.update_one(
                    {"usuario": usuario},
                    {"$set": {"usuario": usuario, "contrasena": hash_contrasena, "timestamp": datetime.now()}},
                    upsert=True
                )
                print("Usuario registrado/actualizado en MongoDB.")
            except errors.PyMongoError as e:
                print(f"Error al registrar en MongoDB: {e}")
                mongodb_available = False

    def verificar_usuario(self):
        global mysql_available, mongodb_available  # Declarar variable global

        usuario = self.Ingreso_Usuario.text()
        contrasena = self.Ingreso_Contrasena.text()
        hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

        try:
            if mysql_available:
                cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s", (usuario, hash_contrasena))
                result = cursor.fetchone()
            else:
                raise mysql.connector.errors.OperationalError
        except (mysql.connector.errors.OperationalError, mysql.connector.errors.InterfaceError):
            print("Conexión a MySQL perdida. Cambiando a MongoDB.")
            mysql_available = False
            result = None

        if not result and mongodb_available:
            try:
                result = mongo_users.find_one({"usuario": usuario, "contrasena": hash_contrasena})
            except errors.PyMongoError as e:
                print(f"Error al verificar usuario en MongoDB: {e}")
                mongodb_available = False

        if result:
            QMessageBox.information(self, "Ingreso", "Acceso concedido.")
            self.toolBox.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Ingreso", "Usuario o contraseña incorrectos.")

    def cargar_imagen(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Imagen (*.png *.jpg *.jpeg)")
        if file_path:
            img = plt.imread(file_path)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
            with open(file_path, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode('utf-8')
            self.imagen_codificada = base64_image

    def registrar_datos_usuario(self):
        global mysql_available, mongodb_available  # Declarar variable global

        nombre = self.Nombre.text()
        apellido = self.Apellido.text()
        edad_str = self.Edad.text()
        cedula = self.Cedula.text()

        # Validar que la edad sea un número entero
        if not edad_str.isdigit():
            QMessageBox.warning(self, "Error", "Por favor, ingresa una edad válida (solo números).")
            return

        edad = int(edad_str)

        if not hasattr(self, 'imagen_codificada'):
            QMessageBox.warning(self, "Error", "Por favor, carga una imagen antes de registrar.")
            return

        try:
            if mysql_available:
                cursor.execute("INSERT INTO datos_usuario (nombre, apellido, edad, cedula, imagen) VALUES (%s, %s, %s, %s, %s)", 
                               (nombre, apellido, edad, cedula, self.imagen_codificada))
                conn.commit()
                QMessageBox.information(self, "Registro", "Datos registrados en MySQL.")
                self.respaldo_datos_usuario(nombre, apellido, edad, cedula, self.imagen_codificada)
            else:
                raise mysql.connector.errors.OperationalError
        except mysql.connector.errors.IntegrityError as e:
            QMessageBox.warning(self, "Error", f"El usuario con cédula '{cedula}' ya está registrado. Por favor, verifica los datos.")
        except (mysql.connector.errors.OperationalError, mysql.connector.errors.InterfaceError) as e:
            print(f"Error al registrar datos en MySQL: {e}")
            mysql_available = False
            if mongodb_available:
                self.respaldo_datos_usuario(nombre, apellido, edad, cedula, self.imagen_codificada)

    def respaldo_datos_usuario(self, nombre, apellido, edad, cedula, imagen):
        global mongodb_available  # Declarar variable global
        if mongodb_available:
            try:
                mongo_data.update_one(
                    {"cedula": cedula},
                    {"$set": {
                        "nombre": nombre, "apellido": apellido, "edad": edad,
                        "cedula": cedula, "imagen": imagen, "timestamp": datetime.now()
                    }},
                    upsert=True
                )
                print("Datos registrados/actualizados en MongoDB.")
            except errors.PyMongoError as e:
                print(f"Error al respaldar datos en MongoDB: {e}")
                mongodb_available = False

    def consultar_datos(self):
        global mysql_available, mongodb_available  # Declarar variables globales

        cedula = self.CedulaConsulta.text()
        
        if not cedula:
            QMessageBox.warning(self, "Consulta", "Por favor ingresa una cédula.")
            return

        # Intentar reconectar a MySQL y MongoDB antes de proceder con la consulta
        connect_mysql()
        connect_mongodb()

        # Inicializar el resultado como None
        result = None

        # Intentar consultar en MySQL si está disponible
        if mysql_available:
            try:
                cursor.execute("SELECT nombre, apellido, edad, cedula, imagen FROM datos_usuario WHERE cedula = %s", (cedula,))
                result = cursor.fetchone()
            except (mysql.connector.errors.OperationalError, mysql.connector.errors.InterfaceError) as e:
                print(f"Error al consultar en MySQL: {e}")
                mysql_available = False
                result = None

        # Si no se encontró resultado en MySQL o no está disponible, intentar en MongoDB
        if result is None and mongodb_available:
            try:
                result = mongo_data.find_one({"cedula": cedula})
            except errors.PyMongoError as e:
                print(f"Error al consultar en MongoDB: {e}")
                mongodb_available = False

        if result:
            if mysql_available and isinstance(result, tuple):
                # Resultado obtenido de MySQL
                if len(result) >= 5:
                    nombre, apellido, edad, cedula, imagen_base64 = result
                else:
                    QMessageBox.warning(self, "Consulta", "Los datos obtenidos no tienen el formato esperado.")
                    return
            elif mongodb_available and isinstance(result, dict):
                # Resultado obtenido de MongoDB
                nombre = result["nombre"]
                apellido = result["apellido"]
                edad = result["edad"]
                cedula = result["cedula"]
                imagen_base64 = result["imagen"]
            else:
                QMessageBox.warning(self, "Consulta", "Los datos obtenidos no tienen el formato esperado.")
                return

            # Mostrar los datos en la interfaz
            self.NombreConsulta.setText(nombre)
            self.ApellidoConsulta.setText(apellido)
            self.EdadConsulta.setText(str(edad))
            self.CedulaConsulta.setText(cedula)

            # Decodificar y mostrar la imagen
            image_data = base64.b64decode(imagen_base64)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image_data)
            self.ImagenLabel.setPixmap(pixmap)
            self.ImagenLabel.setScaledContents(True)
        else:
            QMessageBox.warning(self, "Consulta", "No se encontraron datos para la cédula ingresada.")

    # Función para escuchar la consola y eliminar datos según el comando ingresado
    def listen_console(self):
        while True:
            command = input().strip().lower()
            if command == "borrar":
                self.borrar_datos()
            elif command == "borrarmongo":
                self.borrar_mongo()
            elif command == "borrarsql":
                self.borrar_sql()

    # Función para borrar los datos de ambas bases de datos
    def borrar_datos(self):
        self.borrar_sql()
        self.borrar_mongo()

    # Función para borrar los datos de MongoDB
    def borrar_mongo(self):
        global mongodb_available
        if mongodb_available:
            try:
                mongo_users.delete_many({})
                mongo_data.delete_many({})
                print("Datos borrados de MongoDB.")
            except Exception as e:
                print(f"Error al borrar los datos de MongoDB: {e}")
        else:
            print("MongoDB no está disponible. No se pueden borrar los datos de MongoDB.")

    # Función para borrar los datos de MySQL
    def borrar_sql(self):
        global mysql_available
        if mysql_available:
            try:
                cursor.execute("DELETE FROM usuarios")
                cursor.execute("DELETE FROM datos_usuario")
                conn.commit()
                print("Datos borrados de MySQL.")
            except Exception as e:
                print(f"Error al borrar los datos de MySQL: {e}")
        else:
            print("MySQL no está disponible. No se pueden borrar los datos de MySQL.")

# Inicialización de la aplicación
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
