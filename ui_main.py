# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_drone.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_record = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_record.setObjectName("radioButton_record")
        self.horizontalLayout_2.addWidget(self.radioButton_record)
        self.radioButton_norecord = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_norecord.setChecked(True)
        self.radioButton_norecord.setObjectName("radioButton_norecord")
        self.horizontalLayout_2.addWidget(self.radioButton_norecord)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_9)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_9)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_backward = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_backward.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_backward.setFont(font)
        self.pushButton_backward.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/step-backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_backward.setIcon(icon)
        self.pushButton_backward.setObjectName("pushButton_backward")
        self.horizontalLayout_10.addWidget(self.pushButton_backward)
        self.pushButton_play = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_play.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_play.setFont(font)
        self.pushButton_play.setStyleSheet("")
        self.pushButton_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("icon/pause.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_play.setIcon(icon1)
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout_10.addWidget(self.pushButton_play)
        self.pushButton_forward = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_forward.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_forward.setFont(font)
        self.pushButton_forward.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/step-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_forward.setIcon(icon2)
        self.pushButton_forward.setObjectName("pushButton_forward")
        self.horizontalLayout_10.addWidget(self.pushButton_forward)
        self.verticalLayout_2.addWidget(self.frame_12)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_11 = QtWidgets.QFrame(self.frame)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 115))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.frame_18 = QtWidgets.QFrame(self.frame_11)
        self.frame_18.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_11.setContentsMargins(3, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_13 = QtWidgets.QFrame(self.frame_18)
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_informasi_2 = QtWidgets.QLabel(self.frame_13)
        self.label_informasi_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_informasi_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_2.setObjectName("label_informasi_2")
        self.horizontalLayout_4.addWidget(self.label_informasi_2)
        self.label_10 = QtWidgets.QLabel(self.frame_13)
        self.label_10.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.name_file = QtWidgets.QLabel(self.frame_13)
        self.name_file.setText("")
        self.name_file.setObjectName("name_file")
        self.horizontalLayout_4.addWidget(self.name_file)
        self.verticalLayout_11.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_18)
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_informasi_6 = QtWidgets.QLabel(self.frame_14)
        self.label_informasi_6.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_informasi_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_6.setObjectName("label_informasi_6")
        self.horizontalLayout_7.addWidget(self.label_informasi_6)
        self.label_17 = QtWidgets.QLabel(self.frame_14)
        self.label_17.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.label_resolusi = QtWidgets.QLabel(self.frame_14)
        self.label_resolusi.setText("")
        self.label_resolusi.setObjectName("label_resolusi")
        self.horizontalLayout_7.addWidget(self.label_resolusi)
        self.verticalLayout_11.addWidget(self.frame_14)
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_informasi_10 = QtWidgets.QLabel(self.frame_19)
        self.label_informasi_10.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_informasi_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_10.setObjectName("label_informasi_10")
        self.horizontalLayout_12.addWidget(self.label_informasi_10)
        self.label_23 = QtWidgets.QLabel(self.frame_19)
        self.label_23.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_12.addWidget(self.label_23)
        self.label_drone_alti = QtWidgets.QLabel(self.frame_19)
        self.label_drone_alti.setText("")
        self.label_drone_alti.setObjectName("label_drone_alti")
        self.horizontalLayout_12.addWidget(self.label_drone_alti)
        self.verticalLayout_11.addWidget(self.frame_19)
        self.frame_16 = QtWidgets.QFrame(self.frame_18)
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_informasi_7 = QtWidgets.QLabel(self.frame_16)
        self.label_informasi_7.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_informasi_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_7.setObjectName("label_informasi_7")
        self.horizontalLayout_8.addWidget(self.label_informasi_7)
        self.label_19 = QtWidgets.QLabel(self.frame_16)
        self.label_19.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.label_time_pro = QtWidgets.QLabel(self.frame_16)
        self.label_time_pro.setText("")
        self.label_time_pro.setObjectName("label_time_pro")
        self.horizontalLayout_8.addWidget(self.label_time_pro)
        self.verticalLayout_11.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_18)
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_informasi_8 = QtWidgets.QLabel(self.frame_17)
        self.label_informasi_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_informasi_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_8.setObjectName("label_informasi_8")
        self.horizontalLayout_9.addWidget(self.label_informasi_8)
        self.label_21 = QtWidgets.QLabel(self.frame_17)
        self.label_21.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_9.addWidget(self.label_21)
        self.label_status = QtWidgets.QLabel(self.frame_17)
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_9.addWidget(self.label_status)
        self.verticalLayout_11.addWidget(self.frame_17)
        self.verticalLayout_9.addWidget(self.frame_18)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_grap = QtWidgets.QLabel(self.frame_4)
        self.label_grap.setText("")
        self.label_grap.setObjectName("label_grap")
        self.verticalLayout_3.addWidget(self.label_grap)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_dp = QtWidgets.QLabel(self.frame_5)
        self.label_dp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_dp.setText("")
        self.label_dp.setObjectName("label_dp")
        self.verticalLayout_5.addWidget(self.label_dp)
        self.label_indi_dp = QtWidgets.QLabel(self.frame_5)
        self.label_indi_dp.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_indi_dp.setFrameShape(QtWidgets.QFrame.Box)
        self.label_indi_dp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_indi_dp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_indi_dp.setObjectName("label_indi_dp")
        self.verticalLayout_5.addWidget(self.label_indi_dp)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_ori = QtWidgets.QLabel(self.frame_6)
        self.label_ori.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_ori.setText("")
        self.label_ori.setObjectName("label_ori")
        self.verticalLayout_4.addWidget(self.label_ori)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout_3.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Menu"))
        self.radioButton_record.setText(_translate("Form", "Record"))
        self.radioButton_norecord.setText(_translate("Form", "No Record"))
        self.pushButton_2.setText(_translate("Form", "Load Video"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.pushButton_3.setText(_translate("Form", "Clear"))
        self.label_3.setText(_translate("Form", "Information"))
        self.label_informasi_2.setText(_translate("Form", "Name File "))
        self.label_10.setText(_translate("Form", ":"))
        self.label_informasi_6.setText(_translate("Form", "Resolusi"))
        self.label_17.setText(_translate("Form", ":"))
        self.label_informasi_10.setText(_translate("Form", "Drone Altitude"))
        self.label_23.setText(_translate("Form", ":"))
        self.label_informasi_7.setText(_translate("Form", "Time Processing"))
        self.label_19.setText(_translate("Form", ":"))
        self.label_informasi_8.setText(_translate("Form", "Status"))
        self.label_21.setText(_translate("Form", ":"))
        self.label_4.setText(_translate("Form", "Graph"))
        self.label_7.setText(_translate("Form", "Depth Estimation"))
        self.label_indi_dp.setText(_translate("Form", "Indikator"))
        self.label_5.setText(_translate("Form", "Original"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
