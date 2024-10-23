# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'networkDevicesForm.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(491, 110)
        Form.setMaximumSize(QSize(16777215, 110))
        palette = QPalette()
        brush = QBrush(QColor(230, 230, 230, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Form.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.Client_ip_label = QLabel(Form)
        self.Client_ip_label.setObjectName(u"Client_ip_label")
        self.Client_ip_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout.addWidget(self.Client_ip_label, 1, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(145, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.Client_name_label = QLabel(Form)
        self.Client_name_label.setObjectName(u"Client_name_label")
        self.Client_name_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout.addWidget(self.Client_name_label, 0, 1, 1, 1)

        self.Client_status_label = QLabel(Form)
        self.Client_status_label.setObjectName(u"Client_status_label")
        self.Client_status_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout.addWidget(self.Client_status_label, 2, 1, 1, 1)

        self.Client_connect_pushButton = QPushButton(Form)
        self.Client_connect_pushButton.setObjectName(u"Client_connect_pushButton")

        self.gridLayout.addWidget(self.Client_connect_pushButton, 1, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Adres IP:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Stan Po\u0142\u0105czenia:", None))
        self.Client_ip_label.setText(QCoreApplication.translate("Form", u"127.0.0.1", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nazwa u\u017cytkownika:", None))
        self.Client_name_label.setText(QCoreApplication.translate("Form", u"U\u017cytkownik X", None))
        self.Client_status_label.setText(QCoreApplication.translate("Form", u"Dost\u0119pny", None))
        self.Client_connect_pushButton.setText(QCoreApplication.translate("Form", u"Po\u0142\u0105cz", None))
    # retranslateUi

