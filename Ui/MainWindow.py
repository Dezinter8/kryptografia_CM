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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 645)
        MainWindow.setMinimumSize(QSize(600, 400))
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
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.podstawieniowy_page = QWidget()
        self.podstawieniowy_page.setObjectName(u"podstawieniowy_page")
        self.gridLayout_2 = QGridLayout(self.podstawieniowy_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.podstawieniowy_page)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_3 = QLabel(self.podstawieniowy_page)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_7 = QLabel(self.podstawieniowy_page)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 10, 0, 1, 1)

        self.label_8 = QLabel(self.podstawieniowy_page)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 11, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 14, 0, 1, 1)

        self.Vigener_input_text = QLineEdit(self.podstawieniowy_page)
        self.Vigener_input_text.setObjectName(u"Vigener_input_text")

        self.gridLayout_2.addWidget(self.Vigener_input_text, 3, 1, 1, 1)

        self.Vigener_input_file = QPushButton(self.podstawieniowy_page)
        self.Vigener_input_file.setObjectName(u"Vigener_input_file")

        self.gridLayout_2.addWidget(self.Vigener_input_file, 3, 2, 1, 1)

        self.Vigener_input_key = QLineEdit(self.podstawieniowy_page)
        self.Vigener_input_key.setObjectName(u"Vigener_input_key")

        self.gridLayout_2.addWidget(self.Vigener_input_key, 6, 1, 1, 2)

        self.textEdit = QTextEdit(self.podstawieniowy_page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 75))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 3)

        self.label_5 = QLabel(self.podstawieniowy_page)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 3)

        self.label = QLabel(self.podstawieniowy_page)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)

        self.label_6 = QLabel(self.podstawieniowy_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 9, 0, 1, 3)

        self.Vigener_decode_input_key = QLineEdit(self.podstawieniowy_page)
        self.Vigener_decode_input_key.setObjectName(u"Vigener_decode_input_key")

        self.gridLayout_2.addWidget(self.Vigener_decode_input_key, 11, 1, 1, 2)

        self.Vigener_decode_button = QPushButton(self.podstawieniowy_page)
        self.Vigener_decode_button.setObjectName(u"Vigener_decode_button")

        self.gridLayout_2.addWidget(self.Vigener_decode_button, 12, 0, 1, 3)

        self.Vigener_decode_input_text = QLineEdit(self.podstawieniowy_page)
        self.Vigener_decode_input_text.setObjectName(u"Vigener_decode_input_text")

        self.gridLayout_2.addWidget(self.Vigener_decode_input_text, 10, 1, 1, 1)

        self.Vigener_decode_input_file = QPushButton(self.podstawieniowy_page)
        self.Vigener_decode_input_file.setObjectName(u"Vigener_decode_input_file")

        self.gridLayout_2.addWidget(self.Vigener_decode_input_file, 10, 2, 1, 1)

        self.Vigener_decode_output = QTextEdit(self.podstawieniowy_page)
        self.Vigener_decode_output.setObjectName(u"Vigener_decode_output")
        self.Vigener_decode_output.setMaximumSize(QSize(16777215, 70))
        self.Vigener_decode_output.setReadOnly(True)

        self.gridLayout_2.addWidget(self.Vigener_decode_output, 13, 0, 1, 2)

        self.Vigener_decode_output_save = QPushButton(self.podstawieniowy_page)
        self.Vigener_decode_output_save.setObjectName(u"Vigener_decode_output_save")

        self.gridLayout_2.addWidget(self.Vigener_decode_output_save, 13, 2, 1, 1)

        self.Vigener_output = QTextEdit(self.podstawieniowy_page)
        self.Vigener_output.setObjectName(u"Vigener_output")
        self.Vigener_output.setMaximumSize(QSize(16777215, 70))
        self.Vigener_output.setReadOnly(True)

        self.gridLayout_2.addWidget(self.Vigener_output, 8, 0, 1, 2)

        self.Vigener_output_save = QPushButton(self.podstawieniowy_page)
        self.Vigener_output_save.setObjectName(u"Vigener_output_save")

        self.gridLayout_2.addWidget(self.Vigener_output_save, 8, 2, 1, 1)

        self.Vigener_button = QPushButton(self.podstawieniowy_page)
        self.Vigener_button.setObjectName(u"Vigener_button")

        self.gridLayout_2.addWidget(self.Vigener_button, 7, 0, 1, 3)

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
        self.des_cfb_button = QPushButton(self.DES_page)
        self.des_cfb_button.setObjectName(u"des_cfb_button")

        self.gridLayout_4.addWidget(self.des_cfb_button, 2, 4, 1, 1)

        self.des_ofb_button = QPushButton(self.DES_page)
        self.des_ofb_button.setObjectName(u"des_ofb_button")

        self.gridLayout_4.addWidget(self.des_ofb_button, 2, 3, 1, 1)

        self.label_17 = QLabel(self.DES_page)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)

        self.des_ecb_button = QPushButton(self.DES_page)
        self.des_ecb_button.setObjectName(u"des_ecb_button")

        self.gridLayout_4.addWidget(self.des_ecb_button, 2, 1, 1, 1)

        self.textEdit_3 = QTextEdit(self.DES_page)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 75))

        self.gridLayout_4.addWidget(self.textEdit_3, 1, 0, 1, 5)

        self.label_16 = QLabel(self.DES_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 5)

        self.des_cbc_button = QPushButton(self.DES_page)
        self.des_cbc_button.setObjectName(u"des_cbc_button")

        self.gridLayout_4.addWidget(self.des_cbc_button, 2, 2, 1, 1)

        self.stackedWidget_des = QStackedWidget(self.DES_page)
        self.stackedWidget_des.setObjectName(u"stackedWidget_des")
        self.des_ecb_page = QWidget()
        self.des_ecb_page.setObjectName(u"des_ecb_page")
        self.gridLayout_5 = QGridLayout(self.des_ecb_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.des_ecb_page)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.gridLayout_5.addWidget(self.label_48, 0, 0, 1, 3)

        self.label_47 = QLabel(self.des_ecb_page)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_5.addWidget(self.label_47, 1, 0, 1, 1)

        self.Des_ecb_input_text = QLineEdit(self.des_ecb_page)
        self.Des_ecb_input_text.setObjectName(u"Des_ecb_input_text")

        self.gridLayout_5.addWidget(self.Des_ecb_input_text, 1, 1, 1, 1)

        self.Des_ecb_input_file = QPushButton(self.des_ecb_page)
        self.Des_ecb_input_file.setObjectName(u"Des_ecb_input_file")

        self.gridLayout_5.addWidget(self.Des_ecb_input_file, 1, 2, 1, 1)

        self.label_46 = QLabel(self.des_ecb_page)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_5.addWidget(self.label_46, 2, 0, 1, 1)

        self.Des_ecb_input_key = QLineEdit(self.des_ecb_page)
        self.Des_ecb_input_key.setObjectName(u"Des_ecb_input_key")

        self.gridLayout_5.addWidget(self.Des_ecb_input_key, 2, 1, 1, 2)

        self.Des_ecb_button = QPushButton(self.des_ecb_page)
        self.Des_ecb_button.setObjectName(u"Des_ecb_button")

        self.gridLayout_5.addWidget(self.Des_ecb_button, 3, 0, 1, 3)

        self.Des_ecb_output = QTextEdit(self.des_ecb_page)
        self.Des_ecb_output.setObjectName(u"Des_ecb_output")
        self.Des_ecb_output.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_5.addWidget(self.Des_ecb_output, 4, 0, 1, 2)

        self.Des_ecb_output_save = QPushButton(self.des_ecb_page)
        self.Des_ecb_output_save.setObjectName(u"Des_ecb_output_save")

        self.gridLayout_5.addWidget(self.Des_ecb_output_save, 4, 2, 1, 1)

        self.label_44 = QLabel(self.des_ecb_page)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)

        self.gridLayout_5.addWidget(self.label_44, 5, 0, 1, 3)

        self.label_45 = QLabel(self.des_ecb_page)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_5.addWidget(self.label_45, 6, 0, 1, 1)

        self.Des_ecb_decode_input_text = QLineEdit(self.des_ecb_page)
        self.Des_ecb_decode_input_text.setObjectName(u"Des_ecb_decode_input_text")

        self.gridLayout_5.addWidget(self.Des_ecb_decode_input_text, 6, 1, 1, 1)

        self.Des_ecb_decode_input_file = QPushButton(self.des_ecb_page)
        self.Des_ecb_decode_input_file.setObjectName(u"Des_ecb_decode_input_file")

        self.gridLayout_5.addWidget(self.Des_ecb_decode_input_file, 6, 2, 1, 1)

        self.label_43 = QLabel(self.des_ecb_page)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_5.addWidget(self.label_43, 7, 0, 1, 1)

        self.Des_ecb_decode_input_key = QLineEdit(self.des_ecb_page)
        self.Des_ecb_decode_input_key.setObjectName(u"Des_ecb_decode_input_key")

        self.gridLayout_5.addWidget(self.Des_ecb_decode_input_key, 7, 1, 1, 2)

        self.Des_ecb_decode_button = QPushButton(self.des_ecb_page)
        self.Des_ecb_decode_button.setObjectName(u"Des_ecb_decode_button")

        self.gridLayout_5.addWidget(self.Des_ecb_decode_button, 8, 0, 1, 3)

        self.Des_ecb_decode_output = QTextEdit(self.des_ecb_page)
        self.Des_ecb_decode_output.setObjectName(u"Des_ecb_decode_output")
        self.Des_ecb_decode_output.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_5.addWidget(self.Des_ecb_decode_output, 9, 0, 1, 2)

        self.Des_ecb_decode_output_save = QPushButton(self.des_ecb_page)
        self.Des_ecb_decode_output_save.setObjectName(u"Des_ecb_decode_output_save")

        self.gridLayout_5.addWidget(self.Des_ecb_decode_output_save, 9, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 10, 0, 1, 1)

        self.stackedWidget_des.addWidget(self.des_ecb_page)
        self.des_cbc_page = QWidget()
        self.des_cbc_page.setObjectName(u"des_cbc_page")
        self.gridLayout_8 = QGridLayout(self.des_cbc_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.des_cbc_page)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)

        self.gridLayout_8.addWidget(self.label_38, 0, 0, 1, 3)

        self.label_36 = QLabel(self.des_cbc_page)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_8.addWidget(self.label_36, 1, 0, 1, 1)

        self.Des_cbc_input_text = QLineEdit(self.des_cbc_page)
        self.Des_cbc_input_text.setObjectName(u"Des_cbc_input_text")

        self.gridLayout_8.addWidget(self.Des_cbc_input_text, 1, 1, 1, 1)

        self.Des_cbc_input_file = QPushButton(self.des_cbc_page)
        self.Des_cbc_input_file.setObjectName(u"Des_cbc_input_file")

        self.gridLayout_8.addWidget(self.Des_cbc_input_file, 1, 2, 1, 1)

        self.label_39 = QLabel(self.des_cbc_page)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_8.addWidget(self.label_39, 2, 0, 1, 1)

        self.Des_cbc_input_key = QLineEdit(self.des_cbc_page)
        self.Des_cbc_input_key.setObjectName(u"Des_cbc_input_key")

        self.gridLayout_8.addWidget(self.Des_cbc_input_key, 2, 1, 1, 2)

        self.Des_cbc_button = QPushButton(self.des_cbc_page)
        self.Des_cbc_button.setObjectName(u"Des_cbc_button")

        self.gridLayout_8.addWidget(self.Des_cbc_button, 3, 0, 1, 3)

        self.Des_cbc_output = QTextEdit(self.des_cbc_page)
        self.Des_cbc_output.setObjectName(u"Des_cbc_output")
        self.Des_cbc_output.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_8.addWidget(self.Des_cbc_output, 4, 0, 1, 2)

        self.Des_cbc_output_save = QPushButton(self.des_cbc_page)
        self.Des_cbc_output_save.setObjectName(u"Des_cbc_output_save")

        self.gridLayout_8.addWidget(self.Des_cbc_output_save, 4, 2, 1, 1)

        self.label_37 = QLabel(self.des_cbc_page)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.gridLayout_8.addWidget(self.label_37, 5, 0, 1, 3)

        self.label_40 = QLabel(self.des_cbc_page)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_8.addWidget(self.label_40, 6, 0, 1, 1)

        self.Des_cbc_decode_input_text = QLineEdit(self.des_cbc_page)
        self.Des_cbc_decode_input_text.setObjectName(u"Des_cbc_decode_input_text")

        self.gridLayout_8.addWidget(self.Des_cbc_decode_input_text, 6, 1, 1, 1)

        self.Des_cbc_decode_input_file = QPushButton(self.des_cbc_page)
        self.Des_cbc_decode_input_file.setObjectName(u"Des_cbc_decode_input_file")

        self.gridLayout_8.addWidget(self.Des_cbc_decode_input_file, 6, 2, 1, 1)

        self.label_41 = QLabel(self.des_cbc_page)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_8.addWidget(self.label_41, 7, 0, 1, 1)

        self.Des_cbc_decode_input_key = QLineEdit(self.des_cbc_page)
        self.Des_cbc_decode_input_key.setObjectName(u"Des_cbc_decode_input_key")

        self.gridLayout_8.addWidget(self.Des_cbc_decode_input_key, 7, 1, 1, 2)

        self.Des_cbc_decode_button = QPushButton(self.des_cbc_page)
        self.Des_cbc_decode_button.setObjectName(u"Des_cbc_decode_button")

        self.gridLayout_8.addWidget(self.Des_cbc_decode_button, 8, 0, 1, 3)

        self.Des_cbc_decode_output = QTextEdit(self.des_cbc_page)
        self.Des_cbc_decode_output.setObjectName(u"Des_cbc_decode_output")
        self.Des_cbc_decode_output.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_8.addWidget(self.Des_cbc_decode_output, 9, 0, 1, 2)

        self.Des_cbc_decode_output_save = QPushButton(self.des_cbc_page)
        self.Des_cbc_decode_output_save.setObjectName(u"Des_cbc_decode_output_save")

        self.gridLayout_8.addWidget(self.Des_cbc_decode_output_save, 9, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_7, 10, 0, 1, 1)

        self.stackedWidget_des.addWidget(self.des_cbc_page)
        self.des_ofb_page = QWidget()
        self.des_ofb_page.setObjectName(u"des_ofb_page")
        self.gridLayout_6 = QGridLayout(self.des_ofb_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.des_ofb_page)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.gridLayout_6.addWidget(self.label_54, 0, 0, 1, 3)

        self.label_53 = QLabel(self.des_ofb_page)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_6.addWidget(self.label_53, 1, 0, 1, 1)

        self.Des_ofb_input_text = QLineEdit(self.des_ofb_page)
        self.Des_ofb_input_text.setObjectName(u"Des_ofb_input_text")

        self.gridLayout_6.addWidget(self.Des_ofb_input_text, 1, 1, 1, 1)

        self.Des_ofb_input_file = QPushButton(self.des_ofb_page)
        self.Des_ofb_input_file.setObjectName(u"Des_ofb_input_file")

        self.gridLayout_6.addWidget(self.Des_ofb_input_file, 1, 2, 1, 1)

        self.label_52 = QLabel(self.des_ofb_page)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_6.addWidget(self.label_52, 2, 0, 1, 1)

        self.Des_ofb_input_key = QLineEdit(self.des_ofb_page)
        self.Des_ofb_input_key.setObjectName(u"Des_ofb_input_key")

        self.gridLayout_6.addWidget(self.Des_ofb_input_key, 2, 1, 1, 2)

        self.Des_ofb_button = QPushButton(self.des_ofb_page)
        self.Des_ofb_button.setObjectName(u"Des_ofb_button")

        self.gridLayout_6.addWidget(self.Des_ofb_button, 3, 0, 1, 3)

        self.Des_ofb_output = QTextEdit(self.des_ofb_page)
        self.Des_ofb_output.setObjectName(u"Des_ofb_output")
        self.Des_ofb_output.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_6.addWidget(self.Des_ofb_output, 4, 0, 1, 2)

        self.Des_ofb_output_save = QPushButton(self.des_ofb_page)
        self.Des_ofb_output_save.setObjectName(u"Des_ofb_output_save")

        self.gridLayout_6.addWidget(self.Des_ofb_output_save, 4, 2, 1, 1)

        self.label_50 = QLabel(self.des_ofb_page)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)

        self.gridLayout_6.addWidget(self.label_50, 5, 0, 1, 3)

        self.label_51 = QLabel(self.des_ofb_page)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_6.addWidget(self.label_51, 6, 0, 1, 1)

        self.Des_ofb_decode_input_text = QLineEdit(self.des_ofb_page)
        self.Des_ofb_decode_input_text.setObjectName(u"Des_ofb_decode_input_text")

        self.gridLayout_6.addWidget(self.Des_ofb_decode_input_text, 6, 1, 1, 1)

        self.Des_ofb_decode_input_file = QPushButton(self.des_ofb_page)
        self.Des_ofb_decode_input_file.setObjectName(u"Des_ofb_decode_input_file")

        self.gridLayout_6.addWidget(self.Des_ofb_decode_input_file, 6, 2, 1, 1)

        self.label_49 = QLabel(self.des_ofb_page)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_6.addWidget(self.label_49, 7, 0, 1, 1)

        self.Des_ofb_decode_input_key = QLineEdit(self.des_ofb_page)
        self.Des_ofb_decode_input_key.setObjectName(u"Des_ofb_decode_input_key")

        self.gridLayout_6.addWidget(self.Des_ofb_decode_input_key, 7, 1, 1, 2)

        self.Des_ofb_decode_button = QPushButton(self.des_ofb_page)
        self.Des_ofb_decode_button.setObjectName(u"Des_ofb_decode_button")

        self.gridLayout_6.addWidget(self.Des_ofb_decode_button, 8, 0, 1, 3)

        self.Des_ofb_decode_output = QTextEdit(self.des_ofb_page)
        self.Des_ofb_decode_output.setObjectName(u"Des_ofb_decode_output")
        self.Des_ofb_decode_output.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_6.addWidget(self.Des_ofb_decode_output, 9, 0, 1, 2)

        self.Des_ofb_decode_output_save = QPushButton(self.des_ofb_page)
        self.Des_ofb_decode_output_save.setObjectName(u"Des_ofb_decode_output_save")

        self.gridLayout_6.addWidget(self.Des_ofb_decode_output_save, 9, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_9, 10, 0, 1, 1)

        self.stackedWidget_des.addWidget(self.des_ofb_page)
        self.des_cfb_page = QWidget()
        self.des_cfb_page.setObjectName(u"des_cfb_page")
        self.gridLayout_7 = QGridLayout(self.des_cfb_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.des_cfb_page)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.gridLayout_7.addWidget(self.label_32, 0, 0, 1, 3)

        self.label_30 = QLabel(self.des_cfb_page)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 1, 0, 1, 1)

        self.Des_cfb_input_text = QLineEdit(self.des_cfb_page)
        self.Des_cfb_input_text.setObjectName(u"Des_cfb_input_text")

        self.gridLayout_7.addWidget(self.Des_cfb_input_text, 1, 1, 1, 1)

        self.Des_cfb_input_file = QPushButton(self.des_cfb_page)
        self.Des_cfb_input_file.setObjectName(u"Des_cfb_input_file")

        self.gridLayout_7.addWidget(self.Des_cfb_input_file, 1, 2, 1, 1)

        self.label_33 = QLabel(self.des_cfb_page)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_7.addWidget(self.label_33, 2, 0, 1, 1)

        self.Des_cfb_input_key = QLineEdit(self.des_cfb_page)
        self.Des_cfb_input_key.setObjectName(u"Des_cfb_input_key")

        self.gridLayout_7.addWidget(self.Des_cfb_input_key, 2, 1, 1, 2)

        self.Des_cfb_button = QPushButton(self.des_cfb_page)
        self.Des_cfb_button.setObjectName(u"Des_cfb_button")

        self.gridLayout_7.addWidget(self.Des_cfb_button, 3, 0, 1, 3)

        self.Des_cfb_output = QTextEdit(self.des_cfb_page)
        self.Des_cfb_output.setObjectName(u"Des_cfb_output")
        self.Des_cfb_output.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_7.addWidget(self.Des_cfb_output, 4, 0, 1, 2)

        self.Des_cfb_output_save = QPushButton(self.des_cfb_page)
        self.Des_cfb_output_save.setObjectName(u"Des_cfb_output_save")

        self.gridLayout_7.addWidget(self.Des_cfb_output_save, 4, 2, 1, 1)

        self.label_31 = QLabel(self.des_cfb_page)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.gridLayout_7.addWidget(self.label_31, 5, 0, 1, 3)

        self.label_34 = QLabel(self.des_cfb_page)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_7.addWidget(self.label_34, 6, 0, 1, 1)

        self.Des_cfb_decode_input_text = QLineEdit(self.des_cfb_page)
        self.Des_cfb_decode_input_text.setObjectName(u"Des_cfb_decode_input_text")

        self.gridLayout_7.addWidget(self.Des_cfb_decode_input_text, 6, 1, 1, 1)

        self.Des_cfb_decode_input_file = QPushButton(self.des_cfb_page)
        self.Des_cfb_decode_input_file.setObjectName(u"Des_cfb_decode_input_file")

        self.gridLayout_7.addWidget(self.Des_cfb_decode_input_file, 6, 2, 1, 1)

        self.label_35 = QLabel(self.des_cfb_page)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_7.addWidget(self.label_35, 7, 0, 1, 1)

        self.Des_cfb_decode_input_key = QLineEdit(self.des_cfb_page)
        self.Des_cfb_decode_input_key.setObjectName(u"Des_cfb_decode_input_key")

        self.gridLayout_7.addWidget(self.Des_cfb_decode_input_key, 7, 1, 1, 2)

        self.Des_cfb_decode_button = QPushButton(self.des_cfb_page)
        self.Des_cfb_decode_button.setObjectName(u"Des_cfb_decode_button")

        self.gridLayout_7.addWidget(self.Des_cfb_decode_button, 8, 0, 1, 3)

        self.Des_cfb_decode_output = QTextEdit(self.des_cfb_page)
        self.Des_cfb_decode_output.setObjectName(u"Des_cfb_decode_output")
        self.Des_cfb_decode_output.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_7.addWidget(self.Des_cfb_decode_output, 9, 0, 1, 2)

        self.Des_cfb_decode_output_save = QPushButton(self.des_cfb_page)
        self.Des_cfb_decode_output_save.setObjectName(u"Des_cfb_decode_output_save")

        self.gridLayout_7.addWidget(self.Des_cfb_decode_output_save, 9, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 52, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_6, 10, 0, 1, 1)

        self.stackedWidget_des.addWidget(self.des_cfb_page)

        self.gridLayout_4.addWidget(self.stackedWidget_des, 3, 0, 1, 5)

        self.stackedWidget.addWidget(self.DES_page)
        self.AES_page = QWidget()
        self.AES_page.setObjectName(u"AES_page")
        self.label_42 = QLabel(self.AES_page)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(130, 230, 49, 16))
        self.stackedWidget.addWidget(self.AES_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

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

        self.verticalSpacer = QSpacerItem(20, 403, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout.addWidget(self.label_15)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.podstawieniowy_pushButton, self.transpozycyjny_pushButton)
        QWidget.setTabOrder(self.transpozycyjny_pushButton, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.Vigener_input_text)
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
        QWidget.setTabOrder(self.Vigener_decode_output_save, self.textEdit_2)
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

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kryptografia i teoria kod\u00f3w - Micha\u0142 Chru\u015blicki", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tekst jawny:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tekst zaszyfrowany:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Vigener_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj Plik", None))
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Kodowanie:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Szyfr Vigenere'a (Podstawieniowy):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie:", None))
        self.Vigener_decode_button.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj", None))
        self.Vigener_decode_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj Plik", None))
        self.Vigener_decode_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.Vigener_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.Vigener_button.setText(QCoreApplication.translate("MainWindow", u"Zakoduj", None))
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
        self.des_cfb_button.setText(QCoreApplication.translate("MainWindow", u"CFB", None))
        self.des_ofb_button.setText(QCoreApplication.translate("MainWindow", u"OFB", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Tryb pracy:", None))
        self.des_ecb_button.setText(QCoreApplication.translate("MainWindow", u"ECB", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">Test</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"DES", None))
        self.des_cbc_button.setText(QCoreApplication.translate("MainWindow", u"CBC", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Kodowanie (ECB):", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Tekst jawny:", None))
        self.Des_ecb_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_ecb_button.setText(QCoreApplication.translate("MainWindow", u"Zakoduj", None))
        self.Des_ecb_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie (ECB):", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Tekst zaszyfrowany:", None))
        self.Des_ecb_decode_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_ecb_decode_button.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj", None))
        self.Des_ecb_decode_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Kodowanie (CBC):", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Tekst jawny:", None))
        self.Des_cbc_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_cbc_button.setText(QCoreApplication.translate("MainWindow", u"Zakoduj", None))
        self.Des_cbc_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie (CBC):", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Tekst zaszyfrowany:", None))
        self.Des_cbc_decode_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_cbc_decode_button.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj", None))
        self.Des_cbc_decode_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Kodowanie (OFB):", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Tekst jawny:", None))
        self.Des_ofb_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_ofb_button.setText(QCoreApplication.translate("MainWindow", u"Zakoduj", None))
        self.Des_ofb_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie (OFB):", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Tekst zaszyfrowany:", None))
        self.Des_ofb_decode_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_ofb_decode_button.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj", None))
        self.Des_ofb_decode_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Kodowanie (CFB):", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Tekst jawny:", None))
        self.Des_cfb_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_cfb_button.setText(QCoreApplication.translate("MainWindow", u"Zakoduj", None))
        self.Des_cfb_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Dekodowanie (CFB):", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Tekst zaszyfrowany:", None))
        self.Des_cfb_decode_input_file.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Klucz:", None))
        self.Des_cfb_decode_button.setText(QCoreApplication.translate("MainWindow", u"Zdekoduj", None))
        self.Des_cfb_decode_output_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"AES", None))
        self.podstawieniowy_pushButton.setText(QCoreApplication.translate("MainWindow", u"Podstawieniowy", None))
        self.transpozycyjny_pushButton.setText(QCoreApplication.translate("MainWindow", u"Transpozycyjny", None))
        self.des_pushButton.setText(QCoreApplication.translate("MainWindow", u"DES", None))
        self.aes_pushButton.setText(QCoreApplication.translate("MainWindow", u"AES", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Chru\u015blicki Micha\u0142", None))
    # retranslateUi

