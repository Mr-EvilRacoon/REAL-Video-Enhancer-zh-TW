# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testRVEInterface.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QScrollArea, QScrollBar, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1163, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1050, 700))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setSizeIncrement(QSize(1, 1))
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet(u"\n"
"\n"
"QMainWindow {\n"
"   color:black;\n"
"   background-color:black;\n"
"border:1px;\n"
"}\n"
"QLabel{\n"
"	color: #fff;\n"
"}\n"
"QLineEdit{\n"
"color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color:#1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color:#16191d;\n"
"   border-radius: 30px;\n"
"}\n"
"#bottomMenuSubContainer{\n"
"	background-color:#2c313c;\n"
"   border-radius: 30px;\n"
"}\n"
"\n"
"QProgressBar{\n"
"    background-color:#2c313c;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
" QProgressBar::chunk {\n"
"     background-color:white;\n"
"	text-align:left;\n"
"	border-radius: 10px;\n"
"	\n"
" }\n"
"QStackedWidget{\n"
"	background-color:#16191d;\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPlainTextEdit{\n"
"    background-color:#2c313c;\n"
"	border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton{\n"
"    background-color:#2c313c;\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:checked{\n"
""
                        "	background-color:#676e7b;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#343b47;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    border : 1px solid white;\n"
"    border-radius: 2px;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    left: 2px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/check-square.svg);\n"
"    color: white;\n"
"    border-radius: 2px;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"	max-width: 8px;\n"
"	}\n"
"QScrollBar:horizontal{\n"
"	max-height: 8px;\n"
"	}\n"
"QScrollBar::handle{\n"
"		border-radius:4px;\n"
"        background: #fff;\n"
"}\n"
"\n"
"\n"
"        QScrollBar::handle:vertical:hover {\n"
"            background: gray;\n"
"        }\n"
"\n"
"        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"            border: none;\n"
"            background: transparent;\n"
"            width: 0px;\n"
"            height: 0px;\n"
"        }\n"
"\n"
"        QScrollBar::up-arrow:vertical, "
                        "QScrollBar::down-arrow:vertical {\n"
"            border: none;\n"
"            background: none;\n"
"        }\n"
"\n"
"        /* Horizontal scrollbar */\n"
"        \n"
"\n"
"        QScrollBar::handle:horizontal:hover {\n"
"            background: #0c66c2;\n"
"        }\n"
"\n"
"        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"            border: none;\n"
"            background: #f0f0f0;\n"
"            height: 0px;\n"
"            width: 0px;\n"
"        }\n"
"\n"
"        QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"            border: none;\n"
"            background: none;\n"
"        }\n"
"\n"
"QScrollBar:vertical{\n"
"		background:transparent; /*change background here*/\n"
"		color:#2c313c;\n"
"}\n"
"QScrollBar:horizontal{\n"
"		background:#2c313c; /*change background here*/\n"
"		color:transparent;\n"
"}\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"                border-top: 0px solid #C2C7CB;\n"
"                top: -0.5em;\n"
""
                        "                background: transparent;\n"
"            }\n"
"\n"
"            QTabWidget::tab-bar {\n"
"                alignment: left;\n"
"            }\n"
"\n"
"            QTabBar::tab {\n"
"                background: #1f232a;\n"
"                border: 0px solid #C4C4C3;\n"
"                border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"                border-top-left-radius: 4px;\n"
"                border-top-right-radius: 4px;\n"
"				  border-bottom-left-radius: 4px;\n"
"                border-bottom-right-radius: 4px;\n"
"                min-width: 8ex;\n"
"                padding: 6px;\n"
"				 color: #fff;\n"
"            }\n"
"\n"
"            QTabBar::tab:selected{\n"
"                background:#676e7b;\n"
"            }\n"
"            QTabBar::tab:hover {\n"
"				background: #343b47;\n"
"				}\n"
"\n"
"            QTabBar::tab:selected {\n"
"                border-color: transparent;\n"
"                border-bottom-color: transparent; /* same as pane color */\n"
"        "
                        "    }\n"
"\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }\n"
"\n"
"            QTabBar::tab:selected {\n"
"                /* expand/overlap to the left and right by 4px */\n"
"                margin-left: 2px;\n"
"                margin-right: 2px;\n"
"            }\n"
"\n"
"            QTabBar::tab:first:selected {\n"
"                margin-left: 0; /* the first selected tab should not overlap */\n"
"            }\n"
"\n"
"            QTabBar::tab:last:selected {\n"
"                margin-right: 0; /* the last selected tab should not overlap */\n"
"            }\n"
"\n"
"            QTabBar::tab:only-one {\n"
"                margin: 0; /* if there is only one tab, it should not overlap */\n"
"            }\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centralWidget = QWidget(self.centralwidget)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainWindowContainer = QWidget(self.centralWidget)
        self.mainWindowContainer.setObjectName(u"mainWindowContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainWindowContainer.sizePolicy().hasHeightForWidth())
        self.mainWindowContainer.setSizePolicy(sizePolicy1)
        self.mainWindowContainer.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.mainWindowContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainWindowContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"QWidget{\n"
"background-color:#16191d\n"
"\n"
"}\n"
"QPushButton{\n"
"    background-color:#2c313c;\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#676e7b;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#343b47;\n"
"}\n"
"QPushButton::toolTip{\n"
"background-color:#676e7b;\n"
"}\n"
"QTextEdit{\n"
"background-color:#2c313c;\n"
"border-radius: 10px;\n"
"padding:5px 10px;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.homePage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.widget_11 = QWidget(self.homePage)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_14 = QSpacerItem(466, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_14)

        self.label_13 = QLabel(self.widget_11)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_29.addWidget(self.label_13)

        self.kofiBtn = QPushButton(self.widget_11)
        self.kofiBtn.setObjectName(u"kofiBtn")
        self.kofiBtn.setMaximumSize(QSize(55, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons/coffee.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.kofiBtn.setIcon(icon)
        self.kofiBtn.setIconSize(QSize(35, 35))
        self.kofiBtn.setCheckable(False)

        self.horizontalLayout_29.addWidget(self.kofiBtn)

        self.label_16 = QLabel(self.widget_11)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_29.addWidget(self.label_16)

        self.githubBtn = QPushButton(self.widget_11)
        self.githubBtn.setObjectName(u"githubBtn")
        self.githubBtn.setMaximumSize(QSize(55, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/github.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.githubBtn.setIcon(icon1)
        self.githubBtn.setIconSize(QSize(35, 35))
        self.githubBtn.setCheckable(False)

        self.horizontalLayout_29.addWidget(self.githubBtn)


        self.horizontalLayout_28.addWidget(self.widget_11)


        self.gridLayout_2.addLayout(self.horizontalLayout_28, 4, 0, 1, 1)

        self.widget_8 = QWidget(self.homePage)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_7 = QGridLayout(self.widget_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_2 = QLabel(self.widget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/icons/logo-v2.svg"))
        self.label_2.setScaledContents(False)

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QLabel(self.widget_8)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Fira Mono"])
        font.setPointSize(25)
        self.label.setFont(font)

        self.gridLayout_7.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget_8, 1, 0, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.changeLogText = QTextEdit(self.homePage)
        self.changeLogText.setObjectName(u"changeLogText")
        self.changeLogText.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.changeLogText)

        self.systemInfoText = QTextEdit(self.homePage)
        self.systemInfoText.setObjectName(u"systemInfoText")
        font1 = QFont()
        font1.setPointSize(15)
        self.systemInfoText.setFont(font1)
        self.systemInfoText.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.systemInfoText)


        self.gridLayout_2.addLayout(self.horizontalLayout_30, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.homePage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.morePage.setStyleSheet(u"QWidget{\n"
"background-color:#16191d\n"
"\n"
"}")
        self.gridLayout_6 = QGridLayout(self.morePage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedWidget.addWidget(self.morePage)
        self.procPage = QWidget()
        self.procPage.setObjectName(u"procPage")
        self.procPage.setStyleSheet(u"QWidget{\n"
"background-color:#16191d\n"
"\n"
"}\n"
"QLineEdit{\n"
"background-color:#2c313c;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QTextEdit{\n"
"background-color:#2c313c;\n"
"border-radius: 10px;\n"
"padding:5px 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#2c313c;\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#676e7b;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#343b47;\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color:#2c313c;\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"color:white;\n"
"}\n"
"\n"
"QProgressBar{\n"
"    background-color:#2c313c;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
" QProgressBar::chunk {\n"
"     background-color:white;\n"
"	text-align:left;\n"
"	border-radius: 10px;\n"
"	\n"
" }\n"
"\n"
"QDoubleSpinBox{\n"
"	background-color:#2c313c;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"       \n"
"		image"
                        ": url(:/icons/icons/arrow-up.svg); \n"
"    }\n"
"QDoubleSpinBox::down-arrow {\n"
"\n"
"        image: url(:/icons/icons/arrow-down.svg); \n"
"		\n"
"    }\n"
"QDoubleSpinBox::up-button {\n"
"        width: 20px;\n"
"        height: 15px;\n"
"    }\n"
"QDoubleSpinBox::down-button {\n"
"        width: 20px;\n"
"        height: 15px;\n"
"    }\n"
"QSpinBox{\n"
"	background-color:#2c313c;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"       \n"
"		image: url(:/icons/icons/arrow-up.svg); \n"
"    }\n"
"QSpinBox::down-arrow {\n"
"\n"
"        image: url(:/icons/icons/arrow-down.svg); \n"
"		\n"
"    }\n"
"QSpinBox::up-button {\n"
"        width: 20px;\n"
"        height: 15px;\n"
"    }\n"
"QSpinBox::down-button {\n"
"        width: 20px;\n"
"        height: 15px;\n"
"    }\n"
"\n"
"\n"
"\n"
"QListWidget{\n"
"background-color:#16191d\n"
"\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.procPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.processInfoContainer = QWidget(self.procPage)
        self.processInfoContainer.setObjectName(u"processInfoContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.processInfoContainer.sizePolicy().hasHeightForWidth())
        self.processInfoContainer.setSizePolicy(sizePolicy3)
        self.processInfoContainer.setStyleSheet(u"#processInfoContainer{\n"
"background-color:#1f232a;\n"
"border-radius:10px;\n"
"}\n"
"#infoSubContainer{\n"
"background-color:#1f232a\n"
"\n"
"}\n"
"#previewSubContainer{\n"
"background-color:#1f232a\n"
"}\n"
"#renderOutput{\n"
"background-color:#343b47;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"#previewLabel{\n"
"background-color:#343b47;\n"
"border-radius: 10px;\n"
"\n"
"\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.processInfoContainer)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.previewSubContainer = QWidget(self.processInfoContainer)
        self.previewSubContainer.setObjectName(u"previewSubContainer")
        self.verticalLayout_8 = QVBoxLayout(self.previewSubContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.previewLabel = QLabel(self.previewSubContainer)
        self.previewLabel.setObjectName(u"previewLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.previewLabel.sizePolicy().hasHeightForWidth())
        self.previewLabel.setSizePolicy(sizePolicy4)
        self.previewLabel.setStyleSheet(u"\n"
"QLabel{\n"
"	color: #fff;\n"
"    background-color:#1f232a;\n"
"}\n"
"")
        self.previewLabel.setScaledContents(False)
        self.previewLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.previewLabel)

        self.VideoPreview = QWidget(self.previewSubContainer)
        self.VideoPreview.setObjectName(u"VideoPreview")
        self.VideoPreview.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.VideoPreview.sizePolicy().hasHeightForWidth())
        self.VideoPreview.setSizePolicy(sizePolicy1)
        self.horizontalLayout_26 = QHBoxLayout(self.VideoPreview)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.verticalLayout_8.addWidget(self.VideoPreview)


        self.verticalLayout_5.addWidget(self.previewSubContainer)

        self.RenderedPreviewControlsContainer = QWidget(self.processInfoContainer)
        self.RenderedPreviewControlsContainer.setObjectName(u"RenderedPreviewControlsContainer")
        self.RenderedPreviewControlsContainer.setEnabled(True)
        self.RenderedPreviewControlsContainer.setStyleSheet(u"QWidget{\n"
"border-radius: 10\n"
"}\n"
"\n"
"*:disabled{\n"
"	color:gray;\n"
"}")
        self.horizontalLayout_47 = QHBoxLayout(self.RenderedPreviewControlsContainer)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.widget_30 = QWidget(self.RenderedPreviewControlsContainer)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_37 = QVBoxLayout(self.widget_30)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_9 = QLabel(self.widget_30)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_37.addWidget(self.label_9)

        self.startTimeSpinBox = QDoubleSpinBox(self.widget_30)
        self.startTimeSpinBox.setObjectName(u"startTimeSpinBox")

        self.verticalLayout_37.addWidget(self.startTimeSpinBox)

        self.label_52 = QLabel(self.widget_30)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_37.addWidget(self.label_52)

        self.endTimeSpinBox = QDoubleSpinBox(self.widget_30)
        self.endTimeSpinBox.setObjectName(u"endTimeSpinBox")
        self.endTimeSpinBox.setMinimum(1.000000000000000)
        self.endTimeSpinBox.setValue(1.000000000000000)

        self.verticalLayout_37.addWidget(self.endTimeSpinBox)

        self.widget_14 = QWidget(self.widget_30)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.renderPreviewBtn = QPushButton(self.widget_14)
        self.renderPreviewBtn.setObjectName(u"renderPreviewBtn")
        font2 = QFont()
        font2.setBold(False)
        self.renderPreviewBtn.setFont(font2)
        self.renderPreviewBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_48.addWidget(self.renderPreviewBtn)

        self.label_63 = QLabel(self.widget_14)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(25, 25))
        self.label_63.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_63.setScaledContents(True)

        self.horizontalLayout_48.addWidget(self.label_63)


        self.verticalLayout_37.addWidget(self.widget_14)

        self.timeInVideoScrollBar = QScrollBar(self.widget_30)
        self.timeInVideoScrollBar.setObjectName(u"timeInVideoScrollBar")
        self.timeInVideoScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_37.addWidget(self.timeInVideoScrollBar)


        self.horizontalLayout_47.addWidget(self.widget_30)


        self.verticalLayout_5.addWidget(self.RenderedPreviewControlsContainer)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.ETA = QLabel(self.processInfoContainer)
        self.ETA.setObjectName(u"ETA")
        font3 = QFont()
        font3.setPointSize(10)
        self.ETA.setFont(font3)
        self.ETA.setStyleSheet(u"QLabel{\n"
"background-color: #1f232a\n"
"}")

        self.verticalLayout_34.addWidget(self.ETA)

        self.FPS = QLabel(self.processInfoContainer)
        self.FPS.setObjectName(u"FPS")
        self.FPS.setFont(font3)
        self.FPS.setStyleSheet(u"QLabel{\n"
"background-color: #1f232a\n"
"}")

        self.verticalLayout_34.addWidget(self.FPS)

        self.STATUS = QLabel(self.processInfoContainer)
        self.STATUS.setObjectName(u"STATUS")
        self.STATUS.setFont(font3)
        self.STATUS.setStyleSheet(u"QLabel{\n"
"background-color: #1f232a\n"
"}")

        self.verticalLayout_34.addWidget(self.STATUS)


        self.verticalLayout_5.addLayout(self.verticalLayout_34)


        self.gridLayout_3.addWidget(self.processInfoContainer, 0, 2, 1, 1)

        self.processContainer = QWidget(self.procPage)
        self.processContainer.setObjectName(u"processContainer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.processContainer.sizePolicy().hasHeightForWidth())
        self.processContainer.setSizePolicy(sizePolicy5)
        self.processContainer.setMaximumSize(QSize(500, 16777215))
        self.processContainer.setStyleSheet(u"*:disabled{\n"
" \n"
"	color:gray;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.processContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.bottomMenuSubContainer = QWidget(self.processContainer)
        self.bottomMenuSubContainer.setObjectName(u"bottomMenuSubContainer")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.bottomMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.bottomMenuSubContainer.setSizePolicy(sizePolicy6)
        self.bottomMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.bottomMenuSubContainer.setMaximumSize(QSize(500, 16777215))
        self.bottomMenuSubContainer.setStyleSheet(u"#bottomMenuSubContainer{\n"
"background-color:#1f232a\n"
"}\n"
"#progressBar{\n"
"background-color:#343b47\n"
"}\n"
"")
        self.verticalLayout_21 = QVBoxLayout(self.bottomMenuSubContainer)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.bottomMenuSubContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_24 = QVBoxLayout(self.widget_2)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.processSettingsContainer = QTabWidget(self.widget_2)
        self.processSettingsContainer.setObjectName(u"processSettingsContainer")
        sizePolicy3.setHeightForWidth(self.processSettingsContainer.sizePolicy().hasHeightForWidth())
        self.processSettingsContainer.setSizePolicy(sizePolicy3)
        self.processSettingsContainer.setMinimumSize(QSize(0, 0))
        self.processSettingsContainer.setMaximumSize(QSize(16777215, 16777215))
        self.generalSettings = QWidget()
        self.generalSettings.setObjectName(u"generalSettings")
        sizePolicy3.setHeightForWidth(self.generalSettings.sizePolicy().hasHeightForWidth())
        self.generalSettings.setSizePolicy(sizePolicy3)
        self.generalSettings.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.generalSettings)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.generalSettings)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy3.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy3)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.widget_5)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy2.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy2)
        self.scrollArea_4.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        self.scrollArea_4.setFont(font4)
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_4.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 470, 1040))
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_32.setSpacing(11)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(11, 11, 11, 11)
        self.inputFileContainer = QWidget(self.scrollAreaWidgetContents_4)
        self.inputFileContainer.setObjectName(u"inputFileContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.inputFileContainer)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.inputFileSelectButton = QPushButton(self.inputFileContainer)
        self.inputFileSelectButton.setObjectName(u"inputFileSelectButton")
        self.inputFileSelectButton.setMinimumSize(QSize(0, 30))
        self.inputFileSelectButton.setMaximumSize(QSize(16777215, 30))
        self.inputFileSelectButton.setFont(font4)
        self.inputFileSelectButton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.inputFileSelectButton)

        self.batchSelectButton = QPushButton(self.inputFileContainer)
        self.batchSelectButton.setObjectName(u"batchSelectButton")
        self.batchSelectButton.setMinimumSize(QSize(0, 30))
        self.batchSelectButton.setMaximumSize(QSize(16777215, 30))
        self.batchSelectButton.setFont(font4)
        self.batchSelectButton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.batchSelectButton)


        self.verticalLayout_32.addWidget(self.inputFileContainer)

        self.inputFileText = QLineEdit(self.scrollAreaWidgetContents_4)
        self.inputFileText.setObjectName(u"inputFileText")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.inputFileText.sizePolicy().hasHeightForWidth())
        self.inputFileText.setSizePolicy(sizePolicy7)
        self.inputFileText.setMinimumSize(QSize(0, 30))
        self.inputFileText.setMaximumSize(QSize(1000, 30))
        self.inputFileText.setReadOnly(False)

        self.verticalLayout_32.addWidget(self.inputFileText)

        self.outputFileContainer = QWidget(self.scrollAreaWidgetContents_4)
        self.outputFileContainer.setObjectName(u"outputFileContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.outputFileContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.outputFileSelectButton = QPushButton(self.outputFileContainer)
        self.outputFileSelectButton.setObjectName(u"outputFileSelectButton")
        self.outputFileSelectButton.setEnabled(False)
        self.outputFileSelectButton.setMinimumSize(QSize(0, 30))
        self.outputFileSelectButton.setMaximumSize(QSize(16777215, 30))
        self.outputFileSelectButton.setFont(font4)
        self.outputFileSelectButton.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.outputFileSelectButton)

        self.openOutputFolderButton = QPushButton(self.outputFileContainer)
        self.openOutputFolderButton.setObjectName(u"openOutputFolderButton")
        self.openOutputFolderButton.setEnabled(False)
        self.openOutputFolderButton.setMinimumSize(QSize(0, 30))
        self.openOutputFolderButton.setMaximumSize(QSize(16777215, 30))
        self.openOutputFolderButton.setFont(font4)
        self.openOutputFolderButton.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.openOutputFolderButton)


        self.verticalLayout_32.addWidget(self.outputFileContainer)

        self.outputFileText = QLineEdit(self.scrollAreaWidgetContents_4)
        self.outputFileText.setObjectName(u"outputFileText")
        self.outputFileText.setEnabled(False)
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.outputFileText.sizePolicy().hasHeightForWidth())
        self.outputFileText.setSizePolicy(sizePolicy8)
        self.outputFileText.setMinimumSize(QSize(0, 30))
        self.outputFileText.setMaximumSize(QSize(10000, 30))

        self.verticalLayout_32.addWidget(self.outputFileText)

        self.line = QFrame(self.scrollAreaWidgetContents_4)
        self.line.setObjectName(u"line")
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"background: white")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_32.addWidget(self.line)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.backendComboBox = QComboBox(self.widget_3)
        self.backendComboBox.setObjectName(u"backendComboBox")
        sizePolicy8.setHeightForWidth(self.backendComboBox.sizePolicy().hasHeightForWidth())
        self.backendComboBox.setSizePolicy(sizePolicy8)
        self.backendComboBox.setMinimumSize(QSize(0, 0))
        self.backendComboBox.setMaximumSize(QSize(230, 30))

        self.horizontalLayout_11.addWidget(self.backendComboBox)


        self.verticalLayout_32.addWidget(self.widget_3)

        self.widget_35 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_37 = QWidget(self.widget_35)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.widget_37)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font4)

        self.horizontalLayout_56.addWidget(self.label_76)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_21)

        self.interpolateCheckBox = QCheckBox(self.widget_37)
        self.interpolateCheckBox.setObjectName(u"interpolateCheckBox")
        self.interpolateCheckBox.setTristate(False)

        self.horizontalLayout_56.addWidget(self.interpolateCheckBox)


        self.horizontalLayout_7.addWidget(self.widget_37)


        self.verticalLayout_32.addWidget(self.widget_35)

        self.interpolationContainer = QWidget(self.scrollAreaWidgetContents_4)
        self.interpolationContainer.setObjectName(u"interpolationContainer")
        self.interpolationContainer.setEnabled(True)
        self.verticalLayout_38 = QVBoxLayout(self.interpolationContainer)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(9, 9, 9, 9)
        self.widget_28 = QWidget(self.interpolationContainer)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_28)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)

        self.horizontalLayout_45.addWidget(self.label_14)

        self.interpolateModelComboBox = QComboBox(self.widget_28)
        self.interpolateModelComboBox.setObjectName(u"interpolateModelComboBox")
        sizePolicy8.setHeightForWidth(self.interpolateModelComboBox.sizePolicy().hasHeightForWidth())
        self.interpolateModelComboBox.setSizePolicy(sizePolicy8)
        self.interpolateModelComboBox.setMinimumSize(QSize(0, 0))
        self.interpolateModelComboBox.setMaximumSize(QSize(230, 30))
        self.interpolateModelComboBox.setSizeIncrement(QSize(230, 0))

        self.horizontalLayout_45.addWidget(self.interpolateModelComboBox)


        self.verticalLayout_38.addWidget(self.widget_28)

        self.interpolationContainer2 = QWidget(self.interpolationContainer)
        self.interpolationContainer2.setObjectName(u"interpolationContainer2")
        self.horizontalLayout_55 = QHBoxLayout(self.interpolationContainer2)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.interpolationContainer2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.horizontalLayout_55.addWidget(self.label_11)

        self.interpolationMultiplierSpinBox = QDoubleSpinBox(self.interpolationContainer2)
        self.interpolationMultiplierSpinBox.setObjectName(u"interpolationMultiplierSpinBox")
        sizePolicy5.setHeightForWidth(self.interpolationMultiplierSpinBox.sizePolicy().hasHeightForWidth())
        self.interpolationMultiplierSpinBox.setSizePolicy(sizePolicy5)
        self.interpolationMultiplierSpinBox.setMinimumSize(QSize(75, 30))
        self.interpolationMultiplierSpinBox.setMaximumSize(QSize(75, 30))
        self.interpolationMultiplierSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.interpolationMultiplierSpinBox.setDecimals(0)
        self.interpolationMultiplierSpinBox.setMinimum(2.000000000000000)
        self.interpolationMultiplierSpinBox.setValue(2.000000000000000)

        self.horizontalLayout_55.addWidget(self.interpolationMultiplierSpinBox)


        self.verticalLayout_38.addWidget(self.interpolationContainer2)

        self.sloMoModeContainer = QWidget(self.interpolationContainer)
        self.sloMoModeContainer.setObjectName(u"sloMoModeContainer")
        self.horizontalLayout_31 = QHBoxLayout(self.sloMoModeContainer)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.sloMoModeContainer)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font4)

        self.horizontalLayout_31.addWidget(self.label_36)

        self.horizontalSpacer_16 = QSpacerItem(226, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_16)

        self.label_39 = QLabel(self.sloMoModeContainer)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(25, 25))
        self.label_39.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_39.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_39)

        self.sloMoModeCheckBox = QCheckBox(self.sloMoModeContainer)
        self.sloMoModeCheckBox.setObjectName(u"sloMoModeCheckBox")

        self.horizontalLayout_31.addWidget(self.sloMoModeCheckBox)


        self.verticalLayout_38.addWidget(self.sloMoModeContainer)


        self.verticalLayout_32.addWidget(self.interpolationContainer)

        self.decompressModelContainer_2 = QWidget(self.scrollAreaWidgetContents_4)
        self.decompressModelContainer_2.setObjectName(u"decompressModelContainer_2")
        self.horizontalLayout_65 = QHBoxLayout(self.decompressModelContainer_2)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.decompressModelContainer_2)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font4)

        self.horizontalLayout_65.addWidget(self.label_86)

        self.horizontalSpacer_33 = QSpacerItem(324, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_33)

        self.decompressCheckBox = QCheckBox(self.decompressModelContainer_2)
        self.decompressCheckBox.setObjectName(u"decompressCheckBox")

        self.horizontalLayout_65.addWidget(self.decompressCheckBox)


        self.verticalLayout_32.addWidget(self.decompressModelContainer_2)

        self.decompressContainer = QWidget(self.scrollAreaWidgetContents_4)
        self.decompressContainer.setObjectName(u"decompressContainer")
        self.horizontalLayout_66 = QHBoxLayout(self.decompressContainer)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_87 = QLabel(self.decompressContainer)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font4)

        self.horizontalLayout_66.addWidget(self.label_87)

        self.decompressModelComboBox = QComboBox(self.decompressContainer)
        self.decompressModelComboBox.setObjectName(u"decompressModelComboBox")
        sizePolicy8.setHeightForWidth(self.decompressModelComboBox.sizePolicy().hasHeightForWidth())
        self.decompressModelComboBox.setSizePolicy(sizePolicy8)
        self.decompressModelComboBox.setMinimumSize(QSize(0, 0))
        self.decompressModelComboBox.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_66.addWidget(self.decompressModelComboBox)


        self.verticalLayout_32.addWidget(self.decompressContainer)

        self.denoiseCheckBoxContainer = QWidget(self.scrollAreaWidgetContents_4)
        self.denoiseCheckBoxContainer.setObjectName(u"denoiseCheckBoxContainer")
        self.horizontalLayout_62 = QHBoxLayout(self.denoiseCheckBoxContainer)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.denoiseCheckBoxContainer)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font4)

        self.horizontalLayout_62.addWidget(self.label_82)

        self.horizontalSpacer_32 = QSpacerItem(337, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_32)

        self.denoiseCheckBox = QCheckBox(self.denoiseCheckBoxContainer)
        self.denoiseCheckBox.setObjectName(u"denoiseCheckBox")

        self.horizontalLayout_62.addWidget(self.denoiseCheckBox)


        self.verticalLayout_32.addWidget(self.denoiseCheckBoxContainer)

        self.denoiseContainer = QWidget(self.scrollAreaWidgetContents_4)
        self.denoiseContainer.setObjectName(u"denoiseContainer")
        self.horizontalLayout_64 = QHBoxLayout(self.denoiseContainer)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.widget_44 = QWidget(self.denoiseContainer)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_63 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_83 = QLabel(self.widget_44)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font4)

        self.horizontalLayout_63.addWidget(self.label_83)

        self.denoiseModelComboBox = QComboBox(self.widget_44)
        self.denoiseModelComboBox.setObjectName(u"denoiseModelComboBox")
        sizePolicy8.setHeightForWidth(self.denoiseModelComboBox.sizePolicy().hasHeightForWidth())
        self.denoiseModelComboBox.setSizePolicy(sizePolicy8)
        self.denoiseModelComboBox.setMinimumSize(QSize(0, 0))
        self.denoiseModelComboBox.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_63.addWidget(self.denoiseModelComboBox)


        self.horizontalLayout_64.addWidget(self.widget_44)


        self.verticalLayout_32.addWidget(self.denoiseContainer)

        self.deblurCheckBoxContainer = QWidget(self.scrollAreaWidgetContents_4)
        self.deblurCheckBoxContainer.setObjectName(u"deblurCheckBoxContainer")
        self.horizontalLayout_59 = QHBoxLayout(self.deblurCheckBoxContainer)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_78 = QLabel(self.deblurCheckBoxContainer)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font4)

        self.horizontalLayout_59.addWidget(self.label_78)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_28)

        self.deblurCheckBox = QCheckBox(self.deblurCheckBoxContainer)
        self.deblurCheckBox.setObjectName(u"deblurCheckBox")

        self.horizontalLayout_59.addWidget(self.deblurCheckBox)


        self.verticalLayout_32.addWidget(self.deblurCheckBoxContainer)

        self.deblurContainer = QWidget(self.scrollAreaWidgetContents_4)
        self.deblurContainer.setObjectName(u"deblurContainer")
        self.verticalLayout_41 = QVBoxLayout(self.deblurContainer)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_43 = QWidget(self.deblurContainer)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(9, 9, 9, 9)
        self.label_79 = QLabel(self.widget_43)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font4)

        self.horizontalLayout_60.addWidget(self.label_79)

        self.deblurModelComboBox = QComboBox(self.widget_43)
        self.deblurModelComboBox.setObjectName(u"deblurModelComboBox")
        sizePolicy8.setHeightForWidth(self.deblurModelComboBox.sizePolicy().hasHeightForWidth())
        self.deblurModelComboBox.setSizePolicy(sizePolicy8)
        self.deblurModelComboBox.setMinimumSize(QSize(0, 0))
        self.deblurModelComboBox.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_60.addWidget(self.deblurModelComboBox)


        self.verticalLayout_41.addWidget(self.widget_43)


        self.verticalLayout_32.addWidget(self.deblurContainer)

        self.widget_38 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.widget_39 = QWidget(self.widget_38)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.widget_39)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font4)

        self.horizontalLayout_57.addWidget(self.label_77)

        self.horizontalSpacer_27 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_27)

        self.upscaleCheckBox = QCheckBox(self.widget_39)
        self.upscaleCheckBox.setObjectName(u"upscaleCheckBox")

        self.horizontalLayout_57.addWidget(self.upscaleCheckBox)


        self.horizontalLayout_58.addWidget(self.widget_39)


        self.verticalLayout_32.addWidget(self.widget_38, 0, Qt.AlignmentFlag.AlignTop)

        self.generalUpscaleContainer = QWidget(self.scrollAreaWidgetContents_4)
        self.generalUpscaleContainer.setObjectName(u"generalUpscaleContainer")
        self.verticalLayout_39 = QVBoxLayout(self.generalUpscaleContainer)
        self.verticalLayout_39.setSpacing(6)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(9, 9, 9, 9)
        self.widget = QWidget(self.generalUpscaleContainer)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.horizontalLayout.addWidget(self.label_7)

        self.upscaleModelComboBox = QComboBox(self.widget)
        self.upscaleModelComboBox.setObjectName(u"upscaleModelComboBox")
        sizePolicy8.setHeightForWidth(self.upscaleModelComboBox.sizePolicy().hasHeightForWidth())
        self.upscaleModelComboBox.setSizePolicy(sizePolicy8)
        self.upscaleModelComboBox.setMinimumSize(QSize(0, 0))
        self.upscaleModelComboBox.setMaximumSize(QSize(250, 30))

        self.horizontalLayout.addWidget(self.upscaleModelComboBox)


        self.verticalLayout_39.addWidget(self.widget)

        self.widget_42 = QWidget(self.generalUpscaleContainer)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_50.setSpacing(6)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.widget_42)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font4)

        self.horizontalLayout_50.addWidget(self.label_72)

        self.label_73 = QLabel(self.widget_42)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMaximumSize(QSize(25, 25))
        self.label_73.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_73.setScaledContents(True)

        self.horizontalLayout_50.addWidget(self.label_73)

        self.upscaleScaleSpinBox = QDoubleSpinBox(self.widget_42)
        self.upscaleScaleSpinBox.setObjectName(u"upscaleScaleSpinBox")
        sizePolicy5.setHeightForWidth(self.upscaleScaleSpinBox.sizePolicy().hasHeightForWidth())
        self.upscaleScaleSpinBox.setSizePolicy(sizePolicy5)
        self.upscaleScaleSpinBox.setMinimumSize(QSize(75, 30))
        self.upscaleScaleSpinBox.setMaximumSize(QSize(75, 30))
        self.upscaleScaleSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.upscaleScaleSpinBox.setDecimals(0)
        self.upscaleScaleSpinBox.setMinimum(1.000000000000000)
        self.upscaleScaleSpinBox.setMaximum(4.000000000000000)
        self.upscaleScaleSpinBox.setValue(2.000000000000000)

        self.horizontalLayout_50.addWidget(self.upscaleScaleSpinBox)


        self.verticalLayout_39.addWidget(self.widget_42)


        self.verticalLayout_32.addWidget(self.generalUpscaleContainer, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_25 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.addToRenderQueueButton = QPushButton(self.widget_25)
        self.addToRenderQueueButton.setObjectName(u"addToRenderQueueButton")
        sizePolicy5.setHeightForWidth(self.addToRenderQueueButton.sizePolicy().hasHeightForWidth())
        self.addToRenderQueueButton.setSizePolicy(sizePolicy5)
        self.addToRenderQueueButton.setMaximumSize(QSize(200, 35))
        self.addToRenderQueueButton.setStyleSheet(u"QPushButton{\n"
"text-align: center;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/plus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addToRenderQueueButton.setIcon(icon2)
        self.addToRenderQueueButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_40.addWidget(self.addToRenderQueueButton)


        self.verticalLayout_32.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy5.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy5)
        self.widget_26.setMaximumSize(QSize(42344, 200))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.inputVideoInfoTextEdit = QTextEdit(self.widget_26)
        self.inputVideoInfoTextEdit.setObjectName(u"inputVideoInfoTextEdit")
        self.inputVideoInfoTextEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.inputVideoInfoTextEdit.sizePolicy().hasHeightForWidth())
        self.inputVideoInfoTextEdit.setSizePolicy(sizePolicy3)
        self.inputVideoInfoTextEdit.setMinimumSize(QSize(0, 190))
        self.inputVideoInfoTextEdit.setMaximumSize(QSize(100000, 180))
#if QT_CONFIG(accessibility)
        self.inputVideoInfoTextEdit.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.inputVideoInfoTextEdit.setStyleSheet(u"\n"
"QTextEdit:disabled{color:white;}")
        self.inputVideoInfoTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.inputVideoInfoTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.inputVideoInfoTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.inputVideoInfoTextEdit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.inputVideoInfoTextEdit.setReadOnly(True)
        self.inputVideoInfoTextEdit.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Adwaita Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt;\">FPS:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt;\">Resolution:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt;\">Frame Count:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt;\">Encoder:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt;\">Container:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt;\">Color Space:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt;\">Pixel Format:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt;\">Is HDR:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt;\">Bit Depth:</span></p></body></html>")

        self.horizontalLayout_22.addWidget(self.inputVideoInfoTextEdit)


        self.verticalLayout_32.addWidget(self.widget_26)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_13.addWidget(self.scrollArea_4)


        self.verticalLayout_10.addWidget(self.widget_5)

        self.processSettingsContainer.addTab(self.generalSettings, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_43 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.widget_6 = QWidget(self.tab_6)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_15 = QVBoxLayout(self.widget_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_7 = QScrollArea(self.widget_6)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.encoderSettings = QWidget()
        self.encoderSettings.setObjectName(u"encoderSettings")
        self.encoderSettings.setGeometry(QRect(0, 0, 453, 581))
        self.verticalLayout_40 = QVBoxLayout(self.encoderSettings)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.widget_34 = QWidget(self.encoderSettings)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy2.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy2)
        self.verticalLayout_36 = QVBoxLayout(self.widget_34)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_33 = QWidget(self.widget_34)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy9)
        self.widget_33.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_9 = QVBoxLayout(self.widget_33)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.widget_33)
        self.label_74.setObjectName(u"label_74")
        font5 = QFont()
        font5.setPointSize(15)
        font5.setUnderline(True)
        self.label_74.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_74)

        self.widget_32 = QWidget(self.widget_33)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.scrollArea_6 = QScrollArea(self.widget_32)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        sizePolicy7.setHeightForWidth(self.scrollArea_6.sizePolicy().hasHeightForWidth())
        self.scrollArea_6.setSizePolicy(sizePolicy7)
        self.scrollArea_6.setMinimumSize(QSize(0, 50))
        self.scrollArea_6.setMaximumSize(QSize(16777215, 50))
        self.scrollArea_6.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_6.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 918, 48))
        self.horizontalLayout_54 = QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.EncoderCommand = QLineEdit(self.scrollAreaWidgetContents_6)
        self.EncoderCommand.setObjectName(u"EncoderCommand")
        self.EncoderCommand.setMinimumSize(QSize(900, 30))

        self.horizontalLayout_54.addWidget(self.EncoderCommand)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_51.addWidget(self.scrollArea_6)

        self.label_75 = QLabel(self.widget_32)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(25, 25))
        self.label_75.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_75.setScaledContents(True)

        self.horizontalLayout_51.addWidget(self.label_75)


        self.verticalLayout_9.addWidget(self.widget_32)


        self.verticalLayout_36.addWidget(self.widget_33)


        self.verticalLayout_40.addWidget(self.widget_34)

        self.widget_15 = QWidget(self.encoderSettings)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_26 = QVBoxLayout(self.widget_15)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.encoderLabel = QLabel(self.widget_17)
        self.encoderLabel.setObjectName(u"encoderLabel")
        self.encoderLabel.setFont(font4)

        self.horizontalLayout_15.addWidget(self.encoderLabel)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)

        self.label_54 = QLabel(self.widget_17)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(25, 25))
        self.label_54.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_54.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_54)

        self.encoder = QComboBox(self.widget_17)
        self.encoder.addItem("")
        self.encoder.addItem("")
        self.encoder.addItem("")
        self.encoder.addItem("")
        self.encoder.addItem("")
        self.encoder.addItem("")
        self.encoder.addItem("")
        self.encoder.addItem("")
        self.encoder.addItem("")
        self.encoder.addItem("")
        self.encoder.setObjectName(u"encoder")
        self.encoder.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_15.addWidget(self.encoder)


        self.verticalLayout_26.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.encoderLabel_2 = QLabel(self.widget_16)
        self.encoderLabel_2.setObjectName(u"encoderLabel_2")
        self.encoderLabel_2.setFont(font4)

        self.horizontalLayout_36.addWidget(self.encoderLabel_2)

        self.horizontalSpacer_22 = QSpacerItem(237, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_22)

        self.label_55 = QLabel(self.widget_16)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(25, 25))
        self.label_55.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_55.setScaledContents(True)

        self.horizontalLayout_36.addWidget(self.label_55)

        self.video_encoder_speed = QComboBox(self.widget_16)
        self.video_encoder_speed.addItem("")
        self.video_encoder_speed.addItem("")
        self.video_encoder_speed.addItem("")
        self.video_encoder_speed.addItem("")
        self.video_encoder_speed.addItem("")
        self.video_encoder_speed.setObjectName(u"video_encoder_speed")
        self.video_encoder_speed.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_36.addWidget(self.video_encoder_speed)


        self.verticalLayout_26.addWidget(self.widget_16)

        self.widget_18 = QWidget(self.widget_15)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.encoderLabel_5 = QLabel(self.widget_18)
        self.encoderLabel_5.setObjectName(u"encoderLabel_5")
        self.encoderLabel_5.setFont(font4)

        self.horizontalLayout_33.addWidget(self.encoderLabel_5)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_17)

        self.video_quality = QComboBox(self.widget_18)
        self.video_quality.addItem("")
        self.video_quality.addItem("")
        self.video_quality.addItem("")
        self.video_quality.addItem("")
        self.video_quality.addItem("")
        self.video_quality.addItem("")
        self.video_quality.setObjectName(u"video_quality")
        self.video_quality.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_33.addWidget(self.video_quality)


        self.verticalLayout_26.addWidget(self.widget_18)

        self.widget_27 = QWidget(self.widget_15)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_49 = QLabel(self.widget_27)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font4)

        self.horizontalLayout_44.addWidget(self.label_49)

        self.horizontalSpacer_19 = QSpacerItem(437, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_19)

        self.label_50 = QLabel(self.widget_27)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(25, 25))
        self.label_50.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_50.setScaledContents(True)

        self.horizontalLayout_44.addWidget(self.label_50)

        self.video_container = QComboBox(self.widget_27)
        self.video_container.addItem("")
        self.video_container.addItem("")
        self.video_container.addItem("")
        self.video_container.addItem("")
        self.video_container.addItem("")
        self.video_container.setObjectName(u"video_container")

        self.horizontalLayout_44.addWidget(self.video_container)


        self.verticalLayout_26.addWidget(self.widget_27)

        self.widget_21 = QWidget(self.widget_15)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.encoderLabel_7 = QLabel(self.widget_21)
        self.encoderLabel_7.setObjectName(u"encoderLabel_7")
        self.encoderLabel_7.setFont(font4)

        self.horizontalLayout_35.addWidget(self.encoderLabel_7)

        self.horizontalSpacer_20 = QSpacerItem(469, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_20)

        self.label_58 = QLabel(self.widget_21)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(25, 25))
        self.label_58.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_58.setScaledContents(True)

        self.horizontalLayout_35.addWidget(self.label_58)

        self.video_pixel_format = QComboBox(self.widget_21)
        self.video_pixel_format.addItem("")
        self.video_pixel_format.addItem("")
        self.video_pixel_format.addItem("")
        self.video_pixel_format.addItem("")
        self.video_pixel_format.addItem("")
        self.video_pixel_format.addItem("")
        self.video_pixel_format.setObjectName(u"video_pixel_format")
        self.video_pixel_format.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_35.addWidget(self.video_pixel_format)


        self.verticalLayout_26.addWidget(self.widget_21)

        self.widget_20 = QWidget(self.widget_15)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.encoderLabel_10 = QLabel(self.widget_20)
        self.encoderLabel_10.setObjectName(u"encoderLabel_10")
        self.encoderLabel_10.setFont(font4)

        self.horizontalLayout_34.addWidget(self.encoderLabel_10)

        self.horizontalSpacer_30 = QSpacerItem(382, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_30)

        self.label_56 = QLabel(self.widget_20)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(25, 25))
        self.label_56.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_56.setScaledContents(True)

        self.horizontalLayout_34.addWidget(self.label_56)

        self.audio_encoder = QComboBox(self.widget_20)
        self.audio_encoder.addItem("")
        self.audio_encoder.addItem("")
        self.audio_encoder.addItem("")
        self.audio_encoder.addItem("")
        self.audio_encoder.setObjectName(u"audio_encoder")
        self.audio_encoder.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_34.addWidget(self.audio_encoder)


        self.verticalLayout_26.addWidget(self.widget_20)

        self.widget_36 = QWidget(self.widget_15)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.encoderLabel_6 = QLabel(self.widget_36)
        self.encoderLabel_6.setObjectName(u"encoderLabel_6")
        self.encoderLabel_6.setFont(font4)

        self.horizontalLayout_2.addWidget(self.encoderLabel_6)

        self.horizontalSpacer_18 = QSpacerItem(494, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_18)

        self.label_57 = QLabel(self.widget_36)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(25, 25))
        self.label_57.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_57.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_57)

        self.audio_bitrate = QComboBox(self.widget_36)
        self.audio_bitrate.addItem("")
        self.audio_bitrate.addItem("")
        self.audio_bitrate.addItem("")
        self.audio_bitrate.addItem("")
        self.audio_bitrate.setObjectName(u"audio_bitrate")
        self.audio_bitrate.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.audio_bitrate)


        self.verticalLayout_26.addWidget(self.widget_36)

        self.widget_41 = QWidget(self.widget_15)
        self.widget_41.setObjectName(u"widget_41")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.encoderLabel_11 = QLabel(self.widget_41)
        self.encoderLabel_11.setObjectName(u"encoderLabel_11")
        self.encoderLabel_11.setFont(font4)

        self.horizontalLayout_41.addWidget(self.encoderLabel_11)

        self.horizontalSpacer_35 = QSpacerItem(382, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_35)

        self.label_59 = QLabel(self.widget_41)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(25, 25))
        self.label_59.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_59.setScaledContents(True)

        self.horizontalLayout_41.addWidget(self.label_59)

        self.subtitle_encoder = QComboBox(self.widget_41)
        self.subtitle_encoder.addItem("")
        self.subtitle_encoder.addItem("")
        self.subtitle_encoder.addItem("")
        self.subtitle_encoder.addItem("")
        self.subtitle_encoder.setObjectName(u"subtitle_encoder")
        self.subtitle_encoder.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_41.addWidget(self.subtitle_encoder)


        self.verticalLayout_26.addWidget(self.widget_41)


        self.verticalLayout_40.addWidget(self.widget_15)

        self.verticalSpacer_2 = QSpacerItem(20, 50000, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_2)

        self.scrollArea_7.setWidget(self.encoderSettings)

        self.verticalLayout_15.addWidget(self.scrollArea_7)


        self.horizontalLayout_43.addWidget(self.widget_6)

        self.processSettingsContainer.addTab(self.tab_6, "")
        self.renderQueueTab = QWidget()
        self.renderQueueTab.setObjectName(u"renderQueueTab")
        sizePolicy1.setHeightForWidth(self.renderQueueTab.sizePolicy().hasHeightForWidth())
        self.renderQueueTab.setSizePolicy(sizePolicy1)
        self.renderQueueTab.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_27 = QVBoxLayout(self.renderQueueTab)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_22 = QWidget(self.renderQueueTab)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.renderQueueListWidget = QListWidget(self.widget_22)
        self.renderQueueListWidget.setObjectName(u"renderQueueListWidget")
        sizePolicy.setHeightForWidth(self.renderQueueListWidget.sizePolicy().hasHeightForWidth())
        self.renderQueueListWidget.setSizePolicy(sizePolicy)
        self.renderQueueListWidget.setMinimumSize(QSize(0, 0))
        self.renderQueueListWidget.setMaximumSize(QSize(335, 16777215))
        self.renderQueueListWidget.setStyleSheet(u"QListWidget{\n"
"background-color:#1f232a;\n"
"border-radius:10px;\n"
"}")
        self.renderQueueListWidget.setProperty(u"showDropIndicator", True)

        self.horizontalLayout_38.addWidget(self.renderQueueListWidget)

        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_28 = QVBoxLayout(self.widget_23)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.RemoveFromRenderQueue = QPushButton(self.widget_23)
        self.RemoveFromRenderQueue.setObjectName(u"RemoveFromRenderQueue")

        self.verticalLayout_28.addWidget(self.RemoveFromRenderQueue)

        self.MoveUpRenderQueue = QPushButton(self.widget_23)
        self.MoveUpRenderQueue.setObjectName(u"MoveUpRenderQueue")

        self.verticalLayout_28.addWidget(self.MoveUpRenderQueue)

        self.MoveDownRenderQueue = QPushButton(self.widget_23)
        self.MoveDownRenderQueue.setObjectName(u"MoveDownRenderQueue")

        self.verticalLayout_28.addWidget(self.MoveDownRenderQueue)


        self.horizontalLayout_38.addWidget(self.widget_23)


        self.verticalLayout_27.addWidget(self.widget_22)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.OutputFilesListWidget = QListWidget(self.renderQueueTab)
        self.OutputFilesListWidget.setObjectName(u"OutputFilesListWidget")
        sizePolicy5.setHeightForWidth(self.OutputFilesListWidget.sizePolicy().hasHeightForWidth())
        self.OutputFilesListWidget.setSizePolicy(sizePolicy5)
        self.OutputFilesListWidget.setMinimumSize(QSize(0, 0))
        self.OutputFilesListWidget.setMaximumSize(QSize(16777215, 16777215))
        self.OutputFilesListWidget.setStyleSheet(u"QListWidget{\n"
"background-color:#1f232a;\n"
"border-radius:10px;\n"
"}")

        self.gridLayout_4.addWidget(self.OutputFilesListWidget, 1, 0, 1, 1)

        self.label_51 = QLabel(self.renderQueueTab)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_4.addWidget(self.label_51, 0, 0, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_4)

        self.processSettingsContainer.addTab(self.renderQueueTab, "")
        self.advancedSettings = QWidget()
        self.advancedSettings.setObjectName(u"advancedSettings")
        sizePolicy3.setHeightForWidth(self.advancedSettings.sizePolicy().hasHeightForWidth())
        self.advancedSettings.setSizePolicy(sizePolicy3)
        self.advancedSettings.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_29 = QVBoxLayout(self.advancedSettings)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.scrollArea_5 = QScrollArea(self.advancedSettings)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        sizePolicy3.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy3)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 460, 516))
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents_5.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_5.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents_5.setMinimumSize(QSize(0, 0))
        self.verticalLayout_33 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_33.setSpacing(9)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(11, 11, 11, 11)
        self.generalContainer = QWidget(self.scrollAreaWidgetContents_5)
        self.generalContainer.setObjectName(u"generalContainer")
        sizePolicy2.setHeightForWidth(self.generalContainer.sizePolicy().hasHeightForWidth())
        self.generalContainer.setSizePolicy(sizePolicy2)
        self.verticalLayout_31 = QVBoxLayout(self.generalContainer)
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.generalContainer)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font5)

        self.verticalLayout_31.addWidget(self.label_41)

        self.benchmarkModeContainer = QWidget(self.generalContainer)
        self.benchmarkModeContainer.setObjectName(u"benchmarkModeContainer")
        self.horizontalLayout_42 = QHBoxLayout(self.benchmarkModeContainer)
        self.horizontalLayout_42.setSpacing(6)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(9, 9, 9, 9)
        self.label_18 = QLabel(self.benchmarkModeContainer)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font4)

        self.horizontalLayout_42.addWidget(self.label_18)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.benchmarkModeContainer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(25, 25))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_42.addWidget(self.label_5)

        self.benchmarkModeCheckBox = QCheckBox(self.benchmarkModeContainer)
        self.benchmarkModeCheckBox.setObjectName(u"benchmarkModeCheckBox")
        self.benchmarkModeCheckBox.setStyleSheet(u"")

        self.horizontalLayout_42.addWidget(self.benchmarkModeCheckBox)


        self.verticalLayout_31.addWidget(self.benchmarkModeContainer)


        self.verticalLayout_33.addWidget(self.generalContainer, 0, Qt.AlignmentFlag.AlignTop)

        self.upscaleContainer = QWidget(self.scrollAreaWidgetContents_5)
        self.upscaleContainer.setObjectName(u"upscaleContainer")
        sizePolicy2.setHeightForWidth(self.upscaleContainer.sizePolicy().hasHeightForWidth())
        self.upscaleContainer.setSizePolicy(sizePolicy2)
        self.upscaleContainer.setMinimumSize(QSize(351, 128))
        self.verticalLayout_16 = QVBoxLayout(self.upscaleContainer)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.upscaleContainer)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_40)

        self.tilingContainer = QWidget(self.upscaleContainer)
        self.tilingContainer.setObjectName(u"tilingContainer")
        self.horizontalLayout_16 = QHBoxLayout(self.tilingContainer)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 0, 9, 9)
        self.label_33 = QLabel(self.tilingContainer)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font4)

        self.horizontalLayout_16.addWidget(self.label_33)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)

        self.label_34 = QLabel(self.tilingContainer)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(25, 25))
        self.label_34.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_34.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_34)

        self.tilingCheckBox = QCheckBox(self.tilingContainer)
        self.tilingCheckBox.setObjectName(u"tilingCheckBox")

        self.horizontalLayout_16.addWidget(self.tilingCheckBox)


        self.verticalLayout_16.addWidget(self.tilingContainer)

        self.tileSizeContainer = QWidget(self.upscaleContainer)
        self.tileSizeContainer.setObjectName(u"tileSizeContainer")
        self.horizontalLayout_18 = QHBoxLayout(self.tileSizeContainer)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(9, 0, 9, 0)
        self.label_32 = QLabel(self.tileSizeContainer)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font4)

        self.horizontalLayout_18.addWidget(self.label_32)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)

        self.tileSizeComboBox = QComboBox(self.tileSizeContainer)
        self.tileSizeComboBox.addItem("")
        self.tileSizeComboBox.addItem("")
        self.tileSizeComboBox.addItem("")
        self.tileSizeComboBox.addItem("")
        self.tileSizeComboBox.addItem("")
        self.tileSizeComboBox.setObjectName(u"tileSizeComboBox")

        self.horizontalLayout_18.addWidget(self.tileSizeComboBox)


        self.verticalLayout_16.addWidget(self.tileSizeContainer)


        self.verticalLayout_33.addWidget(self.upscaleContainer, 0, Qt.AlignmentFlag.AlignTop)

        self.interpolateContainer_2 = QWidget(self.scrollAreaWidgetContents_5)
        self.interpolateContainer_2.setObjectName(u"interpolateContainer_2")
        sizePolicy2.setHeightForWidth(self.interpolateContainer_2.sizePolicy().hasHeightForWidth())
        self.interpolateContainer_2.setSizePolicy(sizePolicy2)
        self.interpolateContainer = QVBoxLayout(self.interpolateContainer_2)
        self.interpolateContainer.setSpacing(0)
        self.interpolateContainer.setObjectName(u"interpolateContainer")
        self.interpolateContainer.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.interpolateContainer_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font5)

        self.interpolateContainer.addWidget(self.label_42)

        self.sloMoModeContainer_5 = QWidget(self.interpolateContainer_2)
        self.sloMoModeContainer_5.setObjectName(u"sloMoModeContainer_5")
        self.horizontalLayout_53 = QHBoxLayout(self.sloMoModeContainer_5)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_70 = QLabel(self.sloMoModeContainer_5)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font4)

        self.horizontalLayout_53.addWidget(self.label_70)

        self.horizontalSpacer_26 = QSpacerItem(226, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_26)

        self.label_71 = QLabel(self.sloMoModeContainer_5)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(25, 25))
        self.label_71.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_71.setScaledContents(True)

        self.horizontalLayout_53.addWidget(self.label_71)

        self.dynamicScaledOpticalFlowCheckBox = QCheckBox(self.sloMoModeContainer_5)
        self.dynamicScaledOpticalFlowCheckBox.setObjectName(u"dynamicScaledOpticalFlowCheckBox")

        self.horizontalLayout_53.addWidget(self.dynamicScaledOpticalFlowCheckBox)


        self.interpolateContainer.addWidget(self.sloMoModeContainer_5)

        self.sloMoModeContainer_4 = QWidget(self.interpolateContainer_2)
        self.sloMoModeContainer_4.setObjectName(u"sloMoModeContainer_4")
        self.horizontalLayout_52 = QHBoxLayout(self.sloMoModeContainer_4)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_68 = QLabel(self.sloMoModeContainer_4)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font4)

        self.horizontalLayout_52.addWidget(self.label_68)

        self.horizontalSpacer_25 = QSpacerItem(226, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_25)

        self.label_69 = QLabel(self.sloMoModeContainer_4)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(25, 25))
        self.label_69.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_69.setScaledContents(True)

        self.horizontalLayout_52.addWidget(self.label_69)

        self.ensembleCheckBox = QCheckBox(self.sloMoModeContainer_4)
        self.ensembleCheckBox.setObjectName(u"ensembleCheckBox")

        self.horizontalLayout_52.addWidget(self.ensembleCheckBox)


        self.interpolateContainer.addWidget(self.sloMoModeContainer_4)


        self.verticalLayout_33.addWidget(self.interpolateContainer_2, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_19 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")

        self.verticalLayout_33.addWidget(self.widget_19)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_29.addWidget(self.scrollArea_5)

        self.processSettingsContainer.addTab(self.advancedSettings, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.renderOutput = QTextEdit(self.tab_5)
        self.renderOutput.setObjectName(u"renderOutput")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.renderOutput.sizePolicy().hasHeightForWidth())
        self.renderOutput.setSizePolicy(sizePolicy10)
        font6 = QFont()
        font6.setPointSize(13)
        self.renderOutput.setFont(font6)
        self.renderOutput.setStyleSheet(u"*:disabled{\n"
" \n"
"	color:white;\n"
"}")
        self.renderOutput.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.renderOutput.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.renderOutput.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.renderOutput)

        self.processSettingsContainer.addTab(self.tab_5, "")

        self.verticalLayout_24.addWidget(self.processSettingsContainer)


        self.verticalLayout_21.addWidget(self.widget_2)

        self.widget_13 = QWidget(self.bottomMenuSubContainer)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(500, 16777215))
        self.widget_13.setStyleSheet(u"")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_32.setSpacing(6)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(9, 9, 9, 9)
        self.widget_24 = QWidget(self.widget_13)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.startRenderButton = QPushButton(self.widget_24)
        self.startRenderButton.setObjectName(u"startRenderButton")
        self.startRenderButton.setEnabled(True)
        self.startRenderButton.setMaximumSize(QSize(59, 55))
        self.startRenderButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.startRenderButton.setIcon(icon3)
        self.startRenderButton.setIconSize(QSize(40, 45))
        self.startRenderButton.setCheckable(False)
        self.startRenderButton.setChecked(False)
        self.startRenderButton.setAutoRepeat(False)
        self.startRenderButton.setAutoExclusive(False)

        self.horizontalLayout_39.addWidget(self.startRenderButton)


        self.horizontalLayout_32.addWidget(self.widget_24)

        self.onRenderButtonsContiainer = QHBoxLayout()
        self.onRenderButtonsContiainer.setObjectName(u"onRenderButtonsContiainer")
        self.pauseRenderButton = QPushButton(self.widget_13)
        self.pauseRenderButton.setObjectName(u"pauseRenderButton")
        self.pauseRenderButton.setEnabled(True)
        self.pauseRenderButton.setMaximumSize(QSize(59, 55))
        self.pauseRenderButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/pause-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pauseRenderButton.setIcon(icon4)
        self.pauseRenderButton.setIconSize(QSize(40, 45))
        self.pauseRenderButton.setCheckable(False)
        self.pauseRenderButton.setChecked(False)

        self.onRenderButtonsContiainer.addWidget(self.pauseRenderButton)

        self.killRenderButton = QPushButton(self.widget_13)
        self.killRenderButton.setObjectName(u"killRenderButton")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.killRenderButton.sizePolicy().hasHeightForWidth())
        self.killRenderButton.setSizePolicy(sizePolicy11)
        self.killRenderButton.setMaximumSize(QSize(59, 55))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.killRenderButton.setIcon(icon5)
        self.killRenderButton.setIconSize(QSize(40, 45))

        self.onRenderButtonsContiainer.addWidget(self.killRenderButton)


        self.horizontalLayout_32.addLayout(self.onRenderButtonsContiainer)

        self.progressBar = QProgressBar(self.widget_13)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy7.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy7)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_32.addWidget(self.progressBar)


        self.verticalLayout_21.addWidget(self.widget_13)


        self.verticalLayout_7.addWidget(self.bottomMenuSubContainer)


        self.gridLayout_3.addWidget(self.processContainer, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.procPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.settingsPage.setStyleSheet(u"QWidget{\n"
"background-color:#16191d\n"
"\n"
"}\n"
"QScrollArea{\n"
"	background:transparent;\n"
"}\n"
"QLineEdit{\n"
"background-color:#2c313c;\n"
"border-radius: 10px;\n"
"}\n"
"QSpinBox{\n"
"	background-color:#2c313c;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"       \n"
"		image: url(:/icons/icons/arrow-up.svg); \n"
"    }\n"
"QSpinBox::down-arrow {\n"
"\n"
"        image: url(:/icons/icons/arrow-down.svg); \n"
"		\n"
"    }\n"
"QSpinBox::up-button {\n"
"        width: 20px;\n"
"        height: 15px;\n"
"    }\n"
"QSpinBox::down-button {\n"
"        width: 20px;\n"
"        height: 15px;\n"
"    }\n"
"QTextEdit{\n"
"background-color:#2c313c;\n"
"border-radius: 10px;\n"
"padding:5px 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#2c313c;\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#676e7b;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#343b47;\n"
"}\n"
""
                        "\n"
"QComboBox{\n"
"background-color:#2c313c;\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"color:white;\n"
"}\n"
"\n"
"QProgressBar{\n"
"    background-color:#2c313c;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
" QProgressBar::chunk {\n"
"     background-color:white;\n"
"	text-align:left;\n"
"	border-radius: 10px;\n"
"	\n"
" }\n"
"\n"
"\n"
"Line{\n"
"color:white;\n"
"background-color:white;\n"
"}\n"
"QDoubleSpinBox{\n"
"	background-color:#2c313c;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"	color:white;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"       \n"
"		image: url(:/icons/icons/arrow-up.svg); \n"
"    }\n"
"QDoubleSpinBox::down-arrow {\n"
"\n"
"        image: url(:/icons/icons/arrow-down.svg); \n"
"		\n"
"    }\n"
"QDoubleSpinBox::up-button {\n"
"        width: 20px;\n"
"        height: 15px;\n"
"    }\n"
"QDoubleSpinBox::down-button {\n"
"        width: 20px;\n"
"        height: 15px;\n"
"    }\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"                border-"
                        "top: 0px solid #C2C7CB;\n"
"                top: -0.5em;\n"
"                background: transparent;\n"
"            }\n"
"\n"
"            QTabWidget::tab-bar {\n"
"                alignment: left;\n"
"            }\n"
"\n"
"            QTabBar::tab {\n"
"                background: #1f232a;\n"
"                border: 0px solid #C4C4C3;\n"
"                border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"                border-top-left-radius: 4px;\n"
"                border-top-right-radius: 4px;\n"
"				  border-bottom-left-radius: 4px;\n"
"                border-bottom-right-radius: 4px;\n"
"                min-width: 8ex;\n"
"                padding: 6px;\n"
"				  color: #fff;\n"
"            }\n"
"\n"
"            QTabBar::tab:selected{\n"
"                background:#676e7b;\n"
"            }\n"
"            QTabBar::tab:hover {\n"
"				background: #343b47;\n"
"				}\n"
"\n"
"            QTabBar::tab:selected {\n"
"                border-color: transparent;\n"
"                border-bo"
                        "ttom-color: transparent; /* same as pane color */\n"
"            }\n"
"\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }\n"
"\n"
"            QTabBar::tab:selected {\n"
"                /* expand/overlap to the left and right by 4px */\n"
"                margin-left: 2px;\n"
"                margin-right: 2px;\n"
"            }\n"
"\n"
"            QTabBar::tab:first:selected {\n"
"                margin-left: 0; /* the first selected tab should not overlap */\n"
"            }\n"
"\n"
"            QTabBar::tab:last:selected {\n"
"                margin-right: 0; /* the last selected tab should not overlap */\n"
"            }\n"
"\n"
"            QTabBar::tab:only-one {\n"
"                margin: 0; /* if there is only one tab, it should not overlap */\n"
"            }")
        self.verticalLayout_14 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea = QScrollArea(self.settingsPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 112312))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1026, 652))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_17 = QVBoxLayout(self.tab_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.VideoSettingsContainer = QWidget(self.tab_2)
        self.VideoSettingsContainer.setObjectName(u"VideoSettingsContainer")
        self.verticalLayout_19 = QVBoxLayout(self.VideoSettingsContainer)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.VideoSettingsContainer)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 968, 528))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.outputFileLocationContianer = QWidget(self.scrollAreaWidgetContents_3)
        self.outputFileLocationContianer.setObjectName(u"outputFileLocationContianer")
        self.horizontalLayout_19 = QHBoxLayout(self.outputFileLocationContianer)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.encoderLabel_3 = QLabel(self.outputFileLocationContianer)
        self.encoderLabel_3.setObjectName(u"encoderLabel_3")
        self.encoderLabel_3.setFont(font4)

        self.horizontalLayout_19.addWidget(self.encoderLabel_3)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)

        self.output_folder_location = QLineEdit(self.outputFileLocationContianer)
        self.output_folder_location.setObjectName(u"output_folder_location")
        self.output_folder_location.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_19.addWidget(self.output_folder_location)

        self.select_output_folder_location_btn = QPushButton(self.outputFileLocationContianer)
        self.select_output_folder_location_btn.setObjectName(u"select_output_folder_location_btn")

        self.horizontalLayout_19.addWidget(self.select_output_folder_location_btn)


        self.verticalLayout_25.addWidget(self.outputFileLocationContianer)

        self.sceneChangeDetectionSettingContainer = QWidget(self.scrollAreaWidgetContents_3)
        self.sceneChangeDetectionSettingContainer.setObjectName(u"sceneChangeDetectionSettingContainer")
        self.horizontalLayout_17 = QHBoxLayout(self.sceneChangeDetectionSettingContainer)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.sceneChangeDetectionSettingContainer)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)

        self.horizontalLayout_17.addWidget(self.label_20)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)

        self.label_24 = QLabel(self.sceneChangeDetectionSettingContainer)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(25, 25))
        self.label_24.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_24.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_24)

        self.scene_change_detection_enabled = QCheckBox(self.sceneChangeDetectionSettingContainer)
        self.scene_change_detection_enabled.setObjectName(u"scene_change_detection_enabled")

        self.horizontalLayout_17.addWidget(self.scene_change_detection_enabled)


        self.verticalLayout_25.addWidget(self.sceneChangeDetectionSettingContainer)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget_12)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font4)

        self.horizontalLayout_27.addWidget(self.label_37)

        self.horizontalSpacer_13 = QSpacerItem(305, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_13)

        self.label_38 = QLabel(self.widget_12)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(25, 25))
        self.label_38.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_38.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_38)

        self.scene_change_detection_method = QComboBox(self.widget_12)
        self.scene_change_detection_method.addItem("")
        self.scene_change_detection_method.addItem("")
        self.scene_change_detection_method.addItem("")
        self.scene_change_detection_method.addItem("")
        self.scene_change_detection_method.setObjectName(u"scene_change_detection_method")

        self.horizontalLayout_27.addWidget(self.scene_change_detection_method)


        self.verticalLayout_25.addWidget(self.widget_12)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.widget_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font4)

        self.horizontalLayout_14.addWidget(self.label_30)

        self.horizontalSpacer_6 = QSpacerItem(305, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.label_31 = QLabel(self.widget_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(25, 25))
        self.label_31.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_31.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_31)

        self.scene_change_detection_threshold = QDoubleSpinBox(self.widget_7)
        self.scene_change_detection_threshold.setObjectName(u"scene_change_detection_threshold")
        self.scene_change_detection_threshold.setMinimumSize(QSize(75, 30))
        self.scene_change_detection_threshold.setDecimals(1)
        self.scene_change_detection_threshold.setMinimum(1.000000000000000)
        self.scene_change_detection_threshold.setMaximum(10.000000000000000)

        self.horizontalLayout_14.addWidget(self.scene_change_detection_threshold)


        self.verticalLayout_25.addWidget(self.widget_7)

        self.widget_9 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.widget_9)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font4)

        self.horizontalLayout_25.addWidget(self.label_48)

        self.horizontalSpacer_10 = QSpacerItem(468, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)

        self.label_47 = QLabel(self.widget_9)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(25, 25))
        self.label_47.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_47.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.label_47)

        self.auto_border_cropping = QCheckBox(self.widget_9)
        self.auto_border_cropping.setObjectName(u"auto_border_cropping")

        self.horizontalLayout_25.addWidget(self.auto_border_cropping)


        self.verticalLayout_25.addWidget(self.widget_9)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_19.addWidget(self.scrollArea_3)


        self.verticalLayout_17.addWidget(self.VideoSettingsContainer)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_22 = QVBoxLayout(self.tab_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.renderSettingsContainer = QWidget(self.tab_3)
        self.renderSettingsContainer.setObjectName(u"renderSettingsContainer")
        self.verticalLayout_12 = QVBoxLayout(self.renderSettingsContainer)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.precisionSettingsContainer = QHBoxLayout()
        self.precisionSettingsContainer.setSpacing(10)
        self.precisionSettingsContainer.setObjectName(u"precisionSettingsContainer")
        self.label_3 = QLabel(self.renderSettingsContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)

        self.precisionSettingsContainer.addWidget(self.label_3)

        self.label_17 = QLabel(self.renderSettingsContainer)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(25, 25))
        self.label_17.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_17.setScaledContents(True)

        self.precisionSettingsContainer.addWidget(self.label_17)

        self.precision = QComboBox(self.renderSettingsContainer)
        self.precision.addItem("")
        self.precision.addItem("")
        self.precision.addItem("")
        self.precision.setObjectName(u"precision")

        self.precisionSettingsContainer.addWidget(self.precision)


        self.verticalLayout_12.addLayout(self.precisionSettingsContainer)

        self.tensorRTOptLevelSettingsContainer = QHBoxLayout()
        self.tensorRTOptLevelSettingsContainer.setSpacing(10)
        self.tensorRTOptLevelSettingsContainer.setObjectName(u"tensorRTOptLevelSettingsContainer")
        self.label_15 = QLabel(self.renderSettingsContainer)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.tensorRTOptLevelSettingsContainer.addWidget(self.label_15)

        self.label_21 = QLabel(self.renderSettingsContainer)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(25, 25))
        self.label_21.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_21.setScaledContents(True)

        self.tensorRTOptLevelSettingsContainer.addWidget(self.label_21)

        self.tensorrt_optimization_level = QComboBox(self.renderSettingsContainer)
        self.tensorrt_optimization_level.addItem("")
        self.tensorrt_optimization_level.addItem("")
        self.tensorrt_optimization_level.addItem("")
        self.tensorrt_optimization_level.addItem("")
        self.tensorrt_optimization_level.addItem("")
        self.tensorrt_optimization_level.setObjectName(u"tensorrt_optimization_level")

        self.tensorRTOptLevelSettingsContainer.addWidget(self.tensorrt_optimization_level)


        self.verticalLayout_12.addLayout(self.tensorRTOptLevelSettingsContainer)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setSpacing(10)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_88 = QLabel(self.renderSettingsContainer)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font4)

        self.horizontalLayout_67.addWidget(self.label_88)

        self.horizontalSpacer_34 = QSpacerItem(488, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_34)

        self.label_89 = QLabel(self.renderSettingsContainer)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMaximumSize(QSize(25, 25))
        self.label_89.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_89.setScaledContents(True)

        self.horizontalLayout_67.addWidget(self.label_89)

        self.auto_hdr_mode = QCheckBox(self.renderSettingsContainer)
        self.auto_hdr_mode.setObjectName(u"auto_hdr_mode")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.auto_hdr_mode.sizePolicy().hasHeightForWidth())
        self.auto_hdr_mode.setSizePolicy(sizePolicy12)

        self.horizontalLayout_67.addWidget(self.auto_hdr_mode)


        self.verticalLayout_12.addLayout(self.horizontalLayout_67)

        self.tensorRTOptLevelSettingsContainer_3 = QHBoxLayout()
        self.tensorRTOptLevelSettingsContainer_3.setSpacing(10)
        self.tensorRTOptLevelSettingsContainer_3.setObjectName(u"tensorRTOptLevelSettingsContainer_3")
        self.label_84 = QLabel(self.renderSettingsContainer)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font4)

        self.tensorRTOptLevelSettingsContainer_3.addWidget(self.label_84)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.tensorRTOptLevelSettingsContainer_3.addItem(self.horizontalSpacer_31)

        self.label_85 = QLabel(self.renderSettingsContainer)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMaximumSize(QSize(25, 25))
        self.label_85.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_85.setScaledContents(True)

        self.tensorRTOptLevelSettingsContainer_3.addWidget(self.label_85)

        self.dynamic_tensorrt_engine = QCheckBox(self.renderSettingsContainer)
        self.dynamic_tensorrt_engine.setObjectName(u"dynamic_tensorrt_engine")
        sizePolicy12.setHeightForWidth(self.dynamic_tensorrt_engine.sizePolicy().hasHeightForWidth())
        self.dynamic_tensorrt_engine.setSizePolicy(sizePolicy12)

        self.tensorRTOptLevelSettingsContainer_3.addWidget(self.dynamic_tensorrt_engine)


        self.verticalLayout_12.addLayout(self.tensorRTOptLevelSettingsContainer_3)

        self.precisionSettingsContainer_2 = QHBoxLayout()
        self.precisionSettingsContainer_2.setSpacing(10)
        self.precisionSettingsContainer_2.setObjectName(u"precisionSettingsContainer_2")
        self.label_22 = QLabel(self.renderSettingsContainer)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)

        self.precisionSettingsContainer_2.addWidget(self.label_22)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.precisionSettingsContainer_2.addItem(self.horizontalSpacer_15)

        self.label_35 = QLabel(self.renderSettingsContainer)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(25, 25))
        self.label_35.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_35.setScaledContents(True)

        self.precisionSettingsContainer_2.addWidget(self.label_35)

        self.uhd_mode = QCheckBox(self.renderSettingsContainer)
        self.uhd_mode.setObjectName(u"uhd_mode")

        self.precisionSettingsContainer_2.addWidget(self.uhd_mode)


        self.verticalLayout_12.addLayout(self.precisionSettingsContainer_2)

        self.precisionSettingsContainer_4 = QHBoxLayout()
        self.precisionSettingsContainer_4.setSpacing(10)
        self.precisionSettingsContainer_4.setObjectName(u"precisionSettingsContainer_4")
        self.label_45 = QLabel(self.renderSettingsContainer)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font4)

        self.precisionSettingsContainer_4.addWidget(self.label_45)

        self.label_46 = QLabel(self.renderSettingsContainer)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(25, 25))
        self.label_46.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_46.setScaledContents(True)

        self.precisionSettingsContainer_4.addWidget(self.label_46)

        self.ncnn_gpu_id = QSpinBox(self.renderSettingsContainer)
        self.ncnn_gpu_id.setObjectName(u"ncnn_gpu_id")
        self.ncnn_gpu_id.setMinimumSize(QSize(0, 0))

        self.precisionSettingsContainer_4.addWidget(self.ncnn_gpu_id)


        self.verticalLayout_12.addLayout(self.precisionSettingsContainer_4)

        self.precisionSettingsContainer_3 = QHBoxLayout()
        self.precisionSettingsContainer_3.setSpacing(10)
        self.precisionSettingsContainer_3.setObjectName(u"precisionSettingsContainer_3")
        self.label_43 = QLabel(self.renderSettingsContainer)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font4)

        self.precisionSettingsContainer_3.addWidget(self.label_43)

        self.label_44 = QLabel(self.renderSettingsContainer)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(25, 25))
        self.label_44.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_44.setScaledContents(True)

        self.precisionSettingsContainer_3.addWidget(self.label_44)

        self.pytorch_gpu_id = QSpinBox(self.renderSettingsContainer)
        self.pytorch_gpu_id.setObjectName(u"pytorch_gpu_id")
        self.pytorch_gpu_id.setMinimumSize(QSize(0, 0))

        self.precisionSettingsContainer_3.addWidget(self.pytorch_gpu_id)


        self.verticalLayout_12.addLayout(self.precisionSettingsContainer_3)


        self.verticalLayout_22.addWidget(self.renderSettingsContainer)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_23 = QVBoxLayout(self.tab_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.GUIOptionsContainer = QWidget(self.tab_4)
        self.GUIOptionsContainer.setObjectName(u"GUIOptionsContainer")
        self.verticalLayout_20 = QVBoxLayout(self.GUIOptionsContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, -1, -1, -1)
        self.previewEnabledContainer = QWidget(self.GUIOptionsContainer)
        self.previewEnabledContainer.setObjectName(u"previewEnabledContainer")
        self.horizontalLayout_21 = QHBoxLayout(self.previewEnabledContainer)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.previewEnabledContainer)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)

        self.horizontalLayout_21.addWidget(self.label_19)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_2)

        self.preview_enabled = QCheckBox(self.previewEnabledContainer)
        self.preview_enabled.setObjectName(u"preview_enabled")

        self.horizontalLayout_21.addWidget(self.preview_enabled)


        self.verticalLayout_20.addWidget(self.previewEnabledContainer)

        self.discordRPCSettingsContainer = QWidget(self.GUIOptionsContainer)
        self.discordRPCSettingsContainer.setObjectName(u"discordRPCSettingsContainer")
        self.horizontalLayout_12 = QHBoxLayout(self.discordRPCSettingsContainer)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.discordRPCSettingsContainer)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font4)

        self.horizontalLayout_12.addWidget(self.label_23)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.label_29 = QLabel(self.discordRPCSettingsContainer)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(25, 25))
        self.label_29.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_29.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_29)

        self.discord_rich_presence = QCheckBox(self.discordRPCSettingsContainer)
        self.discord_rich_presence.setObjectName(u"discord_rich_presence")

        self.horizontalLayout_12.addWidget(self.discord_rich_presence)


        self.verticalLayout_20.addWidget(self.discordRPCSettingsContainer)

        self.widget_29 = QWidget(self.GUIOptionsContainer)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_35 = QVBoxLayout(self.widget_29)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.openRVEFolderBtn = QPushButton(self.widget_29)
        self.openRVEFolderBtn.setObjectName(u"openRVEFolderBtn")
        self.openRVEFolderBtn.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.verticalLayout_35.addWidget(self.openRVEFolderBtn)


        self.verticalLayout_20.addWidget(self.widget_29)


        self.verticalLayout_23.addWidget(self.GUIOptionsContainer)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_18.addWidget(self.tabWidget)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)

        self.resetSettingsBtn = QPushButton(self.widget_4)
        self.resetSettingsBtn.setObjectName(u"resetSettingsBtn")

        self.horizontalLayout_20.addWidget(self.resetSettingsBtn)


        self.verticalLayout_18.addWidget(self.widget_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.settingsPage)
        self.downloadPage = QWidget()
        self.downloadPage.setObjectName(u"downloadPage")
        self.downloadPage.setStyleSheet(u"QWidget{\n"
"background-color:#16191d\n"
"\n"
"}\n"
"QScrollArea{\n"
"	background:transparent;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:#2c313c;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#2c313c;\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#676e7b;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#343b47;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color:#676e7b;\n"
"	color:gray;\n"
"}\n"
"QComboBox{\n"
"background-color:#2c313c;\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-radius: 10px;\n"
"color:white;\n"
"}\n"
"Line{\n"
"color:white;\n"
"background-color:white;\n"
"}\n"
"\n"
"")
        self.gridLayout_5 = QGridLayout(self.downloadPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_10 = QWidget(self.downloadPage)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 0))
        self.gridLayout_8 = QGridLayout(self.widget_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.encoderLabel_4 = QLabel(self.widget_10)
        self.encoderLabel_4.setObjectName(u"encoderLabel_4")
        self.encoderLabel_4.setFont(font4)

        self.gridLayout_8.addWidget(self.encoderLabel_4, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 0, 1, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.selectNCNNCustomModel = QPushButton(self.widget_10)
        self.selectNCNNCustomModel.setObjectName(u"selectNCNNCustomModel")
        self.selectNCNNCustomModel.setEnabled(True)

        self.gridLayout_10.addWidget(self.selectNCNNCustomModel, 1, 0, 1, 1)

        self.selectPytorchCustomModel = QPushButton(self.widget_10)
        self.selectPytorchCustomModel.setObjectName(u"selectPytorchCustomModel")
        self.selectPytorchCustomModel.setEnabled(True)

        self.gridLayout_10.addWidget(self.selectPytorchCustomModel, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.widget_10, 4, 0, 1, 1)

        self.ApplicationUpdateContainer = QWidget(self.downloadPage)
        self.ApplicationUpdateContainer.setObjectName(u"ApplicationUpdateContainer")
        self.verticalLayout_30 = QVBoxLayout(self.ApplicationUpdateContainer)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(9, 9, 9, 9)

        self.gridLayout_5.addWidget(self.ApplicationUpdateContainer, 0, 0, 1, 1)

        self.backendSelectContainer = QWidget(self.downloadPage)
        self.backendSelectContainer.setObjectName(u"backendSelectContainer")
        self.backendSelectContainer.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.backendSelectContainer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_31 = QWidget(self.backendSelectContainer)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.uninstallAppBtn = QPushButton(self.widget_31)
        self.uninstallAppBtn.setObjectName(u"uninstallAppBtn")
        sizePolicy5.setHeightForWidth(self.uninstallAppBtn.sizePolicy().hasHeightForWidth())
        self.uninstallAppBtn.setSizePolicy(sizePolicy5)
        self.uninstallAppBtn.setMaximumSize(QSize(50, 45))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.uninstallAppBtn.setIcon(icon6)
        self.uninstallAppBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_49.addWidget(self.uninstallAppBtn)

        self.label_67 = QLabel(self.widget_31)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_49.addWidget(self.label_67)


        self.verticalLayout_11.addWidget(self.widget_31)

        self.label_4 = QLabel(self.backendSelectContainer)
        self.label_4.setObjectName(u"label_4")
        font7 = QFont()
        font7.setPointSize(25)
        font7.setUnderline(True)
        self.label_4.setFont(font7)

        self.verticalLayout_11.addWidget(self.label_4)

        self.low_storage_label = QLabel(self.backendSelectContainer)
        self.low_storage_label.setObjectName(u"low_storage_label")
        font8 = QFont()
        font8.setBold(True)
        self.low_storage_label.setFont(font8)
        self.low_storage_label.setStyleSheet(u"QLabel {\n"
"color: red;\n"
"}")

        self.verticalLayout_11.addWidget(self.low_storage_label)

        self.scrollArea_2 = QScrollArea(self.backendSelectContainer)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy13)
        self.scrollArea_2.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 928, 302))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_64 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(25, 25))
        self.label_64.setToolTipDuration(0)
        self.label_64.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_64.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_64, 1, 1, 1, 1)

        self.label_65 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_9.addWidget(self.label_65, 1, 0, 1, 1)

        self.label_53 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_9.addWidget(self.label_53, 3, 0, 1, 1)

        self.pytorch_backend = QComboBox(self.scrollAreaWidgetContents_2)
        self.pytorch_backend.addItem("")
        self.pytorch_backend.addItem("")
        self.pytorch_backend.addItem("")
        self.pytorch_backend.setObjectName(u"pytorch_backend")

        self.gridLayout_9.addWidget(self.pytorch_backend, 3, 2, 1, 1)

        self.label_66 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(25, 25))
        self.label_66.setToolTipDuration(0)
        self.label_66.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_66.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_66, 3, 1, 1, 1)

        self.pytorch_version = QComboBox(self.scrollAreaWidgetContents_2)
        self.pytorch_version.setObjectName(u"pytorch_version")

        self.gridLayout_9.addWidget(self.pytorch_version, 1, 2, 1, 1)

        self.pytorchBackendInstallerContainer_5 = QWidget(self.scrollAreaWidgetContents_2)
        self.pytorchBackendInstallerContainer_5.setObjectName(u"pytorchBackendInstallerContainer_5")
        self.horizontalLayout_37 = QHBoxLayout(self.pytorchBackendInstallerContainer_5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.downloadRecommendedBtn = QPushButton(self.pytorchBackendInstallerContainer_5)
        self.downloadRecommendedBtn.setObjectName(u"downloadRecommendedBtn")
        sizePolicy5.setHeightForWidth(self.downloadRecommendedBtn.sizePolicy().hasHeightForWidth())
        self.downloadRecommendedBtn.setSizePolicy(sizePolicy5)
        self.downloadRecommendedBtn.setMaximumSize(QSize(50, 45))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.downloadRecommendedBtn.setIcon(icon7)
        self.downloadRecommendedBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_37.addWidget(self.downloadRecommendedBtn)

        self.label_25 = QLabel(self.pytorchBackendInstallerContainer_5)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_37.addWidget(self.label_25)


        self.gridLayout_9.addWidget(self.pytorchBackendInstallerContainer_5, 0, 0, 1, 1)


        self.horizontalLayout_46.addLayout(self.gridLayout_9)


        self.verticalLayout_13.addLayout(self.horizontalLayout_46)

        self.pytorchBackendInstallerContainer_4 = QWidget(self.scrollAreaWidgetContents_2)
        self.pytorchBackendInstallerContainer_4.setObjectName(u"pytorchBackendInstallerContainer_4")
        self.horizontalLayout_9 = QHBoxLayout(self.pytorchBackendInstallerContainer_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.downloadNCNNBtn = QPushButton(self.pytorchBackendInstallerContainer_4)
        self.downloadNCNNBtn.setObjectName(u"downloadNCNNBtn")
        sizePolicy5.setHeightForWidth(self.downloadNCNNBtn.sizePolicy().hasHeightForWidth())
        self.downloadNCNNBtn.setSizePolicy(sizePolicy5)
        self.downloadNCNNBtn.setMaximumSize(QSize(50, 45))
        self.downloadNCNNBtn.setIcon(icon7)
        self.downloadNCNNBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.downloadNCNNBtn)

        self.uninstallNCNNBtn = QPushButton(self.pytorchBackendInstallerContainer_4)
        self.uninstallNCNNBtn.setObjectName(u"uninstallNCNNBtn")
        sizePolicy5.setHeightForWidth(self.uninstallNCNNBtn.sizePolicy().hasHeightForWidth())
        self.uninstallNCNNBtn.setSizePolicy(sizePolicy5)
        self.uninstallNCNNBtn.setMaximumSize(QSize(50, 45))
        self.uninstallNCNNBtn.setIcon(icon6)
        self.uninstallNCNNBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.uninstallNCNNBtn)

        self.label_10 = QLabel(self.pytorchBackendInstallerContainer_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)


        self.verticalLayout_13.addWidget(self.pytorchBackendInstallerContainer_4)

        self.pytorchBackendInstallerContainer = QWidget(self.scrollAreaWidgetContents_2)
        self.pytorchBackendInstallerContainer.setObjectName(u"pytorchBackendInstallerContainer")
        self.horizontalLayout_6 = QHBoxLayout(self.pytorchBackendInstallerContainer)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.downloadTorchBtn = QPushButton(self.pytorchBackendInstallerContainer)
        self.downloadTorchBtn.setObjectName(u"downloadTorchBtn")
        sizePolicy5.setHeightForWidth(self.downloadTorchBtn.sizePolicy().hasHeightForWidth())
        self.downloadTorchBtn.setSizePolicy(sizePolicy5)
        self.downloadTorchBtn.setMaximumSize(QSize(50, 45))
        self.downloadTorchBtn.setIcon(icon7)
        self.downloadTorchBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.downloadTorchBtn)

        self.uninstallTorchBtn = QPushButton(self.pytorchBackendInstallerContainer)
        self.uninstallTorchBtn.setObjectName(u"uninstallTorchBtn")
        sizePolicy5.setHeightForWidth(self.uninstallTorchBtn.sizePolicy().hasHeightForWidth())
        self.uninstallTorchBtn.setSizePolicy(sizePolicy5)
        self.uninstallTorchBtn.setMaximumSize(QSize(50, 45))
        self.uninstallTorchBtn.setIcon(icon6)
        self.uninstallTorchBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.uninstallTorchBtn)

        self.label_6 = QLabel(self.pytorchBackendInstallerContainer)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.verticalLayout_13.addWidget(self.pytorchBackendInstallerContainer)

        self.pytorchBackendInstallerContainer_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.pytorchBackendInstallerContainer_2.setObjectName(u"pytorchBackendInstallerContainer_2")
        self.horizontalLayout_24 = QHBoxLayout(self.pytorchBackendInstallerContainer_2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.downloadTensorRTBtn = QPushButton(self.pytorchBackendInstallerContainer_2)
        self.downloadTensorRTBtn.setObjectName(u"downloadTensorRTBtn")
        sizePolicy5.setHeightForWidth(self.downloadTensorRTBtn.sizePolicy().hasHeightForWidth())
        self.downloadTensorRTBtn.setSizePolicy(sizePolicy5)
        self.downloadTensorRTBtn.setMaximumSize(QSize(50, 45))
        self.downloadTensorRTBtn.setIcon(icon7)
        self.downloadTensorRTBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.downloadTensorRTBtn)

        self.uninstallTensorRTBtn = QPushButton(self.pytorchBackendInstallerContainer_2)
        self.uninstallTensorRTBtn.setObjectName(u"uninstallTensorRTBtn")
        sizePolicy5.setHeightForWidth(self.uninstallTensorRTBtn.sizePolicy().hasHeightForWidth())
        self.uninstallTensorRTBtn.setSizePolicy(sizePolicy5)
        self.uninstallTensorRTBtn.setMaximumSize(QSize(50, 45))
        self.uninstallTensorRTBtn.setIcon(icon6)
        self.uninstallTensorRTBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.uninstallTensorRTBtn)

        self.label_8 = QLabel(self.pytorchBackendInstallerContainer_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_24.addWidget(self.label_8)


        self.verticalLayout_13.addWidget(self.pytorchBackendInstallerContainer_2)

        self.directMLBackendInstallerContainer = QWidget(self.scrollAreaWidgetContents_2)
        self.directMLBackendInstallerContainer.setObjectName(u"directMLBackendInstallerContainer")
        self.horizontalLayout_8 = QHBoxLayout(self.directMLBackendInstallerContainer)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.downloadDirectMLBtn = QPushButton(self.directMLBackendInstallerContainer)
        self.downloadDirectMLBtn.setObjectName(u"downloadDirectMLBtn")
        sizePolicy5.setHeightForWidth(self.downloadDirectMLBtn.sizePolicy().hasHeightForWidth())
        self.downloadDirectMLBtn.setSizePolicy(sizePolicy5)
        self.downloadDirectMLBtn.setMaximumSize(QSize(50, 45))
        self.downloadDirectMLBtn.setIcon(icon7)
        self.downloadDirectMLBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.downloadDirectMLBtn)

        self.uninstallDirectMLBtn = QPushButton(self.directMLBackendInstallerContainer)
        self.uninstallDirectMLBtn.setObjectName(u"uninstallDirectMLBtn")
        sizePolicy5.setHeightForWidth(self.uninstallDirectMLBtn.sizePolicy().hasHeightForWidth())
        self.uninstallDirectMLBtn.setSizePolicy(sizePolicy5)
        self.uninstallDirectMLBtn.setMaximumSize(QSize(50, 45))
        self.uninstallDirectMLBtn.setIcon(icon6)
        self.uninstallDirectMLBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.uninstallDirectMLBtn)

        self.label_28 = QLabel(self.directMLBackendInstallerContainer)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_8.addWidget(self.label_28)


        self.verticalLayout_13.addWidget(self.directMLBackendInstallerContainer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_11.addWidget(self.scrollArea_2)


        self.gridLayout_5.addWidget(self.backendSelectContainer, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.downloadPage)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.mainWindowContainer)


        self.gridLayout.addWidget(self.centralWidget, 0, 1, 1, 1)

        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_2 = QWidget(self.leftMenuSubContainer)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.homeBtn = QPushButton(self.verticalWidget_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(31, 0))
        self.homeBtn.setMaximumSize(QSize(55, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon8)
        self.homeBtn.setIconSize(QSize(35, 35))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setChecked(True)

        self.verticalLayout_6.addWidget(self.homeBtn)

        self.processBtn = QPushButton(self.verticalWidget_2)
        self.processBtn.setObjectName(u"processBtn")
        self.processBtn.setMaximumSize(QSize(55, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/cpu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.processBtn.setIcon(icon9)
        self.processBtn.setIconSize(QSize(35, 35))
        self.processBtn.setCheckable(True)

        self.verticalLayout_6.addWidget(self.processBtn)


        self.verticalLayout_3.addWidget(self.verticalWidget_2)

        self.verticalWidget = QWidget(self.leftMenuSubContainer)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_4 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 9, -1)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.settingsBtn = QPushButton(self.verticalWidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        sizePolicy12.setHeightForWidth(self.settingsBtn.sizePolicy().hasHeightForWidth())
        self.settingsBtn.setSizePolicy(sizePolicy12)
        self.settingsBtn.setMaximumSize(QSize(55, 16777215))
        self.settingsBtn.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.settingsBtn.setStyleSheet(u"text-align:left;\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon10)
        self.settingsBtn.setIconSize(QSize(35, 35))
        self.settingsBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.downloadBtn = QPushButton(self.verticalWidget)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setMaximumSize(QSize(55, 16777215))
        self.downloadBtn.setIcon(icon7)
        self.downloadBtn.setIconSize(QSize(35, 35))
        self.downloadBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.downloadBtn)


        self.verticalLayout_3.addWidget(self.verticalWidget)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.gridLayout.addWidget(self.leftMenuContainer, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.processSettingsContainer.setCurrentIndex(0)
        self.interpolateModelComboBox.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(0)
        self.tensorrt_optimization_level.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Support Me!", None))
#if QT_CONFIG(tooltip)
        self.kofiBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Support Me!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.kofiBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"\"Support Me!\"", None))
#endif // QT_CONFIG(statustip)
        self.kofiBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"GitHub Page", None))
        self.githubBtn.setText("")
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"REAL Video Enhancer", None))
        self.changeLogText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Adwaita Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell';\"><br /></p></body></html>", None))
        self.previewLabel.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Start Time (seconds)", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"End Time (seconds)", None))
        self.renderPreviewBtn.setText(QCoreApplication.translate("MainWindow", u"Render Preview", None))
#if QT_CONFIG(tooltip)
        self.label_63.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Render Preview:</span></p><p>     - Renders a small portion of the video to show the results (most useful for upscaling)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_63.setText("")
        self.ETA.setText(QCoreApplication.translate("MainWindow", u"ETA: ", None))
        self.FPS.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.STATUS.setText(QCoreApplication.translate("MainWindow", u"STATUS:", None))
        self.inputFileSelectButton.setText(QCoreApplication.translate("MainWindow", u"Select Input File", None))
        self.batchSelectButton.setText(QCoreApplication.translate("MainWindow", u"Batch Select", None))
        self.outputFileSelectButton.setText(QCoreApplication.translate("MainWindow", u"Select Output Folder", None))
        self.openOutputFolderButton.setText(QCoreApplication.translate("MainWindow", u"Open Output Folder", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Backend", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Interpolate", None))
        self.interpolateCheckBox.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Interpolate Model", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Interpolation Multiplier", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"SloMo Mode", None))
#if QT_CONFIG(tooltip)
        self.label_39.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Increase video length instead of framerate when interpolating.</p><p>Audio and Subtitles will not be transfered to output video.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_39.setText("")
        self.sloMoModeCheckBox.setText("")
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Decompress", None))
        self.decompressCheckBox.setText("")
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Decompress Model", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Denoise", None))
        self.denoiseCheckBox.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Denoise Model", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Deblur", None))
        self.deblurCheckBox.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Deblur Model", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Upscale", None))
        self.upscaleCheckBox.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Upscale Model", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Upscale Scale", None))
#if QT_CONFIG(tooltip)
        self.label_73.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Upscale Scale:</span></p><p><span style=\" font-weight:700;\">   - </span>Custom output scale no matter the model. Will run AI on video frame once, and scale the image to match the multiplier. Useful for 4x models.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_73.setText("")
        self.addToRenderQueueButton.setText(QCoreApplication.translate("MainWindow", u" Add to Render Queue", None))
        self.processSettingsContainer.setTabText(self.processSettingsContainer.indexOf(self.generalSettings), QCoreApplication.translate("MainWindow", u"General", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Encoder Settings", None))
#if QT_CONFIG(tooltip)
        self.label_75.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Encoder command:</span></p><p><span style=\" font-weight:700;\">     -</span> Encoder settings passed to FFMpeg, can be manually tweaked.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_75.setText("")
        self.encoderLabel.setText(QCoreApplication.translate("MainWindow", u"Video Encoder", None))
#if QT_CONFIG(tooltip)
        self.label_54.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Encoder:</span></p><p>- Compression algorithm for video, most common is libx264</p><p>- Any encoder without a device label is a CPU encoder.</p><p>- <span style=\" font-weight:700; text-decoration: underline;\">Lossy Encoders:</span></p><p>- libx264 (<span style=\" font-weight:700;\">mkv, mp4, mov, avi</span>)</p><p>- libx265 (<span style=\" font-weight:700;\">mkv, mp4, mov</span>)</p><p>- vp9 (<span style=\" font-weight:700;\">mkv, webm</span>)</p><p>- av1 (<span style=\" font-weight:700;\">mkv, mp4, webm</span>)</p><p>- <span style=\" font-weight:700; text-decoration: underline;\">Lossless Encoders:</span></p><p>- prores (<span style=\" font-weight:700;\">mkv, mov</span>)</p><p>- ffv1 (<span style=\" font-weight:700;\">mkv, avi</span>)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_54.setText("")
        self.encoder.setItemText(0, QCoreApplication.translate("MainWindow", u"libx264", None))
        self.encoder.setItemText(1, QCoreApplication.translate("MainWindow", u"libx265", None))
        self.encoder.setItemText(2, QCoreApplication.translate("MainWindow", u"vp9", None))
        self.encoder.setItemText(3, QCoreApplication.translate("MainWindow", u"av1", None))
        self.encoder.setItemText(4, QCoreApplication.translate("MainWindow", u"prores", None))
        self.encoder.setItemText(5, QCoreApplication.translate("MainWindow", u"ffv1", None))
        self.encoder.setItemText(6, QCoreApplication.translate("MainWindow", u"utvideo", None))
        self.encoder.setItemText(7, QCoreApplication.translate("MainWindow", u"x264_nvenc", None))
        self.encoder.setItemText(8, QCoreApplication.translate("MainWindow", u"x265_nvenc", None))
        self.encoder.setItemText(9, QCoreApplication.translate("MainWindow", u"av1_nvenc (40 series and up)", None))

        self.encoderLabel_2.setText(QCoreApplication.translate("MainWindow", u"Video Encoder Speed", None))
#if QT_CONFIG(tooltip)
        self.label_55.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Encoder Speed:</span></p><p> - Speed at which the encoder processes the video, <span style=\" font-weight:700; text-decoration: underline;\">Slower</span> processing time means <span style=\" font-weight:700; text-decoration: underline;\">Better results for the file size</span><span style=\" text-decoration: underline;\">.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_55.setText("")
        self.video_encoder_speed.setItemText(0, QCoreApplication.translate("MainWindow", u"fastest", None))
        self.video_encoder_speed.setItemText(1, QCoreApplication.translate("MainWindow", u"fast", None))
        self.video_encoder_speed.setItemText(2, QCoreApplication.translate("MainWindow", u"medium", None))
        self.video_encoder_speed.setItemText(3, QCoreApplication.translate("MainWindow", u"slow", None))
        self.video_encoder_speed.setItemText(4, QCoreApplication.translate("MainWindow", u"placebo", None))

        self.encoderLabel_5.setText(QCoreApplication.translate("MainWindow", u"Video Quality", None))
        self.video_quality.setItemText(0, QCoreApplication.translate("MainWindow", u"Lossless", None))
        self.video_quality.setItemText(1, QCoreApplication.translate("MainWindow", u"Ultra", None))
        self.video_quality.setItemText(2, QCoreApplication.translate("MainWindow", u"Very_High", None))
        self.video_quality.setItemText(3, QCoreApplication.translate("MainWindow", u"High", None))
        self.video_quality.setItemText(4, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.video_quality.setItemText(5, QCoreApplication.translate("MainWindow", u"Low", None))

        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Video Container", None))
#if QT_CONFIG(tooltip)
        self.label_50.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Video Container</span></p><p>- Changes the video container in the default output file generated container.</p><p>- <span style=\" font-weight:700;\">mkv </span>is <span style=\" font-weight:700;\">recomended</span> due to its extensive support for different formats.</p><p><span style=\" font-weight:700;\">WARNING: Changing this </span><span style=\" font-weight:700; text-decoration: underline;\">MAY</span><span style=\" font-weight:700;\"> break encoder compadibility. </span></p><p><span style=\" font-weight:700;\">Please look at the audio and video encoder tooltips for compadibility.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_50.setText("")
        self.video_container.setItemText(0, QCoreApplication.translate("MainWindow", u"mkv", None))
        self.video_container.setItemText(1, QCoreApplication.translate("MainWindow", u"mp4", None))
        self.video_container.setItemText(2, QCoreApplication.translate("MainWindow", u"mov", None))
        self.video_container.setItemText(3, QCoreApplication.translate("MainWindow", u"webm", None))
        self.video_container.setItemText(4, QCoreApplication.translate("MainWindow", u"avi", None))

        self.encoderLabel_7.setText(QCoreApplication.translate("MainWindow", u"Video Pixel Format", None))
#if QT_CONFIG(tooltip)
        self.label_58.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Pixel Format</span></p><p>- D<span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:9pt; color:#cccccc;\">efines how color information is stored for each pixel in a video frame.</span></p><p><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:9pt; color:#cccccc;\">- yuv420p: Most common, removes the most information. </span>(<span style=\" font-weight:700;\">mkv, mp4, mov, avi, webm</span>)</p><p><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:9pt; color:#cccccc;\">- yuv422p: In between 420p and 444p. </span>(<span style=\" font-weight:700;\">mkv, mov, mp4</span>)</p><p><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:9pt; color:#cccccc;\">- yuv444p: Keeps the most information. </span>(<span style=\" font-weight:700;\">mkv, mov, mp4</span>)<br/></p><p>- <span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:9pt; colo"
                        "r:#cccccc;\">yuv 420/422/444 p10le: 10 bit version of each. (MKV and MP4 containers only) </span>(<span style=\" font-weight:700;\">mkv, mov, mp4</span>)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_58.setText("")
        self.video_pixel_format.setItemText(0, QCoreApplication.translate("MainWindow", u"yuv420p", None))
        self.video_pixel_format.setItemText(1, QCoreApplication.translate("MainWindow", u"yuv422p", None))
        self.video_pixel_format.setItemText(2, QCoreApplication.translate("MainWindow", u"yuv444p", None))
        self.video_pixel_format.setItemText(3, QCoreApplication.translate("MainWindow", u"yuv420p (10 bit)", None))
        self.video_pixel_format.setItemText(4, QCoreApplication.translate("MainWindow", u"yuv422p (10 bit)", None))
        self.video_pixel_format.setItemText(5, QCoreApplication.translate("MainWindow", u"yuv444p (10 bit)", None))

        self.encoderLabel_10.setText(QCoreApplication.translate("MainWindow", u"Audio Encoder", None))
#if QT_CONFIG(tooltip)
        self.label_56.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Audio Encoder</span></p><p>- <span style=\" font-weight:700;\">Recommended </span>to use <span style=\" font-weight:700;\">aac</span> if the video container is <span style=\" font-weight:700;\">not mkv, </span>or if the output video has audio isses.</p><p><span style=\" font-weight:700;\">- </span>copy_audio: No re-encoding is done on the output</p><p>- aac: Most common, and high quality.</p><p>- libmp3lame: Used less, low quality.</p><p>- opus: Used for <span style=\" font-weight:700;\">webm</span>.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_56.setText("")
        self.audio_encoder.setItemText(0, QCoreApplication.translate("MainWindow", u"copy_audio", None))
        self.audio_encoder.setItemText(1, QCoreApplication.translate("MainWindow", u"aac", None))
        self.audio_encoder.setItemText(2, QCoreApplication.translate("MainWindow", u"libmp3lame", None))
        self.audio_encoder.setItemText(3, QCoreApplication.translate("MainWindow", u"opus", None))

        self.encoderLabel_6.setText(QCoreApplication.translate("MainWindow", u"Audio Bitrate", None))
#if QT_CONFIG(tooltip)
        self.label_57.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Audio Bitrate</span></p><p><span style=\" font-weight:700;\">- </span>Higher bitrate = higher quality</p><p>   - Only applies to <span style=\" font-weight:700;\">aac </span>and <span style=\" font-weight:700;\">libmp3lame</span>.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_57.setText("")
        self.audio_bitrate.setItemText(0, QCoreApplication.translate("MainWindow", u"320k", None))
        self.audio_bitrate.setItemText(1, QCoreApplication.translate("MainWindow", u"192k", None))
        self.audio_bitrate.setItemText(2, QCoreApplication.translate("MainWindow", u"128k", None))
        self.audio_bitrate.setItemText(3, QCoreApplication.translate("MainWindow", u"96k", None))

        self.encoderLabel_11.setText(QCoreApplication.translate("MainWindow", u"Subtiitle Encoder", None))
#if QT_CONFIG(tooltip)
        self.label_59.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Subtitle Encoder</span></p><p>- <span style=\" font-weight:700;\">Recommended </span>to use <span style=\" font-weight:700;\">webvtt</span> if the video container is <span style=\" font-weight:700;\">not mkv, </span>or if the output video has audio isses.</p><p><br/>All encoders here are <span style=\" font-weight:700;\">Text Only. </span>If you are enhancing a <span style=\" font-weight:700;\">DVD, </span>use <span style=\" font-weight:700;\">copy_subtitle</span>.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_59.setText("")
        self.subtitle_encoder.setItemText(0, QCoreApplication.translate("MainWindow", u"copy_subtitle", None))
        self.subtitle_encoder.setItemText(1, QCoreApplication.translate("MainWindow", u"ass", None))
        self.subtitle_encoder.setItemText(2, QCoreApplication.translate("MainWindow", u"srt", None))
        self.subtitle_encoder.setItemText(3, QCoreApplication.translate("MainWindow", u"webvtt", None))

        self.processSettingsContainer.setTabText(self.processSettingsContainer.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Encoder Options", None))
        self.RemoveFromRenderQueue.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.MoveUpRenderQueue.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.MoveDownRenderQueue.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Finished Output Files:", None))
        self.processSettingsContainer.setTabText(self.processSettingsContainer.indexOf(self.renderQueueTab), QCoreApplication.translate("MainWindow", u"Render Queue", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"General Settings", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_18.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Benchmark Mode", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Perform processing without outputing new video. This tests the raw performance of the inference.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText("")
        self.benchmarkModeCheckBox.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Upscale/Restoration Tile Settings", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Tiling", None))
#if QT_CONFIG(tooltip)
        self.label_34.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Split up processing upscaled frames into chunks.</p><p>Lowers VRAM usage, but also slows down render. </p><p>Only use when render failes due to VRAM limits.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText("")
        self.tilingCheckBox.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Tile Size", None))
        self.tileSizeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"512", None))
        self.tileSizeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"384", None))
        self.tileSizeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"256", None))
        self.tileSizeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"128", None))
        self.tileSizeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"64", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Interpolate Settings", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Dynamic Scaled Flow (Pytorch Only)", None))
#if QT_CONFIG(tooltip)
        self.label_71.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Scales optical flow based on the difference between frames.</p><p>Helps with anime interpolation.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_71.setText("")
        self.dynamicScaledOpticalFlowCheckBox.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Ensemble (Pytorch/TensorRT Only)", None))
#if QT_CONFIG(tooltip)
        self.label_69.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ensembles flow, can produce better results.</p><p>Only compadible with older RIFE models and GMFSS</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_69.setText("")
        self.ensembleCheckBox.setText("")
        self.processSettingsContainer.setTabText(self.processSettingsContainer.indexOf(self.advancedSettings), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.renderOutput.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Adwaita Sans'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p></body></html>", None))
        self.processSettingsContainer.setTabText(self.processSettingsContainer.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Logs", None))
        self.startRenderButton.setText("")
        self.pauseRenderButton.setText("")
        self.killRenderButton.setText("")
        self.encoderLabel_3.setText(QCoreApplication.translate("MainWindow", u"Output folder directory", None))
        self.select_output_folder_location_btn.setText(QCoreApplication.translate("MainWindow", u"Select Output Folder", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Scene Change Detection Enabled", None))
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Scene Change Detection Enabled:</span></p><p>- Enabled: Attempts to detect when scenes change in a video. </p><p>   When running an interpolation, it will avoide interpolating over these scene changes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText("")
        self.scene_change_detection_enabled.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Scene Change Detection Method", None))
#if QT_CONFIG(tooltip)
        self.label_38.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Scene Change Detection Method</span></p><p>- mean: fastest, least accurate</p><p>- mean (segmented): fast, prone to overdetection</p><p>- pyscenedetect: slow, accuate <span style=\" font-weight:700;\">(Recommended)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_38.setText("")
        self.scene_change_detection_method.setItemText(0, QCoreApplication.translate("MainWindow", u"mean", None))
        self.scene_change_detection_method.setItemText(1, QCoreApplication.translate("MainWindow", u"mean_segmented", None))
        self.scene_change_detection_method.setItemText(2, QCoreApplication.translate("MainWindow", u"sudo_scene_detect", None))
        self.scene_change_detection_method.setItemText(3, QCoreApplication.translate("MainWindow", u"pyscenedetect", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Scene Change Detection Threshold", None))
#if QT_CONFIG(tooltip)
        self.label_31.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Scene Change Detection Threshold</span></p><p> - Lower number: <span style=\" font-weight:700;\">higher</span> chance of detecting scene changes, with risk of <span style=\" font-weight:700;\">overdetection</span>.</p><p> - Higher number: <span style=\" font-weight:700;\">lower </span>chance of detecting scene changes, with risk of <span style=\" font-weight:700;\">underdetection.</span></p><p>   - <span style=\" font-weight:700;\">Recommended: </span>2-3 for real life, 4 for animation.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_31.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Auto Border Cropping", None))
#if QT_CONFIG(tooltip)
        self.label_47.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Audo Border Cropping:</span></p><p>- Will automatically remove black bars if they are present throughout a video, can increase performance.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_47.setText("")
        self.auto_border_cropping.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Output Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Precision", None))
#if QT_CONFIG(tooltip)
        self.label_17.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Precision:</p><p> - Auto: Defaults to float16 if the GPU is supported (RTX 20 series and up)</p><p> - Float16: Faster inference and less VRAM usage.</p><p> - Float32: Slower inference and more VRAM usage, supported on more GPUS.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText("")
        self.precision.setItemText(0, QCoreApplication.translate("MainWindow", u"auto", None))
        self.precision.setItemText(1, QCoreApplication.translate("MainWindow", u"float16", None))
        self.precision.setItemText(2, QCoreApplication.translate("MainWindow", u"float32", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TensorRT Optimization Level", None))
#if QT_CONFIG(tooltip)
        self.label_21.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TensorRT Optimization Level:</p><p>- Lower means less optimization, but faster engine generation time.</p><p>- Higher means more optimization, but slower engine generation time.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText("")
        self.tensorrt_optimization_level.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.tensorrt_optimization_level.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.tensorrt_optimization_level.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.tensorrt_optimization_level.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.tensorrt_optimization_level.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Auto HDR Mode", None))
#if QT_CONFIG(tooltip)
        self.label_89.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Auto HDR Mode</p><p>- Auto enables HDR mode if RVE detects that the video that is being rendered is HDR. <span style=\" font-weight:700;\">This will cause slower rendering if the video is HDR.</span></p><p><span style=\" font-weight:700;\"> - </span><span style=\" font-weight:700;\">HDR is only color tested on x264 and x265 encoders.</span></p><p><span style=\" ont-weight:700\"> - The preview colors may be distorted as the preview itself is not HDR.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_89.setText("")
        self.auto_hdr_mode.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"TensorRT Dynamic Engine", None))
#if QT_CONFIG(tooltip)
        self.label_85.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TensorRT Dynamic Engine:</p><p>- Enables TensorRT to build for many different resolutions in one engine.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_85.setText("")
        self.dynamic_tensorrt_engine.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Interpolation UHD Mode", None))
#if QT_CONFIG(tooltip)
        self.label_35.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Saves VRAM and speeds up inference at resolutions above 1080p by calculating flow at a lower resolution. (GMFSS/GIMM)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText("")
        self.uhd_mode.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"NCNN GPU ID", None))
#if QT_CONFIG(tooltip)
        self.label_46.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>NCNN GPU ID -</p><p>Sets what GPU is used for NCNN</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_46.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"PyTorch GPU ID", None))
#if QT_CONFIG(tooltip)
        self.label_44.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PyTorch GPU ID -</p><p>Sets what GPU is used for PyTorch</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_44.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Render Settings", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Preview Enabled", None))
        self.preview_enabled.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Discord Rich Presence", None))
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Show REAL Video Enhancer in discord.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText("")
        self.discord_rich_presence.setText("")
        self.openRVEFolderBtn.setText(QCoreApplication.translate("MainWindow", u"Open RVE Folder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"RVE Settings", None))
        self.resetSettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Reset Settings", None))
        self.encoderLabel_4.setText(QCoreApplication.translate("MainWindow", u"Import Custom Upscale Model", None))
        self.selectNCNNCustomModel.setText(QCoreApplication.translate("MainWindow", u"Select Model (NCNN/.bin+.param)", None))
        self.selectPytorchCustomModel.setText(QCoreApplication.translate("MainWindow", u"Select Model (PyTorch/TensorRT/.pth)", None))
        self.uninstallAppBtn.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Uninstall App", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Backends", None))
        self.low_storage_label.setText(QCoreApplication.translate("MainWindow", u"Your PC does not have enough storage for PyTorch/TensorRT. Please free up at least 15gb.", None))
#if QT_CONFIG(tooltip)
        self.label_64.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">PyTorch Version</span></p><p>- This is the version downloaded</p><p>- 2.6: Supports older CUDA enabled GPUs</p><p>- 2.8: Supports all RTX cards, faster and recomended.</p><p>- 2.9: Experimental.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_64.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"PyTorch Version", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"PyTorch Backend", None))
        self.pytorch_backend.setItemText(0, QCoreApplication.translate("MainWindow", u"CUDA", None))
        self.pytorch_backend.setItemText(1, QCoreApplication.translate("MainWindow", u"ROCm", None))
        self.pytorch_backend.setItemText(2, QCoreApplication.translate("MainWindow", u"xpu", None))

#if QT_CONFIG(tooltip)
        self.label_66.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">PyTorch Backend</span></p><p>- CUDA: NVIDIA GPUs 10 series and up</p><p>- ROCm: AMD (Linux Only) 7000 series(maybe) and up</p><p>- xpu: Intel: idk fam, dunno if this even works lowkey</p><p>- MPS: Apple Mac M series SOCs only.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_66.setText("")
        self.downloadRecommendedBtn.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Install Recommended Dependencies", None))
        self.downloadNCNNBtn.setText("")
        self.uninstallNCNNBtn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"NCNN Vulkan (All GPUs, slower inference, small download)", None))
        self.downloadTorchBtn.setText("")
        self.uninstallTorchBtn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PyTorch (NVIDIA/CUDA, AMD/ROCm (Linux Only), INTEL/xpu, MacOS/MPS)", None))
        self.downloadTensorRTBtn.setText("")
        self.uninstallTensorRTBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TensorRT (Nvidia RTX 20 series and up, fastest inference, largest download)", None))
        self.downloadDirectMLBtn.setText("")
        self.uninstallDirectMLBtn.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"DirectML - NOT IMPLEMENTED YET (All DirectX12 capable GPUs, faster inference, small download, Windows only)", None))
        self.homeBtn.setText("")
        self.processBtn.setText("")
        self.settingsBtn.setText("")
        self.downloadBtn.setText("")
    # retranslateUi

