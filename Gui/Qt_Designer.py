# Form implementation generated from reading ui file 'Gui/Qt_Designer.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(parent=self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 581, 451))
        self.toolBox.setObjectName("toolBox")
        self.Validacion = QtWidgets.QWidget()
        self.Validacion.setGeometry(QtCore.QRect(0, 0, 581, 397))
        self.Validacion.setObjectName("Validacion")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.Validacion)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 511, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.Ingreso = QtWidgets.QWidget()
        self.Ingreso.setObjectName("Ingreso")
        self.Ingreso_Contrasena_2 = QtWidgets.QLabel(parent=self.Ingreso)
        self.Ingreso_Contrasena_2.setGeometry(QtCore.QRect(60, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingreso_Contrasena_2.setFont(font)
        self.Ingreso_Contrasena_2.setObjectName("Ingreso_Contrasena_2")
        self.BotonVerificar = QtWidgets.QPushButton(parent=self.Ingreso)
        self.BotonVerificar.setGeometry(QtCore.QRect(250, 180, 75, 23))
        self.BotonVerificar.setObjectName("BotonVerificar")
        self.Ingreso_Usuario_2 = QtWidgets.QLabel(parent=self.Ingreso)
        self.Ingreso_Usuario_2.setGeometry(QtCore.QRect(100, 50, 101, 41))
        self.Ingreso_Usuario_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingreso_Usuario_2.setFont(font)
        self.Ingreso_Usuario_2.setLineWidth(1)
        self.Ingreso_Usuario_2.setObjectName("Ingreso_Usuario_2")
        self.Ingreso_Usuario = QtWidgets.QLineEdit(parent=self.Ingreso)
        self.Ingreso_Usuario.setGeometry(QtCore.QRect(200, 60, 181, 20))
        self.Ingreso_Usuario.setObjectName("Ingreso_Usuario")
        self.Ingreso_Contrasena = QtWidgets.QLineEdit(parent=self.Ingreso)
        self.Ingreso_Contrasena.setGeometry(QtCore.QRect(200, 130, 181, 20))
        self.Ingreso_Contrasena.setObjectName("Ingreso_Contrasena")
        self.tabWidget.addTab(self.Ingreso, "")
        self.Registro = QtWidgets.QWidget()
        self.Registro.setObjectName("Registro")
        self.Registro_Contrasena = QtWidgets.QLabel(parent=self.Registro)
        self.Registro_Contrasena.setGeometry(QtCore.QRect(60, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Registro_Contrasena.setFont(font)
        self.Registro_Contrasena.setObjectName("Registro_Contrasena")
        self.Registro_Usuario = QtWidgets.QLabel(parent=self.Registro)
        self.Registro_Usuario.setGeometry(QtCore.QRect(100, 50, 101, 41))
        self.Registro_Usuario.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Registro_Usuario.setFont(font)
        self.Registro_Usuario.setLineWidth(1)
        self.Registro_Usuario.setObjectName("Registro_Usuario")
        self.Usuario = QtWidgets.QLineEdit(parent=self.Registro)
        self.Usuario.setGeometry(QtCore.QRect(200, 60, 181, 20))
        self.Usuario.setObjectName("Usuario")
        self.Boton_Registro = QtWidgets.QPushButton(parent=self.Registro)
        self.Boton_Registro.setGeometry(QtCore.QRect(250, 180, 75, 23))
        self.Boton_Registro.setObjectName("Boton_Registro")
        self.Registro_Contrasena_2 = QtWidgets.QLineEdit(parent=self.Registro)
        self.Registro_Contrasena_2.setGeometry(QtCore.QRect(200, 130, 181, 20))
        self.Registro_Contrasena_2.setObjectName("Registro_Contrasena_2")
        self.tabWidget.addTab(self.Registro, "")
        self.toolBox.addItem(self.Validacion, "")
        self.Consulta = QtWidgets.QWidget()
        self.Consulta.setGeometry(QtCore.QRect(0, 0, 581, 397))
        self.Consulta.setObjectName("Consulta")
        self.tabWidget_2 = QtWidgets.QTabWidget(parent=self.Consulta)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 0, 501, 281))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Ingresar = QtWidgets.QWidget()
        self.Ingresar.setObjectName("Ingresar")
        self.Cedula = QtWidgets.QLineEdit(parent=self.Ingresar)
        self.Cedula.setGeometry(QtCore.QRect(180, 130, 113, 20))
        self.Cedula.setObjectName("Cedula")
        self.Ingresar_Cedula = QtWidgets.QLabel(parent=self.Ingresar)
        self.Ingresar_Cedula.setGeometry(QtCore.QRect(80, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingresar_Cedula.setFont(font)
        self.Ingresar_Cedula.setObjectName("Ingresar_Cedula")
        self.Ingresar_Nombre = QtWidgets.QLabel(parent=self.Ingresar)
        self.Ingresar_Nombre.setGeometry(QtCore.QRect(70, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingresar_Nombre.setFont(font)
        self.Ingresar_Nombre.setObjectName("Ingresar_Nombre")
        self.Apellido = QtWidgets.QLineEdit(parent=self.Ingresar)
        self.Apellido.setGeometry(QtCore.QRect(180, 50, 113, 20))
        self.Apellido.setObjectName("Apellido")
        self.Edad = QtWidgets.QLineEdit(parent=self.Ingresar)
        self.Edad.setGeometry(QtCore.QRect(180, 90, 113, 20))
        self.Edad.setObjectName("Edad")
        self.Ingresar_Foto = QtWidgets.QLabel(parent=self.Ingresar)
        self.Ingresar_Foto.setGeometry(QtCore.QRect(100, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingresar_Foto.setFont(font)
        self.Ingresar_Foto.setObjectName("Ingresar_Foto")
        self.Nombre = QtWidgets.QLineEdit(parent=self.Ingresar)
        self.Nombre.setGeometry(QtCore.QRect(180, 10, 113, 20))
        self.Nombre.setObjectName("Nombre")
        self.Ingresar_Apellido = QtWidgets.QLabel(parent=self.Ingresar)
        self.Ingresar_Apellido.setGeometry(QtCore.QRect(70, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingresar_Apellido.setFont(font)
        self.Ingresar_Apellido.setObjectName("Ingresar_Apellido")
        self.Ingresar_Edad = QtWidgets.QLabel(parent=self.Ingresar)
        self.Ingresar_Edad.setGeometry(QtCore.QRect(100, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingresar_Edad.setFont(font)
        self.Ingresar_Edad.setObjectName("Ingresar_Edad")
        self.Registrar = QtWidgets.QPushButton(parent=self.Ingresar)
        self.Registrar.setGeometry(QtCore.QRect(400, 230, 75, 23))
        self.Registrar.setObjectName("Registrar")
        self.Cargar = QtWidgets.QPushButton(parent=self.Ingresar)
        self.Cargar.setGeometry(QtCore.QRect(180, 170, 111, 23))
        self.Cargar.setObjectName("Cargar")
        self.tabWidget_2.addTab(self.Ingresar, "")
        self.Consulta1 = QtWidgets.QWidget()
        self.Consulta1.setObjectName("Consulta1")
        self.Consultar = QtWidgets.QPushButton(parent=self.Consulta1)
        self.Consultar.setGeometry(QtCore.QRect(400, 230, 75, 23))
        self.Consultar.setObjectName("Consultar")
        self.CedulaConsulta = QtWidgets.QLineEdit(parent=self.Consulta1)
        self.CedulaConsulta.setGeometry(QtCore.QRect(180, 10, 113, 20))
        self.CedulaConsulta.setObjectName("CedulaConsulta")
        self.Cedula_2 = QtWidgets.QLabel(parent=self.Consulta1)
        self.Cedula_2.setGeometry(QtCore.QRect(80, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Cedula_2.setFont(font)
        self.Cedula_2.setObjectName("Cedula_2")
        self.ImagenLabel = QtWidgets.QLabel(parent=self.Consulta1)
        self.ImagenLabel.setGeometry(QtCore.QRect(340, 30, 151, 171))
        self.ImagenLabel.setText("")
        self.ImagenLabel.setScaledContents(True)
        self.ImagenLabel.setObjectName("ImagenLabel")
        self.Ingresar_Nombre_2 = QtWidgets.QLabel(parent=self.Consulta1)
        self.Ingresar_Nombre_2.setGeometry(QtCore.QRect(70, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingresar_Nombre_2.setFont(font)
        self.Ingresar_Nombre_2.setObjectName("Ingresar_Nombre_2")
        self.NombreConsulta = QtWidgets.QLineEdit(parent=self.Consulta1)
        self.NombreConsulta.setGeometry(QtCore.QRect(180, 50, 113, 20))
        self.NombreConsulta.setObjectName("NombreConsulta")
        self.ApellidoConsulta = QtWidgets.QLineEdit(parent=self.Consulta1)
        self.ApellidoConsulta.setGeometry(QtCore.QRect(180, 90, 113, 20))
        self.ApellidoConsulta.setObjectName("ApellidoConsulta")
        self.Ingresar_Apellido_2 = QtWidgets.QLabel(parent=self.Consulta1)
        self.Ingresar_Apellido_2.setGeometry(QtCore.QRect(70, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingresar_Apellido_2.setFont(font)
        self.Ingresar_Apellido_2.setObjectName("Ingresar_Apellido_2")
        self.EdadConsulta = QtWidgets.QLineEdit(parent=self.Consulta1)
        self.EdadConsulta.setGeometry(QtCore.QRect(180, 130, 113, 20))
        self.EdadConsulta.setObjectName("EdadConsulta")
        self.Ingresar_Edad_2 = QtWidgets.QLabel(parent=self.Consulta1)
        self.Ingresar_Edad_2.setGeometry(QtCore.QRect(100, 130, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Ingresar_Edad_2.setFont(font)
        self.Ingresar_Edad_2.setObjectName("Ingresar_Edad_2")
        self.tabWidget_2.addTab(self.Consulta1, "")
        self.toolBox.addItem(self.Consulta, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Ingreso_Contrasena_2.setText(_translate("MainWindow", "Contraseña:"))
        self.BotonVerificar.setText(_translate("MainWindow", "Verificar"))
        self.Ingreso_Usuario_2.setText(_translate("MainWindow", "Usuario:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ingreso), _translate("MainWindow", "Ingreso"))
        self.Registro_Contrasena.setText(_translate("MainWindow", "Contraseña:"))
        self.Registro_Usuario.setText(_translate("MainWindow", "Usuario:"))
        self.Boton_Registro.setText(_translate("MainWindow", "Registrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Registro), _translate("MainWindow", "Registro"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Validacion), _translate("MainWindow", "Validacion"))
        self.Ingresar_Cedula.setText(_translate("MainWindow", "Cedula:"))
        self.Ingresar_Nombre.setText(_translate("MainWindow", "Nombre:"))
        self.Ingresar_Foto.setText(_translate("MainWindow", "Foto:"))
        self.Ingresar_Apellido.setText(_translate("MainWindow", "Apellido:"))
        self.Ingresar_Edad.setText(_translate("MainWindow", "Edad:"))
        self.Registrar.setText(_translate("MainWindow", "Registrar"))
        self.Cargar.setText(_translate("MainWindow", "Cargar Imagen"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Ingresar), _translate("MainWindow", "Ingresar"))
        self.Consultar.setText(_translate("MainWindow", "Consultar"))
        self.Cedula_2.setText(_translate("MainWindow", "Cedula:"))
        self.Ingresar_Nombre_2.setText(_translate("MainWindow", "Nombre:"))
        self.Ingresar_Apellido_2.setText(_translate("MainWindow", "Apellido:"))
        self.Ingresar_Edad_2.setText(_translate("MainWindow", "Edad:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Consulta1), _translate("MainWindow", "Consulta"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Consulta), _translate("MainWindow", "Consulta"))
