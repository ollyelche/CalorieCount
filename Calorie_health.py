# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledLjBHni.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 732)
        MainWindow.setStyleSheet(u"*{\n"
"border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color:rgb(170, 170, 255)\n"
"")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setStyleSheet(u"background-color:rgb(170, 170, 255);\n"
"\n"
"padding: 0;\n"
"\n"
"margin: 0;")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.header_center_frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.open_close_side_bar_btn.setFont(font)
        self.open_close_side_bar_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_close_side_bar_btn.setStyleSheet(u"margin: 0;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons8-menu-squared-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_center_frame, 0, Qt.AlignLeft)

        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setStyleSheet(u"background-color:rgb(170, 170, 255)\n"
"")
        self.header_left_frame.setFrameShape(QFrame.NoFrame)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.header_left_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(2)
        self.label_2.setFont(font1)
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icons8-kawaii-broccoli-64.png"))

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)

        self.label = QLabel(self.header_left_frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.header_left_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons8-minimize-window-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons8-maximize-window-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons8-close-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_menu_cont_frame.sizePolicy().hasHeightForWidth())
        self.left_menu_cont_frame.setSizePolicy(sizePolicy1)
        self.left_menu_cont_frame.setMinimumSize(QSize(35, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(35, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"background-color:rgb(170, 170, 255)\n"
"")
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(130, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.profile_btn = QPushButton(self.menu_frame)
        self.profile_btn.setObjectName(u"profile_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.profile_btn.sizePolicy().hasHeightForWidth())
        self.profile_btn.setSizePolicy(sizePolicy2)
        self.profile_btn.setFont(font2)
        self.profile_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons8-head-profile-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_btn.setIcon(icon4)
        self.profile_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.profile_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.activity_btn = QPushButton(self.menu_frame)
        self.activity_btn.setObjectName(u"activity_btn")
        self.activity_btn.setFont(font2)
        self.activity_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons8-exercise-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_btn.setIcon(icon5)
        self.activity_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.activity_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.dashboard_btn = QPushButton(self.menu_frame)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setMaximumSize(QSize(600, 600))
        self.dashboard_btn.setFont(font2)
        self.dashboard_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons8-statistics-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon6)
        self.dashboard_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.dashboard_btn, 0, 0, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_cont_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        self.main_body_contents.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.verticalLayout_4 = QVBoxLayout(self.dashboard)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.summary_frame = QFrame(self.dashboard)
        self.summary_frame.setObjectName(u"summary_frame")
        self.summary_frame.setFrameShape(QFrame.StyledPanel)
        self.summary_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.summary_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.progressBar = QProgressBar(self.summary_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(250, 16777215))
        self.progressBar.setValue(50)
        self.progressBar.setTextVisible(True)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.total_calories_label = QLabel(self.summary_frame)
        self.total_calories_label.setObjectName(u"total_calories_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.total_calories_label.sizePolicy().hasHeightForWidth())
        self.total_calories_label.setSizePolicy(sizePolicy3)
        self.total_calories_label.setMaximumSize(QSize(100, 13))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.total_calories_label.setFont(font3)
        self.total_calories_label.setStyleSheet(u"background-color:rgb(170, 170, 255)")

        self.verticalLayout_3.addWidget(self.total_calories_label)

        self.total_calories_number = QLCDNumber(self.summary_frame)
        self.total_calories_number.setObjectName(u"total_calories_number")
        self.total_calories_number.setMaximumSize(QSize(100, 50))

        self.verticalLayout_3.addWidget(self.total_calories_number, 0, Qt.AlignLeft)

        self.breakfast_label = QLabel(self.summary_frame)
        self.breakfast_label.setObjectName(u"breakfast_label")
        self.breakfast_label.setMaximumSize(QSize(100, 13))
        self.breakfast_label.setFont(font3)
        self.breakfast_label.setStyleSheet(u"background-color:rgb(170, 170, 255)")

        self.verticalLayout_3.addWidget(self.breakfast_label)

        self.breakfast_number = QLCDNumber(self.summary_frame)
        self.breakfast_number.setObjectName(u"breakfast_number")

        self.verticalLayout_3.addWidget(self.breakfast_number, 0, Qt.AlignLeft)

        self.lunch_label = QLabel(self.summary_frame)
        self.lunch_label.setObjectName(u"lunch_label")
        self.lunch_label.setMaximumSize(QSize(100, 13))
        self.lunch_label.setFont(font3)
        self.lunch_label.setStyleSheet(u"background-color:rgb(170, 170, 255)")

        self.verticalLayout_3.addWidget(self.lunch_label)

        self.lunch_number = QLCDNumber(self.summary_frame)
        self.lunch_number.setObjectName(u"lunch_number")

        self.verticalLayout_3.addWidget(self.lunch_number, 0, Qt.AlignLeft)

        self.dinner_label = QLabel(self.summary_frame)
        self.dinner_label.setObjectName(u"dinner_label")
        self.dinner_label.setMaximumSize(QSize(100, 13))
        self.dinner_label.setFont(font3)
        self.dinner_label.setStyleSheet(u"background-color:rgb(170, 170, 255)")

        self.verticalLayout_3.addWidget(self.dinner_label)

        self.dinner_number = QLCDNumber(self.summary_frame)
        self.dinner_number.setObjectName(u"dinner_number")

        self.verticalLayout_3.addWidget(self.dinner_number, 0, Qt.AlignLeft)

        self.entry_text_box = QTextEdit(self.summary_frame)
        self.entry_text_box.setObjectName(u"entry_text_box")
        self.entry_text_box.setMaximumSize(QSize(5000, 50))
        self.entry_text_box.setOverwriteMode(True)

        self.verticalLayout_3.addWidget(self.entry_text_box)

        self.calories_text_box = QTextEdit(self.summary_frame)
        self.calories_text_box.setObjectName(u"calories_text_box")
        self.calories_text_box.setMaximumSize(QSize(5000, 25))

        self.verticalLayout_3.addWidget(self.calories_text_box)

        self.time_of_day_combo_picker = QComboBox(self.summary_frame)
        self.time_of_day_combo_picker.setObjectName(u"time_of_day_combo_picker")

        self.verticalLayout_3.addWidget(self.time_of_day_combo_picker)

        self.enter_button = QPushButton(self.summary_frame)
        self.enter_button.setObjectName(u"enter_button")
        self.enter_button.setMaximumSize(QSize(150, 16777215))
        self.enter_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.enter_button.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons8-kawaii-broccoli-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.enter_button.setIcon(icon7)
        self.enter_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.enter_button, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.summary_frame)

        self.stackedWidget.addWidget(self.dashboard)
        self.activity = QWidget()
        self.activity.setObjectName(u"activity")
        self.frame = QFrame(self.activity)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(190, 80, 431, 251))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 100, 47, 13))
        self.label_7.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.stackedWidget.addWidget(self.activity)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.stackedWidget.addWidget(self.profile)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_contents)

        self.right_frame = QFrame(self.main_body_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMaximumSize(QSize(80, 16777215))
        self.right_frame.setStyleSheet(u"background-color:rgb(170, 170, 255)\n"
"")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.right_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.footer_left_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Calorie Health", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.profile_btn.setText(QCoreApplication.translate("MainWindow", u"Profile ", None))
        self.activity_btn.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Stats   ", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p% of budget", None))
        self.total_calories_label.setText(QCoreApplication.translate("MainWindow", u"Total Calories", None))
        self.breakfast_label.setText(QCoreApplication.translate("MainWindow", u"Breakfast", None))
        self.lunch_label.setText(QCoreApplication.translate("MainWindow", u"Lunch", None))
        self.dinner_label.setText(QCoreApplication.translate("MainWindow", u"Dinner", None))
        self.entry_text_box.setMarkdown(QCoreApplication.translate("MainWindow", u"entry\n"
"\n"
"", None))
        self.calories_text_box.setMarkdown(QCoreApplication.translate("MainWindow", u"number of calories\n"
"\n"
"", None))
        self.enter_button.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"HELLO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 0.0 | Copyright Oliver Lopez", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

