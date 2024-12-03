# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setBaseSize(QSize(900, 700))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 127))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush6 = QBrush(QColor(127, 127, 127, 127))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush1)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.podstawieniowy_pushButton = QPushButton(self.widget)
        self.podstawieniowy_pushButton.setObjectName(u"podstawieniowy_pushButton")

        self.verticalLayout.addWidget(self.podstawieniowy_pushButton)

        self.transpozycyjny_pushButton = QPushButton(self.widget)
        self.transpozycyjny_pushButton.setObjectName(u"transpozycyjny_pushButton")

        self.verticalLayout.addWidget(self.transpozycyjny_pushButton)

        self.des_pushButton = QPushButton(self.widget)
        self.des_pushButton.setObjectName(u"des_pushButton")

        self.verticalLayout.addWidget(self.des_pushButton)

        self.aes_pushButton = QPushButton(self.widget)
        self.aes_pushButton.setObjectName(u"aes_pushButton")

        self.verticalLayout.addWidget(self.aes_pushButton)

        self.rsa_pushButton = QPushButton(self.widget)
        self.rsa_pushButton.setObjectName(u"rsa_pushButton")

        self.verticalLayout.addWidget(self.rsa_pushButton)

        self.diffieHellman_pushButton = QPushButton(self.widget)
        self.diffieHellman_pushButton.setObjectName(u"diffieHellman_pushButton")

        self.verticalLayout.addWidget(self.diffieHellman_pushButton)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_20 = QVBoxLayout(self.widget_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_41 = QLabel(self.widget_6)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_20.addWidget(self.label_41)

        self.generateSignature_pushButton = QPushButton(self.widget_6)
        self.generateSignature_pushButton.setObjectName(u"generateSignature_pushButton")

        self.verticalLayout_20.addWidget(self.generateSignature_pushButton)

        self.signDocumen_pushButton = QPushButton(self.widget_6)
        self.signDocumen_pushButton.setObjectName(u"signDocumen_pushButton")

        self.verticalLayout_20.addWidget(self.signDocumen_pushButton)

        self.verifySignature_pushButton = QPushButton(self.widget_6)
        self.verifySignature_pushButton.setObjectName(u"verifySignature_pushButton")

        self.verticalLayout_20.addWidget(self.verifySignature_pushButton)


        self.verticalLayout.addWidget(self.widget_6)

        self.verticalSpacer = QSpacerItem(20, 403, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.siec_pushButton = QPushButton(self.widget)
        self.siec_pushButton.setObjectName(u"siec_pushButton")

        self.verticalLayout.addWidget(self.siec_pushButton)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout.addWidget(self.label_15)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.podstawieniowy_page = QWidget()
        self.podstawieniowy_page.setObjectName(u"podstawieniowy_page")
        self.gridLayout_9 = QGridLayout(self.podstawieniowy_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Vigener_stackedWidget = QStackedWidget(self.podstawieniowy_page)
        self.Vigener_stackedWidget.setObjectName(u"Vigener_stackedWidget")
        self.podstawieniowy_normal = QWidget()
        self.podstawieniowy_normal.setObjectName(u"podstawieniowy_normal")
        self.gridLayout_2 = QGridLayout(self.podstawieniowy_normal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Vigener_decode_output_save = QPushButton(self.podstawieniowy_normal)
        self.Vigener_decode_output_save.setObjectName(u"Vigener_decode_output_save")

        self.gridLayout_2.addWidget(self.Vigener_decode_output_save, 9, 2, 1, 1)

        self.Vigener_input_file = QPushButton(self.podstawieniowy_normal)
        self.Vigener_input_file.setObjectName(u"Vigener_input_file")

        self.gridLayout_2.addWidget(self.Vigener_input_file, 1, 2, 1, 1)

        self.Vigener_output = QTextEdit(self.podstawieniowy_normal)
        self.Vigener_output.setObjectName(u"Vigener_output")
        self.Vigener_output.setMaximumSize(QSize(16777215, 70))
        self.Vigener_output.setReadOnly(True)

        self.gridLayout_2.addWidget(self.Vigener_output, 4, 0, 1, 2)

        self.Vigener_output_save = QPushButton(self.podstawieniowy_normal)
        self.Vigener_output_save.setObjectName(u"Vigener_output_save")

        self.gridLayout_2.addWidget(self.Vigener_output_save, 4, 2, 1, 1)

        self.Vigener_decode_input_file = QPushButton(self.podstawieniowy_normal)
        self.Vigener_decode_input_file.setObjectName(u"Vigener_decode_input_file")

        self.gridLayout_2.addWidget(self.Vigener_decode_input_file, 6, 2, 1, 1)

        self.label_6 = QLabel(self.podstawieniowy_normal)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 10, 0, 1, 1)

        self.Vigener_decode_input_text = QLineEdit(self.podstawieniowy_normal)
        self.Vigener_decode_input_text.setObjectName(u"Vigener_decode_input_text")
        self.Vigener_decode_input_text.setMaxLength(999999999)

        self.gridLayout_2.addWidget(self.Vigener_decode_input_text, 6, 1, 1, 1)

        self.Vigener_decode_button = QPushButton(self.podstawieniowy_normal)
        self.Vigener_decode_button.setObjectName(u"Vigener_decode_button")

        self.gridLayout_2.addWidget(self.Vigener_decode_button, 8, 0, 1, 3)

        self.label_5 = QLabel(self.podstawieniowy_normal)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 3)

        self.label_3 = QLabel(self.podstawieniowy_normal)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_7 = QLabel(self.podstawieniowy_normal)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)

        self.Vigener_input_text = QLineEdit(self.podstawieniowy_normal)
        self.Vigener_input_text.setObjectName(u"Vigener_input_text")
        self.Vigener_input_text.setMaxLength(999999999)

        self.gridLayout_2.addWidget(self.Vigener_input_text, 1, 1, 1, 1)

        self.label_8 = QLabel(self.podstawieniowy_normal)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)

        self.Vigener_button = QPushButton(self.podstawieniowy_normal)
        self.Vigener_button.setObjectName(u"Vigener_button")

        self.gridLayout_2.addWidget(self.Vigener_button, 3, 0, 1, 3)

        self.Vigener_decode_output = QTextEdit(self.podstawieniowy_normal)
        self.Vigener_decode_output.setObjectName(u"Vigener_decode_output")
        self.Vigener_decode_output.setMaximumSize(QSize(16777215, 70))
        self.Vigener_decode_output.setReadOnly(True)

        self.gridLayout_2.addWidget(self.Vigener_decode_output, 9, 0, 1, 2)

        self.Vigener_input_key = QLineEdit(self.podstawieniowy_normal)
        self.Vigener_input_key.setObjectName(u"Vigener_input_key")
        self.Vigener_input_key.setMaxLength(999999999)

        self.gridLayout_2.addWidget(self.Vigener_input_key, 2, 1, 1, 2)

        self.label_4 = QLabel(self.podstawieniowy_normal)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.Vigener_decode_input_key = QLineEdit(self.podstawieniowy_normal)
        self.Vigener_decode_input_key.setObjectName(u"Vigener_decode_input_key")
        self.Vigener_decode_input_key.setMaxLength(999999999)

        self.gridLayout_2.addWidget(self.Vigener_decode_input_key, 7, 1, 1, 2)

        self.Vigener_stackedWidget.addWidget(self.podstawieniowy_normal)
        self.podstawieniowy_all_files = QWidget()
        self.podstawieniowy_all_files.setObjectName(u"podstawieniowy_all_files")
        self.gridLayout_10 = QGridLayout(self.podstawieniowy_all_files)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Vigener_decode_button_2 = QPushButton(self.podstawieniowy_all_files)
        self.Vigener_decode_button_2.setObjectName(u"Vigener_decode_button_2")

        self.gridLayout_10.addWidget(self.Vigener_decode_button_2, 7, 0, 1, 3)

        self.Vigener_decode_input_file_2 = QPushButton(self.podstawieniowy_all_files)
        self.Vigener_decode_input_file_2.setObjectName(u"Vigener_decode_input_file_2")

        self.gridLayout_10.addWidget(self.Vigener_decode_input_file_2, 5, 2, 1, 1)

        self.label_20 = QLabel(self.podstawieniowy_all_files)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_10.addWidget(self.label_20, 0, 0, 1, 3)

        self.label_24 = QLabel(self.podstawieniowy_all_files)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_10.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_21 = QLabel(self.podstawieniowy_all_files)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_10.addWidget(self.label_21, 5, 0, 1, 1)

        self.label_19 = QLabel(self.podstawieniowy_all_files)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_10.addWidget(self.label_19, 6, 0, 1, 1)

        self.Vigener_decode_input_key_2 = QLineEdit(self.podstawieniowy_all_files)
        self.Vigener_decode_input_key_2.setObjectName(u"Vigener_decode_input_key_2")
        self.Vigener_decode_input_key_2.setMaxLength(999999999)

        self.gridLayout_10.addWidget(self.Vigener_decode_input_key_2, 6, 1, 1, 2)

        self.label_22 = QLabel(self.podstawieniowy_all_files)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_10.addWidget(self.label_22, 2, 0, 1, 1)

        self.Vigener_button_2 = QPushButton(self.podstawieniowy_all_files)
        self.Vigener_button_2.setObjectName(u"Vigener_button_2")

        self.gridLayout_10.addWidget(self.Vigener_button_2, 3, 0, 1, 3)

        self.Vigener_file_path = QLineEdit(self.podstawieniowy_all_files)
        self.Vigener_file_path.setObjectName(u"Vigener_file_path")
        self.Vigener_file_path.setMaxLength(999999999)
        self.Vigener_file_path.setReadOnly(True)

        self.gridLayout_10.addWidget(self.Vigener_file_path, 1, 1, 1, 1)

        self.label_23 = QLabel(self.podstawieniowy_all_files)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_10.addWidget(self.label_23, 4, 0, 1, 3)

        self.Vigener_decode_file_path = QLineEdit(self.podstawieniowy_all_files)
        self.Vigener_decode_file_path.setObjectName(u"Vigener_decode_file_path")
        self.Vigener_decode_file_path.setMaxLength(999999999)
        self.Vigener_decode_file_path.setReadOnly(True)

        self.gridLayout_10.addWidget(self.Vigener_decode_file_path, 5, 1, 1, 1)

        self.Vigener_input_file_2 = QPushButton(self.podstawieniowy_all_files)
        self.Vigener_input_file_2.setObjectName(u"Vigener_input_file_2")

        self.gridLayout_10.addWidget(self.Vigener_input_file_2, 1, 2, 1, 1)

        self.Vigener_input_key_2 = QLineEdit(self.podstawieniowy_all_files)
        self.Vigener_input_key_2.setObjectName(u"Vigener_input_key_2")
        self.Vigener_input_key_2.setMaxLength(999999999)

        self.gridLayout_10.addWidget(self.Vigener_input_key_2, 2, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(86, 268, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_4, 8, 0, 1, 1)

        self.Vigener_stackedWidget.addWidget(self.podstawieniowy_all_files)

        self.gridLayout_9.addWidget(self.Vigener_stackedWidget, 3, 0, 1, 4)

        self.textEdit = QTextEdit(self.podstawieniowy_page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 75))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.gridLayout_9.addWidget(self.textEdit, 1, 0, 1, 4)

        self.label = QLabel(self.podstawieniowy_page)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_18 = QLabel(self.podstawieniowy_page)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_3.addWidget(self.label_18)

        self.vigener_textMode_button = QPushButton(self.podstawieniowy_page)
        self.vigener_textMode_button.setObjectName(u"vigener_textMode_button")

        self.horizontalLayout_3.addWidget(self.vigener_textMode_button)

        self.vigener_allfilesmode_button = QPushButton(self.podstawieniowy_page)
        self.vigener_allfilesmode_button.setObjectName(u"vigener_allfilesmode_button")

        self.horizontalLayout_3.addWidget(self.vigener_allfilesmode_button)


        self.gridLayout_9.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.stackedWidget.addWidget(self.podstawieniowy_page)
        self.transpozycyjny_page = QWidget()
        self.transpozycyjny_page.setObjectName(u"transpozycyjny_page")
        self.transpozycyjny_page.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gridLayout_3 = QGridLayout(self.transpozycyjny_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.transposition_input_text = QLineEdit(self.transpozycyjny_page)
        self.transposition_input_text.setObjectName(u"transposition_input_text")

        self.gridLayout_3.addWidget(self.transposition_input_text, 3, 1, 1, 1)

        self.label_11 = QLabel(self.transpozycyjny_page)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_13 = QLabel(self.transpozycyjny_page)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 9, 0, 1, 1)

        self.label_14 = QLabel(self.transpozycyjny_page)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 10, 0, 1, 1)

        self.label_10 = QLabel(self.transpozycyjny_page)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 14, 0, 1, 1)

        self.transposition_decode_input_text = QLineEdit(self.transpozycyjny_page)
        self.transposition_decode_input_text.setObjectName(u"transposition_decode_input_text")

        self.gridLayout_3.addWidget(self.transposition_decode_input_text, 9, 1, 1, 1)

        self.transposition_input_file = QPushButton(self.transpozycyjny_page)
        self.transposition_input_file.setObjectName(u"transposition_input_file")

        self.gridLayout_3.addWidget(self.transposition_input_file, 3, 2, 1, 1)

        self.transposition_decode_input_file = QPushButton(self.transpozycyjny_page)
        self.transposition_decode_input_file.setObjectName(u"transposition_decode_input_file")

        self.gridLayout_3.addWidget(self.transposition_decode_input_file, 9, 2, 1, 1)

        self.transposition_decode_input_key = QSpinBox(self.transpozycyjny_page)
        self.transposition_decode_input_key.setObjectName(u"transposition_decode_input_key")
        self.transposition_decode_input_key.setMaximum(1999999999)
        self.transposition_decode_input_key.setValue(31254)

        self.gridLayout_3.addWidget(self.transposition_decode_input_key, 10, 1, 1, 2)

        self.transposition_decode_button = QPushButton(self.transpozycyjny_page)
        self.transposition_decode_button.setObjectName(u"transposition_decode_button")

        self.gridLayout_3.addWidget(self.transposition_decode_button, 12, 0, 1, 3)

        self.label_12 = QLabel(self.transpozycyjny_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_3.addWidget(self.label_12, 8, 0, 1, 3)

        self.transposition_button = QPushButton(self.transpozycyjny_page)
        self.transposition_button.setObjectName(u"transposition_button")

        self.gridLayout_3.addWidget(self.transposition_button, 6, 0, 1, 3)

        self.transposition_input_key = QSpinBox(self.transpozycyjny_page)
        self.transposition_input_key.setObjectName(u"transposition_input_key")
        self.transposition_input_key.setWrapping(False)
        self.transposition_input_key.setFrame(True)
        self.transposition_input_key.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.transposition_input_key.setAccelerated(False)
        self.transposition_input_key.setMaximum(1999999999)
        self.transposition_input_key.setValue(31254)

        self.gridLayout_3.addWidget(self.transposition_input_key, 4, 1, 1, 2)

        self.label_9 = QLabel(self.transpozycyjny_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 3)

        self.textEdit_2 = QTextEdit(self.transpozycyjny_page)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 75))
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.textEdit_2, 1, 0, 1, 3)

        self.label_2 = QLabel(self.transpozycyjny_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 3)

        self.transposition_output = QTextEdit(self.transpozycyjny_page)
        self.transposition_output.setObjectName(u"transposition_output")
        self.transposition_output.setMaximumSize(QSize(16777215, 70))
        self.transposition_output.setReadOnly(True)

        self.gridLayout_3.addWidget(self.transposition_output, 7, 0, 1, 2)

        self.transposition_output_save = QPushButton(self.transpozycyjny_page)
        self.transposition_output_save.setObjectName(u"transposition_output_save")

        self.gridLayout_3.addWidget(self.transposition_output_save, 7, 2, 1, 1)

        self.transposition_decode_output = QTextEdit(self.transpozycyjny_page)
        self.transposition_decode_output.setObjectName(u"transposition_decode_output")
        self.transposition_decode_output.setMaximumSize(QSize(16777215, 70))
        self.transposition_decode_output.setReadOnly(True)

        self.gridLayout_3.addWidget(self.transposition_decode_output, 13, 0, 1, 2)

        self.transposition_decode_output_save = QPushButton(self.transpozycyjny_page)
        self.transposition_decode_output_save.setObjectName(u"transposition_decode_output_save")

        self.gridLayout_3.addWidget(self.transposition_decode_output_save, 13, 2, 1, 1)

        self.stackedWidget.addWidget(self.transpozycyjny_page)
        self.DES_page = QWidget()
        self.DES_page.setObjectName(u"DES_page")
        self.gridLayout_4 = QGridLayout(self.DES_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_16 = QLabel(self.DES_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.des_allFileMode_button = QPushButton(self.DES_page)
        self.des_allFileMode_button.setObjectName(u"des_allFileMode_button")

        self.gridLayout_4.addWidget(self.des_allFileMode_button, 1, 2, 1, 1)

        self.des_normalMode_button = QPushButton(self.DES_page)
        self.des_normalMode_button.setObjectName(u"des_normalMode_button")

        self.gridLayout_4.addWidget(self.des_normalMode_button, 1, 1, 1, 1)

        self.label_26 = QLabel(self.DES_page)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_4.addWidget(self.label_26, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.DES_page)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.des_ecb_radioButton = QRadioButton(self.widget_3)
        self.des_ecb_radioButton.setObjectName(u"des_ecb_radioButton")
        self.des_ecb_radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.des_ecb_radioButton)

        self.des_cbc_radioButton = QRadioButton(self.widget_3)
        self.des_cbc_radioButton.setObjectName(u"des_cbc_radioButton")

        self.horizontalLayout_2.addWidget(self.des_cbc_radioButton)

        self.des_ofb_radioButton = QRadioButton(self.widget_3)
        self.des_ofb_radioButton.setObjectName(u"des_ofb_radioButton")

        self.horizontalLayout_2.addWidget(self.des_ofb_radioButton)

        self.des_cfb_radioButton = QRadioButton(self.widget_3)
        self.des_cfb_radioButton.setObjectName(u"des_cfb_radioButton")

        self.horizontalLayout_2.addWidget(self.des_cfb_radioButton)


        self.gridLayout_4.addWidget(self.widget_3, 0, 1, 1, 2)

        self.stackedWidget_des = QStackedWidget(self.DES_page)
        self.stackedWidget_des.setObjectName(u"stackedWidget_des")
        self.des_normalMode_page = QWidget()
        self.des_normalMode_page.setObjectName(u"des_normalMode_page")
        self.gridLayout_5 = QGridLayout(self.des_normalMode_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Des_input_key = QLineEdit(self.des_normalMode_page)
        self.Des_input_key.setObjectName(u"Des_input_key")

        self.gridLayout_5.addWidget(self.Des_input_key, 2, 1, 1, 2)

        self.Des_decode_input_key = QLineEdit(self.des_normalMode_page)
        self.Des_decode_input_key.setObjectName(u"Des_decode_input_key")

        self.gridLayout_5.addWidget(self.Des_decode_input_key, 7, 1, 1, 2)

        self.label_45 = QLabel(self.des_normalMode_page)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_5.addWidget(self.label_45, 6, 0, 1, 1)

        self.Des_decode_output = QTextEdit(self.des_normalMode_page)
        self.Des_decode_output.setObjectName(u"Des_decode_output")
        self.Des_decode_output.setMaximumSize(QSize(16777215, 70))
        self.Des_decode_output.setReadOnly(True)

        self.gridLayout_5.addWidget(self.Des_decode_output, 9, 0, 1, 2)

        self.Des_decode_output_save = QPushButton(self.des_normalMode_page)
        self.Des_decode_output_save.setObjectName(u"Des_decode_output_save")

        self.gridLayout_5.addWidget(self.Des_decode_output_save, 9, 2, 1, 1)

        self.label_48 = QLabel(self.des_normalMode_page)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.gridLayout_5.addWidget(self.label_48, 0, 0, 1, 3)

        self.Des_output_save = QPushButton(self.des_normalMode_page)
        self.Des_output_save.setObjectName(u"Des_output_save")

        self.gridLayout_5.addWidget(self.Des_output_save, 4, 2, 1, 1)

        self.Des_output = QTextEdit(self.des_normalMode_page)
        self.Des_output.setObjectName(u"Des_output")
        self.Des_output.setMaximumSize(QSize(16777215, 70))
        self.Des_output.setReadOnly(True)

        self.gridLayout_5.addWidget(self.Des_output, 4, 0, 1, 2)

        self.label_47 = QLabel(self.des_normalMode_page)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_5.addWidget(self.label_47, 1, 0, 1, 1)

        self.label_43 = QLabel(self.des_normalMode_page)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_5.addWidget(self.label_43, 7, 0, 1, 1)

        self.Des_decode_input_file = QPushButton(self.des_normalMode_page)
        self.Des_decode_input_file.setObjectName(u"Des_decode_input_file")

        self.gridLayout_5.addWidget(self.Des_decode_input_file, 6, 2, 1, 1)

        self.label_46 = QLabel(self.des_normalMode_page)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_5.addWidget(self.label_46, 2, 0, 1, 1)

        self.Des_button = QPushButton(self.des_normalMode_page)
        self.Des_button.setObjectName(u"Des_button")

        self.gridLayout_5.addWidget(self.Des_button, 3, 0, 1, 3)

        self.Des_input_text = QLineEdit(self.des_normalMode_page)
        self.Des_input_text.setObjectName(u"Des_input_text")

        self.gridLayout_5.addWidget(self.Des_input_text, 1, 1, 1, 1)

        self.Des_decode_input_text = QLineEdit(self.des_normalMode_page)
        self.Des_decode_input_text.setObjectName(u"Des_decode_input_text")

        self.gridLayout_5.addWidget(self.Des_decode_input_text, 6, 1, 1, 1)

        self.Des_decode_button = QPushButton(self.des_normalMode_page)
        self.Des_decode_button.setObjectName(u"Des_decode_button")

        self.gridLayout_5.addWidget(self.Des_decode_button, 8, 0, 1, 3)

        self.label_44 = QLabel(self.des_normalMode_page)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)

        self.gridLayout_5.addWidget(self.label_44, 5, 0, 1, 3)

        self.Des_input_file = QPushButton(self.des_normalMode_page)
        self.Des_input_file.setObjectName(u"Des_input_file")

        self.gridLayout_5.addWidget(self.Des_input_file, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 10, 0, 1, 1)

        self.stackedWidget_des.addWidget(self.des_normalMode_page)
        self.des_allFileMode_page = QWidget()
        self.des_allFileMode_page.setObjectName(u"des_allFileMode_page")
        self.gridLayout_12 = QGridLayout(self.des_allFileMode_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Des_input_file_2 = QPushButton(self.des_allFileMode_page)
        self.Des_input_file_2.setObjectName(u"Des_input_file_2")

        self.gridLayout_12.addWidget(self.Des_input_file_2, 1, 2, 1, 1)

        self.label_59 = QLabel(self.des_allFileMode_page)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_12.addWidget(self.label_59, 2, 0, 1, 1)

        self.Des_file_path = QLineEdit(self.des_allFileMode_page)
        self.Des_file_path.setObjectName(u"Des_file_path")
        self.Des_file_path.setReadOnly(True)

        self.gridLayout_12.addWidget(self.Des_file_path, 1, 1, 1, 1)

        self.Des_button_2 = QPushButton(self.des_allFileMode_page)
        self.Des_button_2.setObjectName(u"Des_button_2")

        self.gridLayout_12.addWidget(self.Des_button_2, 3, 0, 1, 3)

        self.label_60 = QLabel(self.des_allFileMode_page)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font)

        self.gridLayout_12.addWidget(self.label_60, 0, 0, 1, 3)

        self.Des_decode_file_path = QLineEdit(self.des_allFileMode_page)
        self.Des_decode_file_path.setObjectName(u"Des_decode_file_path")
        self.Des_decode_file_path.setReadOnly(True)

        self.gridLayout_12.addWidget(self.Des_decode_file_path, 5, 1, 1, 1)

        self.Des_decode_button_2 = QPushButton(self.des_allFileMode_page)
        self.Des_decode_button_2.setObjectName(u"Des_decode_button_2")

        self.gridLayout_12.addWidget(self.Des_decode_button_2, 7, 0, 1, 3)

        self.Des_decode_input_file_2 = QPushButton(self.des_allFileMode_page)
        self.Des_decode_input_file_2.setObjectName(u"Des_decode_input_file_2")

        self.gridLayout_12.addWidget(self.Des_decode_input_file_2, 5, 2, 1, 1)

        self.label_56 = QLabel(self.des_allFileMode_page)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_12.addWidget(self.label_56, 6, 0, 1, 1)

        self.label_57 = QLabel(self.des_allFileMode_page)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_12.addWidget(self.label_57, 5, 0, 1, 1)

        self.label_58 = QLabel(self.des_allFileMode_page)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_12.addWidget(self.label_58, 1, 0, 1, 1)

        self.Des_decode_input_key_2 = QLineEdit(self.des_allFileMode_page)
        self.Des_decode_input_key_2.setObjectName(u"Des_decode_input_key_2")

        self.gridLayout_12.addWidget(self.Des_decode_input_key_2, 6, 1, 1, 2)

        self.Des_input_key_2 = QLineEdit(self.des_allFileMode_page)
        self.Des_input_key_2.setObjectName(u"Des_input_key_2")

        self.gridLayout_12.addWidget(self.Des_input_key_2, 2, 1, 1, 2)

        self.label_55 = QLabel(self.des_allFileMode_page)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.gridLayout_12.addWidget(self.label_55, 4, 0, 1, 3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_5, 8, 0, 1, 1)

        self.stackedWidget_des.addWidget(self.des_allFileMode_page)

        self.gridLayout_4.addWidget(self.stackedWidget_des, 2, 0, 1, 4)

        self.stackedWidget.addWidget(self.DES_page)
        self.AES_page = QWidget()
        self.AES_page.setObjectName(u"AES_page")
        self.gridLayout_8 = QGridLayout(self.AES_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_27 = QLabel(self.AES_page)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_8.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_28 = QLabel(self.AES_page)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)

        self.gridLayout_8.addWidget(self.label_28, 0, 0, 1, 1)

        self.aes_allFileMode_button = QPushButton(self.AES_page)
        self.aes_allFileMode_button.setObjectName(u"aes_allFileMode_button")

        self.gridLayout_8.addWidget(self.aes_allFileMode_button, 1, 2, 1, 1)

        self.aes_normalMode_button = QPushButton(self.AES_page)
        self.aes_normalMode_button.setObjectName(u"aes_normalMode_button")

        self.gridLayout_8.addWidget(self.aes_normalMode_button, 1, 1, 1, 1)

        self.stackedWidget_aes = QStackedWidget(self.AES_page)
        self.stackedWidget_aes.setObjectName(u"stackedWidget_aes")
        self.aes_normalMode_page = QWidget()
        self.aes_normalMode_page.setObjectName(u"aes_normalMode_page")
        self.gridLayout_7 = QGridLayout(self.aes_normalMode_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Aes_input_key = QLineEdit(self.aes_normalMode_page)
        self.Aes_input_key.setObjectName(u"Aes_input_key")

        self.gridLayout_7.addWidget(self.Aes_input_key, 2, 1, 1, 2)

        self.Aes_decode_input_key = QLineEdit(self.aes_normalMode_page)
        self.Aes_decode_input_key.setObjectName(u"Aes_decode_input_key")

        self.gridLayout_7.addWidget(self.Aes_decode_input_key, 7, 1, 1, 2)

        self.label_49 = QLabel(self.aes_normalMode_page)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_7.addWidget(self.label_49, 6, 0, 1, 1)

        self.Aes_decode_output = QTextEdit(self.aes_normalMode_page)
        self.Aes_decode_output.setObjectName(u"Aes_decode_output")
        self.Aes_decode_output.setMaximumSize(QSize(16777215, 70))
        self.Aes_decode_output.setReadOnly(True)

        self.gridLayout_7.addWidget(self.Aes_decode_output, 9, 0, 1, 2)

        self.Aes_decode_output_save = QPushButton(self.aes_normalMode_page)
        self.Aes_decode_output_save.setObjectName(u"Aes_decode_output_save")

        self.gridLayout_7.addWidget(self.Aes_decode_output_save, 9, 2, 1, 1)

        self.label_50 = QLabel(self.aes_normalMode_page)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)

        self.gridLayout_7.addWidget(self.label_50, 0, 0, 1, 3)

        self.Aes_output_save = QPushButton(self.aes_normalMode_page)
        self.Aes_output_save.setObjectName(u"Aes_output_save")

        self.gridLayout_7.addWidget(self.Aes_output_save, 4, 2, 1, 1)

        self.Aes_output = QTextEdit(self.aes_normalMode_page)
        self.Aes_output.setObjectName(u"Aes_output")
        self.Aes_output.setMaximumSize(QSize(16777215, 70))
        self.Aes_output.setReadOnly(True)

        self.gridLayout_7.addWidget(self.Aes_output, 4, 0, 1, 2)

        self.label_51 = QLabel(self.aes_normalMode_page)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_7.addWidget(self.label_51, 1, 0, 1, 1)

        self.label_52 = QLabel(self.aes_normalMode_page)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_7.addWidget(self.label_52, 7, 0, 1, 1)

        self.Aes_decode_input_file = QPushButton(self.aes_normalMode_page)
        self.Aes_decode_input_file.setObjectName(u"Aes_decode_input_file")

        self.gridLayout_7.addWidget(self.Aes_decode_input_file, 6, 2, 1, 1)

        self.label_53 = QLabel(self.aes_normalMode_page)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_7.addWidget(self.label_53, 2, 0, 1, 1)

        self.Aes_button = QPushButton(self.aes_normalMode_page)
        self.Aes_button.setObjectName(u"Aes_button")

        self.gridLayout_7.addWidget(self.Aes_button, 3, 0, 1, 3)

        self.Aes_input_text = QLineEdit(self.aes_normalMode_page)
        self.Aes_input_text.setObjectName(u"Aes_input_text")

        self.gridLayout_7.addWidget(self.Aes_input_text, 1, 1, 1, 1)

        self.Aes_decode_input_text = QLineEdit(self.aes_normalMode_page)
        self.Aes_decode_input_text.setObjectName(u"Aes_decode_input_text")

        self.gridLayout_7.addWidget(self.Aes_decode_input_text, 6, 1, 1, 1)

        self.Aes_decode_button = QPushButton(self.aes_normalMode_page)
        self.Aes_decode_button.setObjectName(u"Aes_decode_button")

        self.gridLayout_7.addWidget(self.Aes_decode_button, 8, 0, 1, 3)

        self.label_54 = QLabel(self.aes_normalMode_page)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.gridLayout_7.addWidget(self.label_54, 5, 0, 1, 3)

        self.Aes_input_file = QPushButton(self.aes_normalMode_page)
        self.Aes_input_file.setObjectName(u"Aes_input_file")

        self.gridLayout_7.addWidget(self.Aes_input_file, 1, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_8, 10, 0, 1, 1)

        self.stackedWidget_aes.addWidget(self.aes_normalMode_page)
        self.aes_allFileMode_page = QWidget()
        self.aes_allFileMode_page.setObjectName(u"aes_allFileMode_page")
        self.gridLayout_13 = QGridLayout(self.aes_allFileMode_page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Aes_input_file_2 = QPushButton(self.aes_allFileMode_page)
        self.Aes_input_file_2.setObjectName(u"Aes_input_file_2")

        self.gridLayout_13.addWidget(self.Aes_input_file_2, 1, 2, 1, 1)

        self.label_61 = QLabel(self.aes_allFileMode_page)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_13.addWidget(self.label_61, 2, 0, 1, 1)

        self.Aes_file_path = QLineEdit(self.aes_allFileMode_page)
        self.Aes_file_path.setObjectName(u"Aes_file_path")
        self.Aes_file_path.setReadOnly(True)

        self.gridLayout_13.addWidget(self.Aes_file_path, 1, 1, 1, 1)

        self.Aes_button_2 = QPushButton(self.aes_allFileMode_page)
        self.Aes_button_2.setObjectName(u"Aes_button_2")

        self.gridLayout_13.addWidget(self.Aes_button_2, 3, 0, 1, 3)

        self.label_62 = QLabel(self.aes_allFileMode_page)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font)

        self.gridLayout_13.addWidget(self.label_62, 0, 0, 1, 3)

        self.Aes_decode_file_path = QLineEdit(self.aes_allFileMode_page)
        self.Aes_decode_file_path.setObjectName(u"Aes_decode_file_path")
        self.Aes_decode_file_path.setReadOnly(True)

        self.gridLayout_13.addWidget(self.Aes_decode_file_path, 5, 1, 1, 1)

        self.Aes_decode_button_2 = QPushButton(self.aes_allFileMode_page)
        self.Aes_decode_button_2.setObjectName(u"Aes_decode_button_2")

        self.gridLayout_13.addWidget(self.Aes_decode_button_2, 7, 0, 1, 3)

        self.Aes_decode_input_file_2 = QPushButton(self.aes_allFileMode_page)
        self.Aes_decode_input_file_2.setObjectName(u"Aes_decode_input_file_2")

        self.gridLayout_13.addWidget(self.Aes_decode_input_file_2, 5, 2, 1, 1)

        self.label_63 = QLabel(self.aes_allFileMode_page)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_13.addWidget(self.label_63, 6, 0, 1, 1)

        self.label_64 = QLabel(self.aes_allFileMode_page)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_13.addWidget(self.label_64, 5, 0, 1, 1)

        self.label_65 = QLabel(self.aes_allFileMode_page)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_13.addWidget(self.label_65, 1, 0, 1, 1)

        self.Aes_decode_input_key_2 = QLineEdit(self.aes_allFileMode_page)
        self.Aes_decode_input_key_2.setObjectName(u"Aes_decode_input_key_2")

        self.gridLayout_13.addWidget(self.Aes_decode_input_key_2, 6, 1, 1, 2)

        self.Aes_input_key_2 = QLineEdit(self.aes_allFileMode_page)
        self.Aes_input_key_2.setObjectName(u"Aes_input_key_2")

        self.gridLayout_13.addWidget(self.Aes_input_key_2, 2, 1, 1, 2)

        self.label_66 = QLabel(self.aes_allFileMode_page)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font)

        self.gridLayout_13.addWidget(self.label_66, 4, 0, 1, 3)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_9, 8, 0, 1, 1)

        self.stackedWidget_aes.addWidget(self.aes_allFileMode_page)

        self.gridLayout_8.addWidget(self.stackedWidget_aes, 2, 0, 1, 4)

        self.widget_4 = QWidget(self.AES_page)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.aes_ecb_radioButton = QRadioButton(self.widget_4)
        self.aes_ecb_radioButton.setObjectName(u"aes_ecb_radioButton")
        self.aes_ecb_radioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.aes_ecb_radioButton)

        self.aes_cbc_radioButton = QRadioButton(self.widget_4)
        self.aes_cbc_radioButton.setObjectName(u"aes_cbc_radioButton")

        self.horizontalLayout_4.addWidget(self.aes_cbc_radioButton)

        self.aes_ofb_radioButton = QRadioButton(self.widget_4)
        self.aes_ofb_radioButton.setObjectName(u"aes_ofb_radioButton")

        self.horizontalLayout_4.addWidget(self.aes_ofb_radioButton)

        self.aes_cfb_radioButton = QRadioButton(self.widget_4)
        self.aes_cfb_radioButton.setObjectName(u"aes_cfb_radioButton")

        self.horizontalLayout_4.addWidget(self.aes_cfb_radioButton)

        self.aes_gcm_radioButton = QRadioButton(self.widget_4)
        self.aes_gcm_radioButton.setObjectName(u"aes_gcm_radioButton")

        self.horizontalLayout_4.addWidget(self.aes_gcm_radioButton)


        self.gridLayout_8.addWidget(self.widget_4, 0, 1, 1, 2)

        self.stackedWidget.addWidget(self.AES_page)
        self.Network_page = QWidget()
        self.Network_page.setObjectName(u"Network_page")
        self.gridLayout_6 = QGridLayout(self.Network_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.host_user_name = QLabel(self.Network_page)
        self.host_user_name.setObjectName(u"host_user_name")

        self.gridLayout_6.addWidget(self.host_user_name, 0, 1, 1, 2)

        self.network_mode_stackedWidget = QStackedWidget(self.Network_page)
        self.network_mode_stackedWidget.setObjectName(u"network_mode_stackedWidget")
        self.automatic_page = QWidget()
        self.automatic_page.setObjectName(u"automatic_page")
        self.verticalLayout_4 = QVBoxLayout(self.automatic_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.network_search_button = QPushButton(self.automatic_page)
        self.network_search_button.setObjectName(u"network_search_button")

        self.verticalLayout_4.addWidget(self.network_search_button)

        self.devicesList_widget = QWidget(self.automatic_page)
        self.devicesList_widget.setObjectName(u"devicesList_widget")
        self.verticalLayout_8 = QVBoxLayout(self.devicesList_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_8.addLayout(self.verticalLayout_5)


        self.verticalLayout_4.addWidget(self.devicesList_widget)

        self.verticalSpacer_7 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.network_mode_stackedWidget.addWidget(self.automatic_page)
        self.manual_page = QWidget()
        self.manual_page.setObjectName(u"manual_page")
        self.verticalLayout_7 = QVBoxLayout(self.manual_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.network_mode_stackedWidget.addWidget(self.manual_page)

        self.gridLayout_6.addWidget(self.network_mode_stackedWidget, 2, 0, 1, 3)

        self.label_17 = QLabel(self.Network_page)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)

        self.host_user_ip = QLabel(self.Network_page)
        self.host_user_ip.setObjectName(u"host_user_ip")

        self.gridLayout_6.addWidget(self.host_user_ip, 1, 1, 1, 2)

        self.label_25 = QLabel(self.Network_page)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_6.addWidget(self.label_25, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.Network_page)
        self.Rsa_page = QWidget()
        self.Rsa_page.setObjectName(u"Rsa_page")
        self.gridLayout_16 = QGridLayout(self.Rsa_page)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.rsa_normalMode_button = QPushButton(self.Rsa_page)
        self.rsa_normalMode_button.setObjectName(u"rsa_normalMode_button")

        self.gridLayout_16.addWidget(self.rsa_normalMode_button, 1, 1, 1, 1)

        self.label_37 = QLabel(self.Rsa_page)
        self.label_37.setObjectName(u"label_37")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_37.setFont(font1)

        self.gridLayout_16.addWidget(self.label_37, 1, 0, 1, 1)

        self.label_36 = QLabel(self.Rsa_page)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.gridLayout_16.addWidget(self.label_36, 0, 0, 1, 3)

        self.rsa_allFileMode_button = QPushButton(self.Rsa_page)
        self.rsa_allFileMode_button.setObjectName(u"rsa_allFileMode_button")

        self.gridLayout_16.addWidget(self.rsa_allFileMode_button, 1, 2, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_38 = QLabel(self.Rsa_page)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_38)

        self.rsa_keySize = QComboBox(self.Rsa_page)
        self.rsa_keySize.addItem("")
        self.rsa_keySize.addItem("")
        self.rsa_keySize.addItem("")
        self.rsa_keySize.setObjectName(u"rsa_keySize")

        self.horizontalLayout_8.addWidget(self.rsa_keySize)

        self.rsa_generateKey_pushButton = QPushButton(self.Rsa_page)
        self.rsa_generateKey_pushButton.setObjectName(u"rsa_generateKey_pushButton")

        self.horizontalLayout_8.addWidget(self.rsa_generateKey_pushButton)


        self.gridLayout_16.addLayout(self.horizontalLayout_8, 2, 0, 1, 3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_71 = QLabel(self.Rsa_page)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_71)

        self.rsa_publicKey = QLineEdit(self.Rsa_page)
        self.rsa_publicKey.setObjectName(u"rsa_publicKey")

        self.horizontalLayout_7.addWidget(self.rsa_publicKey)

        self.rsa_save_publicKey_pushButton = QPushButton(self.Rsa_page)
        self.rsa_save_publicKey_pushButton.setObjectName(u"rsa_save_publicKey_pushButton")

        self.horizontalLayout_7.addWidget(self.rsa_save_publicKey_pushButton)

        self.rsa_load_publicKey_pushButton = QPushButton(self.Rsa_page)
        self.rsa_load_publicKey_pushButton.setObjectName(u"rsa_load_publicKey_pushButton")

        self.horizontalLayout_7.addWidget(self.rsa_load_publicKey_pushButton)


        self.gridLayout_16.addLayout(self.horizontalLayout_7, 3, 0, 1, 3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_70 = QLabel(self.Rsa_page)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_70)

        self.rsa_privetKey = QLineEdit(self.Rsa_page)
        self.rsa_privetKey.setObjectName(u"rsa_privetKey")

        self.horizontalLayout_6.addWidget(self.rsa_privetKey)

        self.rsa_save_privateKey_pushButton = QPushButton(self.Rsa_page)
        self.rsa_save_privateKey_pushButton.setObjectName(u"rsa_save_privateKey_pushButton")

        self.horizontalLayout_6.addWidget(self.rsa_save_privateKey_pushButton)

        self.rsa_load_privateKey_pushButton = QPushButton(self.Rsa_page)
        self.rsa_load_privateKey_pushButton.setObjectName(u"rsa_load_privateKey_pushButton")

        self.horizontalLayout_6.addWidget(self.rsa_load_privateKey_pushButton)


        self.gridLayout_16.addLayout(self.horizontalLayout_6, 4, 0, 1, 3)

        self.stackedWidget_rsa = QStackedWidget(self.Rsa_page)
        self.stackedWidget_rsa.setObjectName(u"stackedWidget_rsa")
        self.rsa_normalMode_page = QWidget()
        self.rsa_normalMode_page.setObjectName(u"rsa_normalMode_page")
        self.verticalLayout_15 = QVBoxLayout(self.rsa_normalMode_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_39 = QLabel(self.rsa_normalMode_page)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_39)

        self.rsa_plainText = QTextEdit(self.rsa_normalMode_page)
        self.rsa_plainText.setObjectName(u"rsa_plainText")
        self.rsa_plainText.setMinimumSize(QSize(0, 0))
        self.rsa_plainText.setMaximumSize(QSize(16777215, 16777215))
        self.rsa_plainText.setFont(font1)
        self.rsa_plainText.setReadOnly(False)

        self.verticalLayout_13.addWidget(self.rsa_plainText)

        self.rsa_plainText_input_file = QPushButton(self.rsa_normalMode_page)
        self.rsa_plainText_input_file.setObjectName(u"rsa_plainText_input_file")

        self.verticalLayout_13.addWidget(self.rsa_plainText_input_file)

        self.rsa_plainText_save = QPushButton(self.rsa_normalMode_page)
        self.rsa_plainText_save.setObjectName(u"rsa_plainText_save")

        self.verticalLayout_13.addWidget(self.rsa_plainText_save)

        self.verticalLayout_13.setStretch(1, 1)

        self.horizontalLayout_14.addLayout(self.verticalLayout_13)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)

        self.rsa_cipher_button = QPushButton(self.rsa_normalMode_page)
        self.rsa_cipher_button.setObjectName(u"rsa_cipher_button")

        self.verticalLayout_3.addWidget(self.rsa_cipher_button)

        self.rsa_decipher_button = QPushButton(self.rsa_normalMode_page)
        self.rsa_decipher_button.setObjectName(u"rsa_decipher_button")

        self.verticalLayout_3.addWidget(self.rsa_decipher_button)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_3)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_40 = QLabel(self.rsa_normalMode_page)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_40)

        self.rsa_cipherText = QTextEdit(self.rsa_normalMode_page)
        self.rsa_cipherText.setObjectName(u"rsa_cipherText")
        self.rsa_cipherText.setMaximumSize(QSize(16777215, 16777215))
        self.rsa_cipherText.setFont(font1)
        self.rsa_cipherText.setReadOnly(False)

        self.verticalLayout_14.addWidget(self.rsa_cipherText)

        self.rsa_cipherText_input_file = QPushButton(self.rsa_normalMode_page)
        self.rsa_cipherText_input_file.setObjectName(u"rsa_cipherText_input_file")

        self.verticalLayout_14.addWidget(self.rsa_cipherText_input_file)

        self.rsa_cipherText_save = QPushButton(self.rsa_normalMode_page)
        self.rsa_cipherText_save.setObjectName(u"rsa_cipherText_save")

        self.verticalLayout_14.addWidget(self.rsa_cipherText_save)

        self.verticalLayout_14.setStretch(1, 1)

        self.horizontalLayout_14.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_14 = QSpacerItem(208, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_14)

        self.verticalLayout_15.setStretch(0, 1)
        self.stackedWidget_rsa.addWidget(self.rsa_normalMode_page)
        self.rsa_allFileMode_page = QWidget()
        self.rsa_allFileMode_page.setObjectName(u"rsa_allFileMode_page")
        self.verticalLayout_10 = QVBoxLayout(self.rsa_allFileMode_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.rsa_allFileMode_page)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_67 = QLabel(self.widget_5)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_67)

        self.rsa_fileForCypher = QLineEdit(self.widget_5)
        self.rsa_fileForCypher.setObjectName(u"rsa_fileForCypher")
        self.rsa_fileForCypher.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.rsa_fileForCypher)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.rsaCypher_input_file = QPushButton(self.widget_5)
        self.rsaCypher_input_file.setObjectName(u"rsaCypher_input_file")

        self.verticalLayout_11.addWidget(self.rsaCypher_input_file)

        self.rsa_cipherFile_button = QPushButton(self.widget_5)
        self.rsa_cipherFile_button.setObjectName(u"rsa_cipherFile_button")

        self.verticalLayout_11.addWidget(self.rsa_cipherFile_button)


        self.horizontalLayout_13.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_42 = QLabel(self.widget_5)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_5.addWidget(self.label_42)

        self.rsa_fileToDecypher = QLineEdit(self.widget_5)
        self.rsa_fileToDecypher.setObjectName(u"rsa_fileToDecypher")
        self.rsa_fileToDecypher.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.rsa_fileToDecypher)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.rsaDecypher_input_file = QPushButton(self.widget_5)
        self.rsaDecypher_input_file.setObjectName(u"rsaDecypher_input_file")

        self.verticalLayout_12.addWidget(self.rsaDecypher_input_file)

        self.rsa_decipherFile_button = QPushButton(self.widget_5)
        self.rsa_decipherFile_button.setObjectName(u"rsa_decipherFile_button")

        self.verticalLayout_12.addWidget(self.rsa_decipherFile_button)


        self.horizontalLayout_13.addLayout(self.verticalLayout_12)


        self.verticalLayout_10.addWidget(self.widget_5)

        self.verticalSpacer_12 = QSpacerItem(298, 407, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_12)

        self.stackedWidget_rsa.addWidget(self.rsa_allFileMode_page)

        self.gridLayout_16.addWidget(self.stackedWidget_rsa, 5, 0, 1, 3)

        self.stackedWidget.addWidget(self.Rsa_page)
        self.DiffieHellman_page = QWidget()
        self.DiffieHellman_page.setObjectName(u"DiffieHellman_page")
        self.verticalLayout_18 = QVBoxLayout(self.DiffieHellman_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_29 = QLabel(self.DiffieHellman_page)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.verticalLayout_17.addWidget(self.label_29)

        self.textEdit_3 = QTextEdit(self.DiffieHellman_page)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMinimumSize(QSize(0, 0))
        self.textEdit_3.setMaximumSize(QSize(16777215, 75))
        self.textEdit_3.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_3.setLineWidth(0)
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.textEdit_3)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_32 = QLabel(self.DiffieHellman_page)
        self.label_32.setObjectName(u"label_32")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.label_32.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_32)

        self.g_input_lineEdit = QLineEdit(self.DiffieHellman_page)
        self.g_input_lineEdit.setObjectName(u"g_input_lineEdit")

        self.horizontalLayout_10.addWidget(self.g_input_lineEdit)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.label_30 = QLabel(self.DiffieHellman_page)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_30)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_34 = QLabel(self.DiffieHellman_page)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_34)

        self.a_input_lineEdit = QLineEdit(self.DiffieHellman_page)
        self.a_input_lineEdit.setObjectName(u"a_input_lineEdit")

        self.horizontalLayout_11.addWidget(self.a_input_lineEdit)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_15.addLayout(self.verticalLayout_9)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_33 = QLabel(self.DiffieHellman_page)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)

        self.horizontalLayout.addWidget(self.label_33)

        self.p_input_lineEdit = QLineEdit(self.DiffieHellman_page)
        self.p_input_lineEdit.setObjectName(u"p_input_lineEdit")

        self.horizontalLayout.addWidget(self.p_input_lineEdit)


        self.verticalLayout_16.addLayout(self.horizontalLayout)

        self.label_31 = QLabel(self.DiffieHellman_page)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_31)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_35 = QLabel(self.DiffieHellman_page)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_35)

        self.b_input_lineEdit = QLineEdit(self.DiffieHellman_page)
        self.b_input_lineEdit.setObjectName(u"b_input_lineEdit")

        self.horizontalLayout_9.addWidget(self.b_input_lineEdit)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_15.addLayout(self.verticalLayout_16)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)

        self.calculate_diffieHellman_pushButton = QPushButton(self.DiffieHellman_page)
        self.calculate_diffieHellman_pushButton.setObjectName(u"calculate_diffieHellman_pushButton")
        font3 = QFont()
        font3.setPointSize(11)
        self.calculate_diffieHellman_pushButton.setFont(font3)

        self.verticalLayout_17.addWidget(self.calculate_diffieHellman_pushButton)

        self.diffieHellman_output = QTextEdit(self.DiffieHellman_page)
        self.diffieHellman_output.setObjectName(u"diffieHellman_output")
        self.diffieHellman_output.setMinimumSize(QSize(0, 300))
        self.diffieHellman_output.setFont(font3)
        self.diffieHellman_output.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.diffieHellman_output)

        self.verticalSpacer_10 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_10)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.stackedWidget.addWidget(self.DiffieHellman_page)
        self.generateSignature_page = QWidget()
        self.generateSignature_page.setObjectName(u"generateSignature_page")
        self.verticalLayout_21 = QVBoxLayout(self.generateSignature_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_68 = QLabel(self.generateSignature_page)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font3)

        self.verticalLayout_21.addWidget(self.label_68)

        self.nameInput_lineEdit = QLineEdit(self.generateSignature_page)
        self.nameInput_lineEdit.setObjectName(u"nameInput_lineEdit")

        self.verticalLayout_21.addWidget(self.nameInput_lineEdit)

        self.organizationalUnitInput_lineEdit = QLineEdit(self.generateSignature_page)
        self.organizationalUnitInput_lineEdit.setObjectName(u"organizationalUnitInput_lineEdit")

        self.verticalLayout_21.addWidget(self.organizationalUnitInput_lineEdit)

        self.organizationNameInput_lineEdit = QLineEdit(self.generateSignature_page)
        self.organizationNameInput_lineEdit.setObjectName(u"organizationNameInput_lineEdit")

        self.verticalLayout_21.addWidget(self.organizationNameInput_lineEdit)

        self.emailInput_lineEdit = QLineEdit(self.generateSignature_page)
        self.emailInput_lineEdit.setObjectName(u"emailInput_lineEdit")

        self.verticalLayout_21.addWidget(self.emailInput_lineEdit)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_75 = QLabel(self.generateSignature_page)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_16.addWidget(self.label_75)

        self.countryInput_combobox = QComboBox(self.generateSignature_page)
        self.countryInput_combobox.addItem("")
        self.countryInput_combobox.addItem("")
        self.countryInput_combobox.addItem("")
        self.countryInput_combobox.setObjectName(u"countryInput_combobox")

        self.horizontalLayout_16.addWidget(self.countryInput_combobox)

        self.horizontalLayout_16.setStretch(1, 1)

        self.verticalLayout_21.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_76 = QLabel(self.generateSignature_page)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_17.addWidget(self.label_76)

        self.keyAlgoInput_comboBox = QComboBox(self.generateSignature_page)
        self.keyAlgoInput_comboBox.addItem("")
        self.keyAlgoInput_comboBox.addItem("")
        self.keyAlgoInput_comboBox.addItem("")
        self.keyAlgoInput_comboBox.setObjectName(u"keyAlgoInput_comboBox")

        self.horizontalLayout_17.addWidget(self.keyAlgoInput_comboBox)

        self.horizontalLayout_17.setStretch(1, 1)

        self.verticalLayout_21.addLayout(self.horizontalLayout_17)

        self.generateCert_pushButton = QPushButton(self.generateSignature_page)
        self.generateCert_pushButton.setObjectName(u"generateCert_pushButton")

        self.verticalLayout_21.addWidget(self.generateCert_pushButton)

        self.verticalSpacer_15 = QSpacerItem(20, 421, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_15)

        self.stackedWidget.addWidget(self.generateSignature_page)
        self.signDocumen_page = QWidget()
        self.signDocumen_page.setObjectName(u"signDocumen_page")
        self.verticalLayout_22 = QVBoxLayout(self.signDocumen_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_69 = QLabel(self.signDocumen_page)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font3)

        self.verticalLayout_22.addWidget(self.label_69)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pdfPath_lineEdit = QLineEdit(self.signDocumen_page)
        self.pdfPath_lineEdit.setObjectName(u"pdfPath_lineEdit")
        self.pdfPath_lineEdit.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.pdfPath_lineEdit)

        self.loadPdf_pushButton = QPushButton(self.signDocumen_page)
        self.loadPdf_pushButton.setObjectName(u"loadPdf_pushButton")

        self.horizontalLayout_18.addWidget(self.loadPdf_pushButton)


        self.verticalLayout_22.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.privateKeyPath_lineEdit = QLineEdit(self.signDocumen_page)
        self.privateKeyPath_lineEdit.setObjectName(u"privateKeyPath_lineEdit")
        self.privateKeyPath_lineEdit.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.privateKeyPath_lineEdit)

        self.loadPrivateKey_pushButton = QPushButton(self.signDocumen_page)
        self.loadPrivateKey_pushButton.setObjectName(u"loadPrivateKey_pushButton")

        self.horizontalLayout_19.addWidget(self.loadPrivateKey_pushButton)


        self.verticalLayout_22.addLayout(self.horizontalLayout_19)

        self.signDocument_pushButton = QPushButton(self.signDocumen_page)
        self.signDocument_pushButton.setObjectName(u"signDocument_pushButton")

        self.verticalLayout_22.addWidget(self.signDocument_pushButton)

        self.verticalSpacer_16 = QSpacerItem(20, 541, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_16)

        self.stackedWidget.addWidget(self.signDocumen_page)
        self.verifySignature_page = QWidget()
        self.verifySignature_page.setObjectName(u"verifySignature_page")
        self.verticalLayout_23 = QVBoxLayout(self.verifySignature_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_72 = QLabel(self.verifySignature_page)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font3)

        self.verticalLayout_23.addWidget(self.label_72)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pdfPath_lineEdit_2 = QLineEdit(self.verifySignature_page)
        self.pdfPath_lineEdit_2.setObjectName(u"pdfPath_lineEdit_2")
        self.pdfPath_lineEdit_2.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.pdfPath_lineEdit_2)

        self.loadPdf_pushButton_2 = QPushButton(self.verifySignature_page)
        self.loadPdf_pushButton_2.setObjectName(u"loadPdf_pushButton_2")

        self.horizontalLayout_20.addWidget(self.loadPdf_pushButton_2)


        self.verticalLayout_23.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.csrPath_lineEdit = QLineEdit(self.verifySignature_page)
        self.csrPath_lineEdit.setObjectName(u"csrPath_lineEdit")
        self.csrPath_lineEdit.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.csrPath_lineEdit)

        self.loadCsr_pushButton = QPushButton(self.verifySignature_page)
        self.loadCsr_pushButton.setObjectName(u"loadCsr_pushButton")

        self.horizontalLayout_21.addWidget(self.loadCsr_pushButton)


        self.verticalLayout_23.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pemPath_lineEdit = QLineEdit(self.verifySignature_page)
        self.pemPath_lineEdit.setObjectName(u"pemPath_lineEdit")
        self.pemPath_lineEdit.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.pemPath_lineEdit)

        self.loadPem_pushButton = QPushButton(self.verifySignature_page)
        self.loadPem_pushButton.setObjectName(u"loadPem_pushButton")

        self.horizontalLayout_22.addWidget(self.loadPem_pushButton)


        self.verticalLayout_23.addLayout(self.horizontalLayout_22)

        self.verify_pushButton = QPushButton(self.verifySignature_page)
        self.verify_pushButton.setObjectName(u"verify_pushButton")

        self.verticalLayout_23.addWidget(self.verify_pushButton)

        self.verifyOutput_textEdit = QTextEdit(self.verifySignature_page)
        self.verifyOutput_textEdit.setObjectName(u"verifyOutput_textEdit")

        self.verticalLayout_23.addWidget(self.verifyOutput_textEdit)

        self.verticalSpacer_17 = QSpacerItem(20, 250, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_17)

        self.stackedWidget.addWidget(self.verifySignature_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.podstawieniowy_pushButton, self.transpozycyjny_pushButton)
        QWidget.setTabOrder(self.transpozycyjny_pushButton, self.des_pushButton)
        QWidget.setTabOrder(self.des_pushButton, self.aes_pushButton)
        QWidget.setTabOrder(self.aes_pushButton, self.rsa_pushButton)
        QWidget.setTabOrder(self.rsa_pushButton, self.diffieHellman_pushButton)
        QWidget.setTabOrder(self.diffieHellman_pushButton, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.vigener_textMode_button)
        QWidget.setTabOrder(self.vigener_textMode_button, self.vigener_allfilesmode_button)
        QWidget.setTabOrder(self.vigener_allfilesmode_button, self.Vigener_input_text)
        QWidget.setTabOrder(self.Vigener_input_text, self.Vigener_input_file)
        QWidget.setTabOrder(self.Vigener_input_file, self.Vigener_input_key)
        QWidget.setTabOrder(self.Vigener_input_key, self.Vigener_button)
        QWidget.setTabOrder(self.Vigener_button, self.Vigener_output)
        QWidget.setTabOrder(self.Vigener_output, self.Vigener_output_save)
        QWidget.setTabOrder(self.Vigener_output_save, self.Vigener_decode_input_text)
        QWidget.setTabOrder(self.Vigener_decode_input_text, self.Vigener_decode_input_file)
        QWidget.setTabOrder(self.Vigener_decode_input_file, self.Vigener_decode_input_key)
        QWidget.setTabOrder(self.Vigener_decode_input_key, self.Vigener_decode_button)
        QWidget.setTabOrder(self.Vigener_decode_button, self.Vigener_decode_output)
        QWidget.setTabOrder(self.Vigener_decode_output, self.Vigener_decode_output_save)
        QWidget.setTabOrder(self.Vigener_decode_output_save, self.Vigener_file_path)
        QWidget.setTabOrder(self.Vigener_file_path, self.Vigener_input_file_2)
        QWidget.setTabOrder(self.Vigener_input_file_2, self.Vigener_input_key_2)
        QWidget.setTabOrder(self.Vigener_input_key_2, self.Vigener_button_2)
        QWidget.setTabOrder(self.Vigener_button_2, self.Vigener_decode_file_path)
        QWidget.setTabOrder(self.Vigener_decode_file_path, self.Vigener_decode_input_file_2)
        QWidget.setTabOrder(self.Vigener_decode_input_file_2, self.Vigener_decode_input_key_2)
        QWidget.setTabOrder(self.Vigener_decode_input_key_2, self.Vigener_decode_button_2)
        QWidget.setTabOrder(self.Vigener_decode_button_2, self.textEdit_2)
        QWidget.setTabOrder(self.textEdit_2, self.transposition_input_text)
        QWidget.setTabOrder(self.transposition_input_text, self.transposition_input_file)
        QWidget.setTabOrder(self.transposition_input_file, self.transposition_input_key)
        QWidget.setTabOrder(self.transposition_input_key, self.transposition_button)
        QWidget.setTabOrder(self.transposition_button, self.transposition_output)
        QWidget.setTabOrder(self.transposition_output, self.transposition_output_save)
        QWidget.setTabOrder(self.transposition_output_save, self.transposition_decode_input_text)
        QWidget.setTabOrder(self.transposition_decode_input_text, self.transposition_decode_input_file)
        QWidget.setTabOrder(self.transposition_decode_input_file, self.transposition_decode_input_key)
        QWidget.setTabOrder(self.transposition_decode_input_key, self.transposition_decode_button)
        QWidget.setTabOrder(self.transposition_decode_button, self.transposition_decode_output)
        QWidget.setTabOrder(self.transposition_decode_output, self.transposition_decode_output_save)
        QWidget.setTabOrder(self.transposition_decode_output_save, self.des_ecb_radioButton)
        QWidget.setTabOrder(self.des_ecb_radioButton, self.des_cbc_radioButton)
        QWidget.setTabOrder(self.des_cbc_radioButton, self.des_ofb_radioButton)
        QWidget.setTabOrder(self.des_ofb_radioButton, self.des_cfb_radioButton)
        QWidget.setTabOrder(self.des_cfb_radioButton, self.des_normalMode_button)
        QWidget.setTabOrder(self.des_normalMode_button, self.des_allFileMode_button)
        QWidget.setTabOrder(self.des_allFileMode_button, self.Des_input_text)
        QWidget.setTabOrder(self.Des_input_text, self.Des_input_file)
        QWidget.setTabOrder(self.Des_input_file, self.Des_input_key)
        QWidget.setTabOrder(self.Des_input_key, self.Des_button)
        QWidget.setTabOrder(self.Des_button, self.Des_output)
        QWidget.setTabOrder(self.Des_output, self.Des_output_save)
        QWidget.setTabOrder(self.Des_output_save, self.Des_decode_input_text)
        QWidget.setTabOrder(self.Des_decode_input_text, self.Des_decode_input_file)
        QWidget.setTabOrder(self.Des_decode_input_file, self.Des_decode_input_key)
        QWidget.setTabOrder(self.Des_decode_input_key, self.Des_decode_button)
        QWidget.setTabOrder(self.Des_decode_button, self.Des_decode_output)
        QWidget.setTabOrder(self.Des_decode_output, self.Des_decode_output_save)
        QWidget.setTabOrder(self.Des_decode_output_save, self.Des_file_path)
        QWidget.setTabOrder(self.Des_file_path, self.Des_input_file_2)
        QWidget.setTabOrder(self.Des_input_file_2, self.Des_input_key_2)
        QWidget.setTabOrder(self.Des_input_key_2, self.Des_button_2)
        QWidget.setTabOrder(self.Des_button_2, self.Des_decode_file_path)
        QWidget.setTabOrder(self.Des_decode_file_path, self.Des_decode_input_file_2)
        QWidget.setTabOrder(self.Des_decode_input_file_2, self.Des_decode_input_key_2)
        QWidget.setTabOrder(self.Des_decode_input_key_2, self.Des_decode_button_2)
        QWidget.setTabOrder(self.Des_decode_button_2, self.aes_ecb_radioButton)
        QWidget.setTabOrder(self.aes_ecb_radioButton, self.aes_cbc_radioButton)
        QWidget.setTabOrder(self.aes_cbc_radioButton, self.aes_ofb_radioButton)
        QWidget.setTabOrder(self.aes_ofb_radioButton, self.aes_cfb_radioButton)
        QWidget.setTabOrder(self.aes_cfb_radioButton, self.aes_gcm_radioButton)
        QWidget.setTabOrder(self.aes_gcm_radioButton, self.aes_normalMode_button)
        QWidget.setTabOrder(self.aes_normalMode_button, self.aes_allFileMode_button)
        QWidget.setTabOrder(self.aes_allFileMode_button, self.Aes_input_text)
        QWidget.setTabOrder(self.Aes_input_text, self.Aes_input_file)
        QWidget.setTabOrder(self.Aes_input_file, self.Aes_input_key)
        QWidget.setTabOrder(self.Aes_input_key, self.Aes_button)
        QWidget.setTabOrder(self.Aes_button, self.Aes_output)
        QWidget.setTabOrder(self.Aes_output, self.Aes_output_save)
        QWidget.setTabOrder(self.Aes_output_save, self.Aes_decode_input_text)
        QWidget.setTabOrder(self.Aes_decode_input_text, self.Aes_decode_input_file)
        QWidget.setTabOrder(self.Aes_decode_input_file, self.Aes_decode_input_key)
        QWidget.setTabOrder(self.Aes_decode_input_key, self.Aes_decode_button)
        QWidget.setTabOrder(self.Aes_decode_button, self.Aes_decode_output)
        QWidget.setTabOrder(self.Aes_decode_output, self.Aes_decode_output_save)
        QWidget.setTabOrder(self.Aes_decode_output_save, self.Aes_file_path)
        QWidget.setTabOrder(self.Aes_file_path, self.Aes_input_file_2)
        QWidget.setTabOrder(self.Aes_input_file_2, self.Aes_input_key_2)
        QWidget.setTabOrder(self.Aes_input_key_2, self.Aes_button_2)
        QWidget.setTabOrder(self.Aes_button_2, self.Aes_decode_file_path)
        QWidget.setTabOrder(self.Aes_decode_file_path, self.Aes_decode_input_file_2)
        QWidget.setTabOrder(self.Aes_decode_input_file_2, self.Aes_decode_input_key_2)
        QWidget.setTabOrder(self.Aes_decode_input_key_2, self.Aes_decode_button_2)
        QWidget.setTabOrder(self.Aes_decode_button_2, self.rsa_normalMode_button)
        QWidget.setTabOrder(self.rsa_normalMode_button, self.rsa_allFileMode_button)
        QWidget.setTabOrder(self.rsa_allFileMode_button, self.rsa_keySize)
        QWidget.setTabOrder(self.rsa_keySize, self.rsa_generateKey_pushButton)
        QWidget.setTabOrder(self.rsa_generateKey_pushButton, self.rsa_publicKey)
        QWidget.setTabOrder(self.rsa_publicKey, self.rsa_save_publicKey_pushButton)
        QWidget.setTabOrder(self.rsa_save_publicKey_pushButton, self.rsa_load_publicKey_pushButton)
        QWidget.setTabOrder(self.rsa_load_publicKey_pushButton, self.rsa_privetKey)
        QWidget.setTabOrder(self.rsa_privetKey, self.rsa_save_privateKey_pushButton)
        QWidget.setTabOrder(self.rsa_save_privateKey_pushButton, self.rsa_load_privateKey_pushButton)
        QWidget.setTabOrder(self.rsa_load_privateKey_pushButton, self.rsa_plainText)
        QWidget.setTabOrder(self.rsa_plainText, self.rsa_cipherText)
        QWidget.setTabOrder(self.rsa_cipherText, self.rsa_cipher_button)
        QWidget.setTabOrder(self.rsa_cipher_button, self.rsa_decipher_button)
        QWidget.setTabOrder(self.rsa_decipher_button, self.rsa_plainText_input_file)
        QWidget.setTabOrder(self.rsa_plainText_input_file, self.rsa_plainText_save)
        QWidget.setTabOrder(self.rsa_plainText_save, self.rsa_cipherText_input_file)
        QWidget.setTabOrder(self.rsa_cipherText_input_file, self.rsa_cipherText_save)
        QWidget.setTabOrder(self.rsa_cipherText_save, self.textEdit_3)
        QWidget.setTabOrder(self.textEdit_3, self.g_input_lineEdit)
        QWidget.setTabOrder(self.g_input_lineEdit, self.p_input_lineEdit)
        QWidget.setTabOrder(self.p_input_lineEdit, self.a_input_lineEdit)
        QWidget.setTabOrder(self.a_input_lineEdit, self.b_input_lineEdit)
        QWidget.setTabOrder(self.b_input_lineEdit, self.calculate_diffieHellman_pushButton)
        QWidget.setTabOrder(self.calculate_diffieHellman_pushButton, self.diffieHellman_output)
        QWidget.setTabOrder(self.diffieHellman_output, self.rsaCypher_input_file)
        QWidget.setTabOrder(self.rsaCypher_input_file, self.rsa_fileToDecypher)
        QWidget.setTabOrder(self.rsa_fileToDecypher, self.rsa_decipherFile_button)
        QWidget.setTabOrder(self.rsa_decipherFile_button, self.siec_pushButton)
        QWidget.setTabOrder(self.siec_pushButton, self.rsa_cipherFile_button)
        QWidget.setTabOrder(self.rsa_cipherFile_button, self.network_search_button)
        QWidget.setTabOrder(self.network_search_button, self.rsa_fileForCypher)
        QWidget.setTabOrder(self.rsa_fileForCypher, self.rsaDecypher_input_file)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kryptografia i teoria kod\u00f3w - Micha\u0142 Chru\u015blicki", None))
        self.podstawieniowy_pushButton.setText(QCoreApplication.translate("MainWindow", u"Podstawieniowy", None))
        self.transpozycyjny_pushButton.setText(QCoreApplication.translate("MainWindow", u"Transpozycyjny", None))
        self.des_pushButton.setText(QCoreApplication.translate("MainWindow", u"DES", None))
        self.aes_pushButton.setText(QCoreApplication.translate("MainWindow", u"AES", None))
        self.rsa_pushButton.setText(QCoreApplication.translate("MainWindow", u"Rsa", None))
        self.diffieHellman_pushButton.setText(QCoreApplication.translate("MainWindow", u"Diffie-Hellman", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Podpisy cyfrowe", None))
        self.generateSignature_pushButton.setText(QCoreApplication.translate("MainWindow", u"Generowanie", None))
        self.signDocumen_pushButton.setText(QCoreApplication.translate("MainWindow", u"Podpisywanie", None))
        self.verifySignature_pushButton.setText(QCoreApplication.translate("MainWindow", u"Weryfikacja", None))
        self.siec_pushButton.setText(QCoreApplication.translate("MainWindow", u"Sie\u0107", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Chru\u015blicki Micha\u0142", None))
        self.Vigener_decode_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.Vigener_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj Plik", None))
        self.Vigener_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.Vigener_decode_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj Plik", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie:", None))
        self.Vigener_decode_button.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Kodowanie:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tekst jawny:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tekst zaszyfrowany:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Vigener_button.setText(QCoreApplication.translate("MainWindow", u"Zakoduj", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Vigener_decode_button_2.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj i zapisz do dowolnego pliku", None))
        self.Vigener_decode_input_file_2.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj z pliku tekstowego", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Kodowanie:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Za\u0142adowany plik:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Za\u0142adowany plik:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Vigener_button_2.setText(QCoreApplication.translate("MainWindow", u"Zakoduj i zapisz do pliku tekstowego", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie:", None))
        self.Vigener_input_file_2.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj dowolny Plik", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Przyk\u0142ad szyfru polialfabetycznego, symetrycznego, podstawieniowego.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Kolejne znaki informacji szyfrowane s\u0105 przez kolejne znaki klucza. Gdy d\u0142ugo\u015b\u0107 klucza jest mniejsza od d"
                        "\u0142ugo\u015bci wiadomo\u015bci, kolejne znaki klucza pobierane s\u0105 od pocz\u0105tku. </span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Szyfr Vigenere'a (Podstawieniowy):", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tryb Pracy:", None))
        self.vigener_textMode_button.setText(QCoreApplication.translate("MainWindow", u"Pliki tekstowe", None))
        self.vigener_allfilesmode_button.setText(QCoreApplication.translate("MainWindow", u"Wszystkie pliki", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Tekst zaszyfrowany:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tekst jawny:", None))
        self.transposition_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj Plik", None))
        self.transposition_decode_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj Plik", None))
        self.transposition_decode_button.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie:", None))
        self.transposition_button.setText(QCoreApplication.translate("MainWindow", u"Zakoduj", None))
        self.transposition_input_key.setSpecialValueText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Kodowanie:", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">W implementacji kolumnowej, tekst jest dzielony na kolumny na podstawie d\u0142ugo\u015bci klucza, a nast\u0119pnie litery s\u0105 odczytywane w okre\u015blonej kolejno\u015bci wynikaj\u0105cej z posortowanego klucza. W ten spos\u00f3b litery zmieniaj\u0105 swoje pozycje, ale ich warto\u015bci pozostaj\u0105 takie same, co tworzy zaszyfrowany tekst.</span></p></body></"
                        "html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Szyfr Kolumnowy (Przestawieniowy):", None))
        self.transposition_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.transposition_decode_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"DES", None))
        self.des_allFileMode_button.setText(QCoreApplication.translate("MainWindow", u"Wszystkie pliki", None))
        self.des_normalMode_button.setText(QCoreApplication.translate("MainWindow", u"Pliki tekstowe", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Tryb pracy des:", None))
        self.des_ecb_radioButton.setText(QCoreApplication.translate("MainWindow", u"ECB", None))
        self.des_cbc_radioButton.setText(QCoreApplication.translate("MainWindow", u"CBC", None))
        self.des_ofb_radioButton.setText(QCoreApplication.translate("MainWindow", u"OFB", None))
        self.des_cfb_radioButton.setText(QCoreApplication.translate("MainWindow", u"CFB", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Tekst zaszyfrowany:", None))
        self.Des_decode_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Kodowanie:", None))
        self.Des_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Tekst jawny:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_decode_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_button.setText(QCoreApplication.translate("MainWindow", u"Zakoduj", None))
        self.Des_decode_button.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie:", None))
        self.Des_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.Des_input_file_2.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj dowolny Plik", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_button_2.setText(QCoreApplication.translate("MainWindow", u"Zakoduj i zapisz do pliku tekstowego", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Kodowanie:", None))
        self.Des_decode_button_2.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj i zapisz do dowolnego pliku", None))
        self.Des_decode_input_file_2.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj z pliku tekstowego", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Za\u0142adowany plik:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Za\u0142adowany plik:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Tryb pracy aes:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"AES", None))
        self.aes_allFileMode_button.setText(QCoreApplication.translate("MainWindow", u"Wszystkie pliki", None))
        self.aes_normalMode_button.setText(QCoreApplication.translate("MainWindow", u"Pliki tekstowe", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Tekst zaszyfrowany:", None))
        self.Aes_decode_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Kodowanie:", None))
        self.Aes_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Tekst jawny:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Aes_decode_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Aes_button.setText(QCoreApplication.translate("MainWindow", u"Zakoduj", None))
        self.Aes_decode_button.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie:", None))
        self.Aes_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.Aes_input_file_2.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj dowolny Plik", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Aes_button_2.setText(QCoreApplication.translate("MainWindow", u"Zakoduj i zapisz do pliku tekstowego", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Kodowanie:", None))
        self.Aes_decode_button_2.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj i zapisz do dowolnego pliku", None))
        self.Aes_decode_input_file_2.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj z pliku tekstowego", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Za\u0142adowany plik:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Za\u0142adowany plik:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie:", None))
        self.aes_ecb_radioButton.setText(QCoreApplication.translate("MainWindow", u"ECB", None))
        self.aes_cbc_radioButton.setText(QCoreApplication.translate("MainWindow", u"CBC", None))
        self.aes_ofb_radioButton.setText(QCoreApplication.translate("MainWindow", u"OFB", None))
        self.aes_cfb_radioButton.setText(QCoreApplication.translate("MainWindow", u"CFB", None))
        self.aes_gcm_radioButton.setText(QCoreApplication.translate("MainWindow", u"GCM", None))
        self.host_user_name.setText(QCoreApplication.translate("MainWindow", u"Urz\u0105dzenie 1", None))
        self.network_search_button.setText(QCoreApplication.translate("MainWindow", u"Wyszukaj urz\u0105dzenia", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Nazwa urz\u0105dzenia:", None))
        self.host_user_ip.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Adres IP:", None))
        self.rsa_normalMode_button.setText(QCoreApplication.translate("MainWindow", u"Pliki tekstowe", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Tryb pracy rsa:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"RSA", None))
        self.rsa_allFileMode_button.setText(QCoreApplication.translate("MainWindow", u"Wszystkie pliki", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Rozmiar Klucza (bity):", None))
        self.rsa_keySize.setItemText(0, QCoreApplication.translate("MainWindow", u"1024", None))
        self.rsa_keySize.setItemText(1, QCoreApplication.translate("MainWindow", u"2048", None))
        self.rsa_keySize.setItemText(2, QCoreApplication.translate("MainWindow", u"4096", None))

        self.rsa_generateKey_pushButton.setText(QCoreApplication.translate("MainWindow", u"Generuj klucze", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Klucz Publiczny:", None))
        self.rsa_save_publicKey_pushButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.rsa_load_publicKey_pushButton.setText(QCoreApplication.translate("MainWindow", u"Wczytaj", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Klucz Prywatny:", None))
        self.rsa_save_privateKey_pushButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.rsa_load_privateKey_pushButton.setText(QCoreApplication.translate("MainWindow", u"Wczytaj", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Tekst Jawny:", None))
        self.rsa_plainText_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj zawarto\u015b\u0107 pliku", None))
        self.rsa_plainText_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz do pliku", None))
        self.rsa_cipher_button.setText(QCoreApplication.translate("MainWindow", u"Zaszyfruj ->", None))
        self.rsa_decipher_button.setText(QCoreApplication.translate("MainWindow", u"<- Zdeszyfruj", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Tekst Zaszyfrowany:", None))
        self.rsa_cipherText_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj zawarto\u015b\u0107 pliku", None))
        self.rsa_cipherText_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz do pliku", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Plik:", None))
        self.rsaCypher_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.rsa_cipherFile_button.setText(QCoreApplication.translate("MainWindow", u"Zaszyfruj", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Plik:", None))
        self.rsaDecypher_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj z pliku", None))
        self.rsa_decipherFile_button.setText(QCoreApplication.translate("MainWindow", u"Zdeszyfruj", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Diffie\u2013Hellman", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Protoko\u0142 Diffie-Hellmana umo\u017cliwia dw\u00f3m stronom bezpieczn\u0105 wymian\u0119 klucza kryptograficznego przez niezabezpieczony kana\u0142 komunikacyjny. Klucz ten mo\u017ce nast\u0119pnie by\u0107 u\u017cyty do szyfrowania dalszej komunikacji.</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"g:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Alicja", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"a:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"p:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Bob", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"b:", None))
        self.calculate_diffieHellman_pushButton.setText(QCoreApplication.translate("MainWindow", u"Oblicz Klucz", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Wygeneruj Certyfikat wraz z kluczami", None))
        self.nameInput_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Imi\u0119 i Nazwisko", None))
        self.organizationalUnitInput_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Jednostka organizacyjna", None))
        self.organizationNameInput_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nazwa organizacji", None))
        self.emailInput_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Kraj:", None))
        self.countryInput_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"PL", None))
        self.countryInput_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"US", None))
        self.countryInput_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"GB", None))

        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Klucz RSA:", None))
        self.keyAlgoInput_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1024", None))
        self.keyAlgoInput_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2048", None))
        self.keyAlgoInput_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"4096", None))

        self.generateCert_pushButton.setText(QCoreApplication.translate("MainWindow", u"Wygeneruj klucz prywatny, klucz publiczny oraz certyfikat", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Podpisywanie dokumentu PDF", None))
        self.pdfPath_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wybierz plik PDF", None))
        self.loadPdf_pushButton.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.privateKeyPath_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wybierz klucz prywatny", None))
        self.loadPrivateKey_pushButton.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.signDocument_pushButton.setText(QCoreApplication.translate("MainWindow", u"Podpisz dokument", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Analiza podpisu cyfrowego", None))
        self.pdfPath_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wybierz plik PDF", None))
        self.loadPdf_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.csrPath_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wybierz plik podpisu (csr)", None))
        self.loadCsr_pushButton.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.pemPath_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wybierz klucz publiczny (pem)", None))
        self.loadPem_pushButton.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.verify_pushButton.setText(QCoreApplication.translate("MainWindow", u"Zferyfikuj", None))
    # retranslateUi

