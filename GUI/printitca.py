# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printitca.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(1000, 1000)
        Dialog.setMinimumSize(QtCore.QSize(1000, 1000))
        Dialog.setMaximumSize(QtCore.QSize(2000, 1500))
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_data = QtWidgets.QVBoxLayout()
        self.verticalLayout_data.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_data.setObjectName("verticalLayout_data")
        self.horizontal_1 = QtWidgets.QHBoxLayout()
        self.horizontal_1.setObjectName("horizontal_1")
        self.label_moms = QtWidgets.QLabel(Dialog)
        self.label_moms.setObjectName("label_moms")
        self.horizontal_1.addWidget(self.label_moms, 0, QtCore.Qt.AlignHCenter)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontal_1.addWidget(self.line_2)
        self.label_itca = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_itca.setFont(font)
        self.label_itca.setObjectName("label_itca")
        self.horizontal_1.addWidget(self.label_itca, 0, QtCore.Qt.AlignHCenter)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontal_1.addWidget(self.line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_itca_number = QtWidgets.QLabel(Dialog)
        self.label_itca_number.setObjectName("label_itca_number")
        self.verticalLayout_3.addWidget(self.label_itca_number, 0, QtCore.Qt.AlignHCenter)
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.label_page = QtWidgets.QLabel(Dialog)
        self.label_page.setObjectName("label_page")
        self.verticalLayout_3.addWidget(self.label_page, 0, QtCore.Qt.AlignHCenter)
        self.horizontal_1.addLayout(self.verticalLayout_3)
        self.verticalLayout_data.addLayout(self.horizontal_1)
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_data.addWidget(self.line_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_emetteur = QtWidgets.QLabel(Dialog)
        self.label_emetteur.setObjectName("label_emetteur")
        self.horizontalLayout.addWidget(self.label_emetteur, 0, QtCore.Qt.AlignHCenter)
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout.addWidget(self.line_6)
        self.label_qualite = QtWidgets.QLabel(Dialog)
        self.label_qualite.setObjectName("label_qualite")
        self.horizontalLayout.addWidget(self.label_qualite, 0, QtCore.Qt.AlignHCenter)
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout.addWidget(self.line_7)
        self.label_visa = QtWidgets.QLabel(Dialog)
        self.label_visa.setObjectName("label_visa")
        self.horizontalLayout.addWidget(self.label_visa, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_data.addLayout(self.horizontalLayout)
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_data.addWidget(self.line_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_intervention = QtWidgets.QLabel(Dialog)
        self.label_intervention.setObjectName("label_intervention")
        self.verticalLayout_4.addWidget(self.label_intervention, 0, QtCore.Qt.AlignHCenter)
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_4.addWidget(self.line_8)
        self.label_ref_doc = QtWidgets.QLabel(Dialog)
        self.label_ref_doc.setObjectName("label_ref_doc")
        self.verticalLayout_4.addWidget(self.label_ref_doc, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.line_16 = QtWidgets.QFrame(Dialog)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.horizontalLayout_2.addWidget(self.line_16)
        self.label_pixmap = QtWidgets.QLabel(Dialog)
        self.label_pixmap.setMinimumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_pixmap.setFont(font)
        self.label_pixmap.setObjectName("label_pixmap")
        self.horizontalLayout_2.addWidget(self.label_pixmap, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_data.addLayout(self.horizontalLayout_2)
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_data.addWidget(self.line_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_etape = QtWidgets.QLabel(Dialog)
        self.label_etape.setObjectName("label_etape")
        self.horizontalLayout_3.addWidget(self.label_etape, 0, QtCore.Qt.AlignHCenter)
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_3.addWidget(self.line_11)
        self.label_mot = QtWidgets.QLabel(Dialog)
        self.label_mot.setObjectName("label_mot")
        self.horizontalLayout_3.addWidget(self.label_mot, 0, QtCore.Qt.AlignHCenter)
        self.line_12 = QtWidgets.QFrame(Dialog)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_3.addWidget(self.line_12)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_lru = QtWidgets.QLabel(Dialog)
        self.label_lru.setObjectName("label_lru")
        self.verticalLayout_5.addWidget(self.label_lru, 0, QtCore.Qt.AlignHCenter)
        self.line_14 = QtWidgets.QFrame(Dialog)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_5.addWidget(self.line_14)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_position_mot = QtWidgets.QLabel(Dialog)
        self.label_position_mot.setObjectName("label_position_mot")
        self.horizontalLayout_5.addWidget(self.label_position_mot, 0, QtCore.Qt.AlignHCenter)
        self.line_13 = QtWidgets.QFrame(Dialog)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_5.addWidget(self.line_13)
        self.label_av = QtWidgets.QLabel(Dialog)
        self.label_av.setObjectName("label_av")
        self.horizontalLayout_5.addWidget(self.label_av, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_data.addLayout(self.horizontalLayout_3)
        self.line_15 = QtWidgets.QFrame(Dialog)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_data.addWidget(self.line_15)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_data.addItem(spacerItem)
        self.verticalLayout.addLayout(self.verticalLayout_data)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setMinimumSize(QtCore.QSize(0, 3))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_cmd = QtWidgets.QHBoxLayout()
        self.horizontalLayout_cmd.setObjectName("horizontalLayout_cmd")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_cmd.addItem(spacerItem1)
        self.pushButton_itca = QtWidgets.QPushButton(Dialog)
        self.pushButton_itca.setObjectName("pushButton_itca")
        self.horizontalLayout_cmd.addWidget(self.pushButton_itca)
        self.pushButton_pdf = QtWidgets.QPushButton(Dialog)
        self.pushButton_pdf.setObjectName("pushButton_pdf")
        self.horizontalLayout_cmd.addWidget(self.pushButton_pdf)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_cmd.addWidget(self.pushButton_cancel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_cmd.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_cmd)

        self.retranslateUi(Dialog)
        self.pushButton_cancel.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton_pdf, self.pushButton_cancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NEW ITCA"))
        self.label_moms.setText(_translate("Dialog", "MOMS"))
        self.label_itca.setText(_translate("Dialog", "ITCA"))
        self.label_itca_number.setText(_translate("Dialog", "ITCA-N°XXXX"))
        self.label_page.setText(_translate("Dialog", "PAGE N°1"))
        self.label_emetteur.setText(_translate("Dialog", "EMETTEUR"))
        self.label_qualite.setText(_translate("Dialog", "QUALITE"))
        self.label_visa.setText(_translate("Dialog", "VISA"))
        self.label_intervention.setText(_translate("Dialog", "Essaie/inspection/intervention"))
        self.label_ref_doc.setText(_translate("Dialog", "REF DOC"))
        self.label_pixmap.setText(_translate("Dialog", "NO PICTURES"))
        self.label_etape.setText(_translate("Dialog", "ETAPE 4 "))
        self.label_mot.setText(_translate("Dialog", "WM000XXX"))
        self.label_lru.setText(_translate("Dialog", "Nom de l\'équipement ou LRU"))
        self.label_position_mot.setText(_translate("Dialog", "Position MOT"))
        self.label_av.setText(_translate("Dialog", "AV"))
        self.pushButton_itca.setText(_translate("Dialog", "SAVE ITCA"))
        self.pushButton_pdf.setText(_translate("Dialog", "SAVE PDF"))
        self.pushButton_cancel.setText(_translate("Dialog", "Close"))