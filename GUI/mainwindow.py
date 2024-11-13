# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 600)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_central = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_central.setObjectName("gridLayout_central")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_central.addWidget(self.line, 3, 2, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout_central.addLayout(self.verticalLayout, 1, 2, 1, 2)
        self.horizontalLayout_launch = QtWidgets.QHBoxLayout()
        self.horizontalLayout_launch.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_launch.setObjectName("horizontalLayout_launch")
        self.pushButton_launch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_launch.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_launch.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_launch.setCheckable(True)
        self.pushButton_launch.setObjectName("pushButton_launch")
        self.horizontalLayout_launch.addWidget(self.pushButton_launch)
        self.gridLayout_central.addLayout(self.horizontalLayout_launch, 4, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAcquisitioninfo = QtWidgets.QAction(MainWindow)
        self.actionAcquisitioninfo.setObjectName("actionAcquisitioninfo")
        self.actionParametersinfo = QtWidgets.QAction(MainWindow)
        self.actionParametersinfo.setObjectName("actionParametersinfo")
        self.actionStop_AWG = QtWidgets.QAction(MainWindow)
        self.actionStop_AWG.setObjectName("actionStop_AWG")
        self.actionStop_CC = QtWidgets.QAction(MainWindow)
        self.actionStop_CC.setObjectName("actionStop_CC")
        self.actionExport_config = QtWidgets.QAction(MainWindow)
        self.actionExport_config.setObjectName("actionExport_config")
        self.actionLoad_config = QtWidgets.QAction(MainWindow)
        self.actionLoad_config.setObjectName("actionLoad_config")
        self.actionLaunch_SCT = QtWidgets.QAction(MainWindow)
        self.actionLaunch_SCT.setCheckable(True)
        self.actionLaunch_SCT.setObjectName("actionLaunch_SCT")
        self.actionReset_all = QtWidgets.QAction(MainWindow)
        self.actionReset_all.setCheckable(True)
        self.actionReset_all.setObjectName("actionReset_all")
        self.actionLaunch_for_GCID_only = QtWidgets.QAction(MainWindow)
        self.actionLaunch_for_GCID_only.setCheckable(True)
        self.actionLaunch_for_GCID_only.setObjectName("actionLaunch_for_GCID_only")
        self.actionNativeDialog = QtWidgets.QAction(MainWindow)
        self.actionNativeDialog.setCheckable(True)
        self.actionNativeDialog.setChecked(True)
        self.actionNativeDialog.setObjectName("actionNativeDialog")
        self.actionLaunch_script = QtWidgets.QAction(MainWindow)
        self.actionLaunch_script.setObjectName("actionLaunch_script")

        self.retranslateUi(MainWindow)
        self.pushButton_launch.clicked.connect(MainWindow.launch) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ITCA"))
        self.label.setText(_translate("MainWindow", "Selectionné le type d\'ITCA:"))
        self.label_2.setText(_translate("MainWindow", "Pour créer un nouveau, appuyer sur start sans rien sélectionner."))
        self.pushButton_launch.setText(_translate("MainWindow", "Start"))
        self.actionAcquisitioninfo.setText(_translate("MainWindow", "Acquisition information"))
        self.actionAcquisitioninfo.setIconText(_translate("MainWindow", "Acquisition information"))
        self.actionParametersinfo.setText(_translate("MainWindow", "Parameters information"))
        self.actionStop_AWG.setText(_translate("MainWindow", "Stop AWG"))
        self.actionStop_CC.setText(_translate("MainWindow", "Stop CC"))
        self.actionExport_config.setText(_translate("MainWindow", "Export config"))
        self.actionLoad_config.setText(_translate("MainWindow", "Load config"))
        self.actionLaunch_SCT.setText(_translate("MainWindow", "Launch"))
        self.actionReset_all.setText(_translate("MainWindow", "Reset config"))
        self.actionLaunch_for_GCID_only.setText(_translate("MainWindow", "Launch for GCID only"))
        self.actionNativeDialog.setText(_translate("MainWindow", "Native dialog"))
        self.actionLaunch_script.setText(_translate("MainWindow", "Launch script"))
