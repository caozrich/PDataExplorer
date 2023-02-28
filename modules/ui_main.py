# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 601))
        MainWindow.setStyleSheet(u"\n"
"QScrollBar:vertical {\n"
"\n"
"background: rgb(52, 59, 72);\n"
"\n"
" }\n"
" QScrollBar:horizontal {\n"
"\n"
" background: rgb(52, 59, 72); \n"
"\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
" {\n"
"   \n"
"	background-color: rgb(244, 242, 249);\n"
" min-width: 5px;\n"
"border-radius: 4px;\n"
" }\n"
"\n"
"QScrollBar::handle:horizontal\n"
" {\n"
"   \n"
"	background-color: rgb(244, 242, 249);\n"
" min-width: 5px;\n"
"border-radius: 4px;\n"
" }\n"
"\n"
"\n"
"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Mont"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"\n"
"\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Mont\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(243, 171, 65);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-"
                        "color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(243,171,65);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left"
                        ": 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(243,171,65);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(243,171,65);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTo"
                        "pBg{	\n"
"	background-color: rgb(243,171,65)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	pad"
                        "ding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(243,171,65);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(243,171,65); }\n"
""
                        "\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(243,171,65);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"\n"
"/* ////////////////////////////////////////////////////"
                        "/////////////////////////////////////////////\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(50,140,255);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(255, 255, 255);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(50,140,255);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: rgb(74, 74, 74);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(74, 74, 74);\n"
"\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: to"
                        "p;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rg"
                        "b(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
""
                        "	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(243, 171, 65);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(50,140,255);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(243, 171, 65);\n"
"}\n"
"\n"
"QSlider::groove:vert"
                        "ical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(50,140,255);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(50,140,255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(243, 171, 65);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
""
                        "	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(self.styleSheet)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, -1, 9)
        self.contentTopBg = QFrame(self.styleSheet)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(1262, 40))
        self.contentTopBg.setMaximumSize(QSize(16777215, 40))
        self.contentTopBg.setStyleSheet(u"background-color: rgb(253, 254, 254);\n"
"border-top-left-radius: 19px;\n"
"\n"
"border-top-right-radius: 19px;\n"
"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 7, -1, -1)
        self.topLogo = QFrame(self.contentTopBg)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(30, 30))
        self.topLogo.setMaximumSize(QSize(30, 30))
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setStyleSheet(u"background-image: url(:/img/images/images/ico.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.topLogo)

        self.titleRightInfo = QLabel(self.contentTopBg)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.titleRightInfo.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.titleRightInfo.setWordWrap(False)

        self.horizontalLayout.addWidget(self.titleRightInfo)

        self.pushButton_1 = QPushButton(self.contentTopBg)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setEnabled(True)
        self.pushButton_1.setMinimumSize(QSize(18, 18))
        self.pushButton_1.setMaximumSize(QSize(18, 18))
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(u"QPushButton{\n"
"border-radius: 9px;\n"
"background:#328CFF;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 9px;\n"
"background:#3b4bc3;\n"
"color:white;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius: 9px;\n"
"background:#328CFF;\n"
"color:white;\n"
"font: bold 14px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#bfbfbf;\n"
"background:#808080;\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_1)

        self.pushButton_4 = QPushButton(self.contentTopBg)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setMinimumSize(QSize(18, 18))
        self.pushButton_4.setMaximumSize(QSize(18, 18))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"border-radius: 9px;\n"
"background:#01c975;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:9px;\n"
"background:#13ae69;\n"
"color:white;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius: 9px;\n"
"background:#01c975;\n"
"color:white;\n"
"font: bold 14px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#bfbfbf;\n"
"background:#808080;\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.contentTopBg)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMinimumSize(QSize(18, 18))
        self.pushButton_3.setMaximumSize(QSize(18, 18))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"border-radius: 9px;\n"
"background:#FFA532;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 9px;\n"
"background:#d3701b;\n"
"color:white;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:9px;\n"
"background:#FFA532;\n"
"color:white;\n"
"font: 75 9pt \"Gilroy\";\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"color:#bfbfbf;\n"
"background:#808080;\n"
"\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4.raise_()
        self.pushButton_3.raise_()
        self.pushButton_1.raise_()
        self.titleRightInfo.raise_()
        self.topLogo.raise_()

        self.gridLayout_2.addWidget(self.contentTopBg, 0, 0, 1, 1)

        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"\n"
"background-color: rgb(60, 60, 65);")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.bgApp)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(240, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.leftMenuBg)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"border-bottom-left-radius: 10px;\n"
"\n"
"\n"
"background-color: rgb(60, 60, 65);")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.leftMenuFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.gridLayout.addWidget(self.toggleBox, 4, 0, 1, 3)

        self.frame_2 = QFrame(self.leftMenuFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_2, 5, 0, 1, 3)

        self.bottomBar = QFrame(self.leftMenuFrame)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font1 = QFont()
        font1.setFamilies([u"Mont"])
        font1.setBold(False)
        font1.setItalic(False)
        self.creditsLabel.setFont(font1)
        self.creditsLabel.setStyleSheet(u"")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)


        self.gridLayout.addWidget(self.bottomBar, 6, 0, 1, 3)

        self.labelVersion_4 = QLabel(self.leftMenuFrame)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setEnabled(True)
        self.labelVersion_4.setFont(font1)
        self.labelVersion_4.setLayoutDirection(Qt.LeftToRight)
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"font:12px ;\n"
"\n"
"")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.labelVersion_4, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.leftMenuFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(240, 27))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(234, 236, 237);\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"color: gray;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 3)

        self.lineEdit_2 = QLineEdit(self.leftMenuFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(43, 43, 43);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(243, 171, 65);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 0, 1, 3)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.topMenu)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 77, 9, -1)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-view-module.png);")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy1.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy1)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.btn_widgets)

        self.btn_compare = QPushButton(self.topMenu)
        self.btn_compare.setObjectName(u"btn_compare")
        sizePolicy1.setHeightForWidth(self.btn_compare.sizePolicy().hasHeightForWidth())
        self.btn_compare.setSizePolicy(sizePolicy1)
        self.btn_compare.setMinimumSize(QSize(0, 45))
        self.btn_compare.setFont(font)
        self.btn_compare.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_compare.setLayoutDirection(Qt.LeftToRight)
        self.btn_compare.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.btn_compare)

        self.btn_correlation = QPushButton(self.topMenu)
        self.btn_correlation.setObjectName(u"btn_correlation")
        sizePolicy1.setHeightForWidth(self.btn_correlation.sizePolicy().hasHeightForWidth())
        self.btn_correlation.setSizePolicy(sizePolicy1)
        self.btn_correlation.setMinimumSize(QSize(0, 45))
        self.btn_correlation.setFont(font)
        self.btn_correlation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_correlation.setLayoutDirection(Qt.LeftToRight)
        self.btn_correlation.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-loop-circular.png);")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.btn_correlation)

        self.btn_clear = QPushButton(self.topMenu)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy1.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy1)
        self.btn_clear.setMinimumSize(QSize(0, 45))
        self.btn_clear.setFont(font)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear.setLayoutDirection(Qt.LeftToRight)
        self.btn_clear.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-task.png);")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.btn_clear)


        self.gridLayout.addWidget(self.topMenu, 3, 0, 1, 3)

        self.toggleBox.raise_()
        self.topMenu.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_2.raise_()
        self.frame_2.raise_()
        self.bottomBar.raise_()
        self.labelVersion_4.raise_()

        self.gridLayout_4.addWidget(self.leftMenuFrame, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.leftMenuBg, 0, 0, 1, 1)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"background-color: rgb(234, 236, 237);\n"
"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.pagesContainer)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"\n"
"background-color: rgb(234, 236, 237);")
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.widgets)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.widgets)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.feature_distribution = QWidget()
        self.feature_distribution.setObjectName(u"feature_distribution")
        self.gridLayout_8 = QGridLayout(self.feature_distribution)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_6 = QFrame(self.feature_distribution)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(1002, 43))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_6)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(181, 20))
        self.label_2.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_18.addWidget(self.label_2, 0, 0, 2, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(201, 20))
        self.label_3.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_18.addWidget(self.label_3, 0, 1, 2, 2)

        self.horizontalSpacer_3 = QSpacerItem(818, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.feature_distribution)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(1002, 43))
        self.frame_5.setStyleSheet(u"background-color: rgb(212, 214, 215);\n"
"border-top-right-radius: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(13)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.frame_5)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(51, 51, 49);\n"
"	border: none;\n"
"\n"
"border-top-right-radius: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_6.addWidget(self.comboBox, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_5)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(51, 51, 49);\n"
"	border: none;\n"
"\n"
"border-top-right-radius: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")
        self.comboBox_2.setIconSize(QSize(16, 16))
        self.comboBox_2.setFrame(True)

        self.gridLayout_6.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(362, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.plot_1 = QPushButton(self.frame_5)
        self.plot_1.setObjectName(u"plot_1")
        self.plot_1.setEnabled(True)
        self.plot_1.setMinimumSize(QSize(191, 31))
        self.plot_1.setFont(font1)
        self.plot_1.setStyleSheet(u"QPushButton{\n"
"\n"
"background:#328CFF;\n"
"color:white;\n"
"border: none;\n"
"font: 16px ;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(40, 115, 206);\n"
"color:white;\n"
"border: none;\n"
"font: 15px ;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"background:#328CFF;\n"
"color:white;\n"
"font: bold 13px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#bfbfbf;\n"
"background:#808080;\n"
"\n"
"}")

        self.gridLayout_6.addWidget(self.plot_1, 0, 3, 1, 1)


        self.gridLayout_8.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.feature_distribution)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(961, 541))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_4)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 991, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_8.addWidget(self.frame_4, 2, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.feature_distribution)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_3.addWidget(self.page_2)

        self.gridLayout_9.addWidget(self.stackedWidget_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.widgets)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"b")
        self.gridLayout_17 = QGridLayout(self.home)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(6, 11, -1, 7)
        self.frame_3 = QFrame(self.home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(981, 81))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(400, 50, 211, 31))
        self.pushButton_8.setMinimumSize(QSize(211, 31))
        self.pushButton_8.setStyleSheet(u"\n"
"QPushButton{\n"
"\n"
"color: gray;\n"
"background-color: rgb(242, 246, 254);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: gray;\n"
"	background-color: rgb(216, 221, 229);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"font: bold ;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: gray;\n"
"background-color: rgb(242, 246, 254);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#bfbfbf;\n"
"background:#808080;\n"
"\n"
"}")
        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(200, 50, 211, 31))
        self.pushButton_7.setMinimumSize(QSize(211, 31))
        self.pushButton_7.setStyleSheet(u"\n"
"QPushButton{\n"
"\n"
"color: gray;\n"
"background-color: rgb(242, 246, 254);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: gray;\n"
"	background-color: rgb(216, 221, 229);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"font: bold ;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: gray;\n"
"background-color: rgb(242, 246, 254);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#bfbfbf;\n"
"background:#808080;\n"
"\n"
"}")
        self.data = QLabel(self.frame_3)
        self.data.setObjectName(u"data")
        self.data.setGeometry(QRect(7, 6, 741, 41))
        font2 = QFont()
        font2.setFamilies([u"Mont"])
        font2.setBold(True)
        font2.setItalic(False)
        self.data.setFont(font2)
        self.data.setStyleSheet(u"font: bold 21px ;\n"
"color: gray;\n"
"")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 50, 211, 31))
        self.pushButton.setMinimumSize(QSize(211, 31))
        self.pushButton.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"\n"
"color: gray;\n"
"background-color: rgb(242, 246, 254);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: gray;\n"
"	background-color: rgb(216, 221, 229);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"font: bold ;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: gray;\n"
"background-color: rgb(242, 246, 254);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#bfbfbf;\n"
"background:#808080;\n"
"\n"
"}")
        self.pushButton_9 = QPushButton(self.frame_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(600, 50, 211, 31))
        self.pushButton_9.setMinimumSize(QSize(211, 31))
        self.pushButton_9.setStyleSheet(u"\n"
"QPushButton{\n"
"\n"
"color: gray;\n"
"background-color: rgb(242, 246, 254);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: gray;\n"
"	background-color: rgb(216, 221, 229);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"font: bold ;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: gray;\n"
"background-color: rgb(242, 246, 254);\n"
"\n"
"border-top-left-radius: 15px;\n"
"\n"
"border: 1px solid rgb(223, 228, 237);\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#bfbfbf;\n"
"background:#808080;\n"
"\n"
"}")
        self.data.raise_()
        self.pushButton.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()

        self.gridLayout_17.addWidget(self.frame_3, 0, 0, 1, 1)

        self.stackedWidget_2 = QStackedWidget(self.home)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setFont(font)
        self.describe = QWidget()
        self.describe.setObjectName(u"describe")
        self.gridLayout_11 = QGridLayout(self.describe)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.row_5 = QFrame(self.describe)
        self.row_5.setObjectName(u"row_5")
        self.row_5.setMinimumSize(QSize(0, 150))
        self.row_5.setFrameShape(QFrame.StyledPanel)
        self.row_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.row_5)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_5 = QTableWidget(self.row_5)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setEnabled(True)
        self.tableWidget_5.setMinimumSize(QSize(981, 541))
        self.tableWidget_5.setStyleSheet(u"QTableWidget::item {\n"
"    color: gray;\n"
"}\n"
"QTableWidget {	\n"
"background-color: rgb(252, 252, 252);\n"
"	padding: 10px;\n"
"	border-radius: 8px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"background-color: rgb(82,156,250);\n"
"font: bold ;\n"
"color: white;\n"
"}\n"
"QHeaderView::section{\n"
"color: gray;\n"
"font: bold ;\n"
"background-color: rgb(242, 246, 254);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"rgb(242, 246, 254)\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"color: gray;\n"
"font: bold ;\n"
"background-color: rgb(242, 246, 254);\n"
"	padding: 3px;\n"
"	border-top"
                        "-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.tableWidget_5.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_12.addWidget(self.tableWidget_5, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.row_5, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.describe)
        self.unique = QWidget()
        self.unique.setObjectName(u"unique")
        self.frame = QFrame(self.unique)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 0, 999, 559))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_6 = QTableWidget(self.frame)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setEnabled(True)
        self.tableWidget_6.setMinimumSize(QSize(981, 541))
        self.tableWidget_6.setStyleSheet(u"QTableWidget::item {\n"
"    color: gray;\n"
"}\n"
"QTableWidget {	\n"
"background-color: rgb(252, 252, 252);\n"
"	padding: 10px;\n"
"	border-radius: 8px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"background-color: rgb(82,156,250);\n"
"font: bold ;\n"
"color: white;\n"
"}\n"
"QHeaderView::section{\n"
"color: gray;\n"
"font: bold ;\n"
"background-color: rgb(242, 246, 254);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"rgb(242, 246, 254)\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"color: gray;\n"
"font: bold ;\n"
"background-color: rgb(242, 246, 254);\n"
"	padding: 3px;\n"
"	border-top"
                        "-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.tableWidget_6.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_6.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_13.addWidget(self.tableWidget_6, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.unique)
        self.preview = QWidget()
        self.preview.setObjectName(u"preview")
        self.row_3 = QFrame(self.preview)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setGeometry(QRect(-10, 0, 1011, 559))
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.row_3)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setMinimumSize(QSize(981, 541))
        self.tableWidget.setStyleSheet(u"QTableWidget::item {\n"
"    color: gray;\n"
"}\n"
"QTableWidget {	\n"
"background-color: rgb(252, 252, 252);\n"
"	padding: 10px;\n"
"	border-radius: 8px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"background-color: rgb(82,156,250);\n"
"font: bold ;\n"
"color: white;\n"
"}\n"
"QHeaderView::section{\n"
"color: gray;\n"
"font: bold ;\n"
"background-color: rgb(242, 246, 254);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"rgb(242, 246, 254)\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"color: gray;\n"
"font: bold ;\n"
"background-color: rgb(242, 246, 254);\n"
"	padding: 3px;\n"
"	border-top"
                        "-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_14.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.preview)
        self.info = QWidget()
        self.info.setObjectName(u"info")
        self.gridLayout_16 = QGridLayout(self.info)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.row_4 = QFrame(self.info)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setMinimumSize(QSize(0, 150))
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.row_4)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_4 = QTableWidget(self.row_4)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setEnabled(True)
        self.tableWidget_4.setMinimumSize(QSize(981, 541))
        self.tableWidget_4.setStyleSheet(u"QTableWidget::item {\n"
"    color: gray;\n"
"}\n"
"QTableWidget {	\n"
"background-color: rgb(252, 252, 252);\n"
"	padding: 10px;\n"
"	border-radius: 8px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"background-color: rgb(82,156,250);\n"
"font: bold ;\n"
"color: white;\n"
"}\n"
"QHeaderView::section{\n"
"color: gray;\n"
"font: bold ;\n"
"background-color: rgb(242, 246, 254);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"rgb(242, 246, 254)\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"color: gray;\n"
"font: bold ;\n"
"background-color: rgb(242, 246, 254);\n"
"	padding: 3px;\n"
"	border-top"
                        "-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.tableWidget_4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_15.addWidget(self.tableWidget_4, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.row_4, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.info)

        self.gridLayout_17.addWidget(self.stackedWidget_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.target = QWidget()
        self.target.setObjectName(u"target")
        self.gridLayout_21 = QGridLayout(self.target)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.target)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(1020, 70))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(5)
        self.gridLayout_19.setVerticalSpacing(0)
        self.gridLayout_19.setContentsMargins(0, 30, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(961, 6))
        self.frame_11.setMaximumSize(QSize(1020, 6))
        self.frame_11.setStyleSheet(u"background-color: rgb(51, 51, 49);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayout_19.addWidget(self.frame_11, 0, 0, 1, 4)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(191, 20))
        self.label_6.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_19.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(191, 20))
        self.label_4.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_19.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(191, 21))
        self.label_5.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_19.addWidget(self.label_5, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(429, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)


        self.gridLayout_21.addWidget(self.frame_10, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.target)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setStyleSheet(u"background-color: rgb(212, 214, 215);\n"
"border-top-right-radius: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(3)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 1, 0)
        self.comboBox_5 = QComboBox(self.frame_8)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMaximumSize(QSize(191, 30))
        self.comboBox_5.setFont(font)
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setStyleSheet(u"background-color: rgb(51, 51, 49);\n"
"	border: none;\n"
"\n"
"border-top-right-radius: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")
        self.comboBox_5.setIconSize(QSize(16, 16))
        self.comboBox_5.setDuplicatesEnabled(False)
        self.comboBox_5.setFrame(True)

        self.gridLayout_7.addWidget(self.comboBox_5, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_8)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(191, 30))
        self.comboBox_3.setFont(font)
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet(u"background-color: rgb(51, 51, 49);\n"
"	border: none;\n"
"\n"
"border-top-right-radius: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")
        self.comboBox_3.setIconSize(QSize(16, 16))
        self.comboBox_3.setFrame(True)

        self.gridLayout_7.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.frame_8)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMaximumSize(QSize(191, 30))
        self.comboBox_4.setFont(font)
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet(u"background-color: rgb(51, 51, 49);\n"
"	border: none;\n"
"\n"
"border-top-right-radius: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")
        self.comboBox_4.setIconSize(QSize(16, 16))
        self.comboBox_4.setFrame(True)

        self.gridLayout_7.addWidget(self.comboBox_4, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.plot_2 = QPushButton(self.frame_8)
        self.plot_2.setObjectName(u"plot_2")
        self.plot_2.setEnabled(True)
        self.plot_2.setMinimumSize(QSize(191, 31))
        self.plot_2.setMaximumSize(QSize(199, 31))
        self.plot_2.setFont(font1)
        self.plot_2.setStyleSheet(u"QPushButton{\n"
"\n"
"background:#328CFF;\n"
"color:white;\n"
"border: none;\n"
"font: 16px ;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(40, 115, 206);\n"
"color:white;\n"
"border: none;\n"
"font: 15px ;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"background:#328CFF;\n"
"color:white;\n"
"font: bold 13px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color:#bfbfbf;\n"
"background:#808080;\n"
"\n"
"}")

        self.gridLayout_7.addWidget(self.plot_2, 0, 4, 1, 1)


        self.gridLayout_21.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.target)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(961, 521))
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_9)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout_20.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frame_9, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.target)
        self.correlations = QWidget()
        self.correlations.setObjectName(u"correlations")
        self.gridLayout_23 = QGridLayout(self.correlations)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(9, 9, -1, -1)
        self.frame_12 = QFrame(self.correlations)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(951, 601))
        self.frame_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_12)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.gridLayout_22.addLayout(self.verticalLayout_8, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_12, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.correlations)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_24 = QGridLayout(self.page)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(991, 611))
        self.label_7.setStyleSheet(u"color: gray;\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.clean = QWidget()
        self.clean.setObjectName(u"clean")
        self.frame_13 = QFrame(self.clean)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(20, 19, 389, 369))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_13)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(371, 351))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame_14)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 40, 251, 111))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"color: gray;\n"
"")
        self.groupBox.setCheckable(False)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 40, 261, 21))
        self.radioButton.setStyleSheet(u"")
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 70, 221, 21))
        self.radioButton_2.setStyleSheet(u"")
        self.radioButton_2.setChecked(True)
        self.groupBox_2 = QGroupBox(self.frame_14)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 170, 221, 121))
        self.groupBox_2.setStyleSheet(u"color: gray;")
        self.groupBox_2.setCheckable(False)
        self.radioButton_7 = QRadioButton(self.groupBox_2)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(10, 40, 251, 21))
        self.radioButton_7.setStyleSheet(u"")
        self.radioButton_8 = QRadioButton(self.groupBox_2)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(10, 70, 211, 21))
        self.radioButton_8.setStyleSheet(u"")
        self.radioButton_8.setChecked(True)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(30, 290, 261, 1))
        self.frame_15.setStyleSheet(u"background-color: rgb(60, 60, 65);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.csave = QPushButton(self.frame_14)
        self.csave.setObjectName(u"csave")
        self.csave.setGeometry(QRect(30, 300, 141, 31))
        self.csave.setMinimumSize(QSize(100, 27))
        self.csave.setFont(font)
        self.csave.setCursor(QCursor(Qt.PointingHandCursor))
        self.csave.setStyleSheet(u"background-color: rgb(60, 60, 65);\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"color: white;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.csave.setIcon(icon1)

        self.gridLayout_25.addWidget(self.frame_14, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.clean)

        self.gridLayout_10.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.gridLayout_3.addWidget(self.contentBox, 0, 1, 1, 1)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon2)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.gridLayout_3.addWidget(self.extraLeftBox, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.bgApp, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PDataExplorer", None))
        self.pushButton_1.setText("")
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Richard Libreros", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"press \u201cOpen\u201d to load  a new dataset", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Data Summary", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Feature distribution", None))
        self.btn_compare.setText(QCoreApplication.translate("MainWindow", u"Features vs target", None))
        self.btn_correlation.setText(QCoreApplication.translate("MainWindow", u"Correlations", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear Dataset", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Feature type:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Feature name:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"No values loaded yet", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"No values loaded yet", None))

        self.plot_1.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u".describe", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u".info", None))
        self.data.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u".nunique", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"   \u2022Target:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u2022Variable X:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u2022Variable Y:", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"No values loaded yet", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"No values loaded yet", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"No values loaded yet", None))

        self.plot_2.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Load a new Dataset to start.", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u2022NaN values:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"delete rows with nan values", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"replace nan values with 0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u2022inf values", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"delete rows with nan values", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"replace nan values with 0", None))
        self.csave.setText(QCoreApplication.translate("MainWindow", u"Clean&&Save", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Mont'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#f3ab41;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#f3ab41;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#f3ab41;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
    # retranslateUi

