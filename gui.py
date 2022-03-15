# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 802, 452))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.panel = QtWidgets.QWidget()
        self.panel.setObjectName("panel")
        self.Panel_controls = QtWidgets.QGroupBox(self.panel)
        self.Panel_controls.setGeometry(QtCore.QRect(4, 300, 221, 101))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_controls.setFont(font)
        self.Panel_controls.setObjectName("Panel_controls")
        self.Panel_start = QtWidgets.QPushButton(self.Panel_controls)
        self.Panel_start.setGeometry(QtCore.QRect(5, 25, 100, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_start.setFont(font)
        self.Panel_start.setObjectName("Panel_start")
        self.Panel_stop = QtWidgets.QPushButton(self.Panel_controls)
        self.Panel_stop.setEnabled(False)
        self.Panel_stop.setGeometry(QtCore.QRect(115, 25, 100, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_stop.setFont(font)
        self.Panel_stop.setObjectName("Panel_stop")
        self.Panel_forcestop = QtWidgets.QPushButton(self.Panel_controls)
        self.Panel_forcestop.setEnabled(False)
        self.Panel_forcestop.setGeometry(QtCore.QRect(115, 60, 100, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_forcestop.setFont(font)
        self.Panel_forcestop.setObjectName("Panel_forcestop")
        self.Panel_restart = QtWidgets.QPushButton(self.Panel_controls)
        self.Panel_restart.setEnabled(False)
        self.Panel_restart.setGeometry(QtCore.QRect(5, 60, 100, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_restart.setFont(font)
        self.Panel_restart.setObjectName("Panel_restart")
        self.Panel_consolegroup = QtWidgets.QGroupBox(self.panel)
        self.Panel_consolegroup.setGeometry(QtCore.QRect(230, 10, 561, 391))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_consolegroup.setFont(font)
        self.Panel_consolegroup.setObjectName("Panel_consolegroup")
        self.Panel_input = QtWidgets.QLineEdit(self.Panel_consolegroup)
        self.Panel_input.setGeometry(QtCore.QRect(10, 360, 541, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_input.setFont(font)
        self.Panel_input.setObjectName("Panel_input")
        self.Panel_console = QtWebEngineWidgets.QWebEngineView(self.Panel_consolegroup)
        self.Panel_console.setGeometry(QtCore.QRect(9, 29, 541, 321))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_console.setFont(font)
        self.Panel_console.setObjectName("Panel_console")
        self.Panel_info = QtWidgets.QGroupBox(self.panel)
        self.Panel_info.setGeometry(QtCore.QRect(9, 9, 211, 271))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_info.setFont(font)
        self.Panel_info.setObjectName("Panel_info")
        self.Panel_state = QtWidgets.QLabel(self.Panel_info)
        self.Panel_state.setGeometry(QtCore.QRect(11, 20, 60, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_state.setFont(font)
        self.Panel_state.setScaledContents(False)
        self.Panel_state.setWordWrap(False)
        self.Panel_state.setObjectName("Panel_state")
        self.Panel_version = QtWidgets.QLabel(self.Panel_info)
        self.Panel_version.setGeometry(QtCore.QRect(11, 50, 60, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_version.setFont(font)
        self.Panel_version.setScaledContents(False)
        self.Panel_version.setWordWrap(False)
        self.Panel_version.setObjectName("Panel_version")
        self.Panel_gamemode = QtWidgets.QLabel(self.Panel_info)
        self.Panel_gamemode.setGeometry(QtCore.QRect(11, 80, 60, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_gamemode.setFont(font)
        self.Panel_gamemode.setScaledContents(False)
        self.Panel_gamemode.setWordWrap(False)
        self.Panel_gamemode.setObjectName("Panel_gamemode")
        self.Panel_difficulty = QtWidgets.QLabel(self.Panel_info)
        self.Panel_difficulty.setGeometry(QtCore.QRect(12, 110, 60, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_difficulty.setFont(font)
        self.Panel_difficulty.setScaledContents(False)
        self.Panel_difficulty.setWordWrap(False)
        self.Panel_difficulty.setObjectName("Panel_difficulty")
        self.Panel_levelname = QtWidgets.QLabel(self.Panel_info)
        self.Panel_levelname.setGeometry(QtCore.QRect(12, 140, 60, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_levelname.setFont(font)
        self.Panel_levelname.setScaledContents(False)
        self.Panel_levelname.setWordWrap(False)
        self.Panel_levelname.setObjectName("Panel_levelname")
        self.Panel_port = QtWidgets.QLabel(self.Panel_info)
        self.Panel_port.setGeometry(QtCore.QRect(12, 170, 60, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_port.setFont(font)
        self.Panel_port.setScaledContents(False)
        self.Panel_port.setWordWrap(False)
        self.Panel_port.setObjectName("Panel_port")
        self.Panel_port_2 = QtWidgets.QLabel(self.Panel_info)
        self.Panel_port_2.setGeometry(QtCore.QRect(70, 170, 125, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_port_2.setFont(font)
        self.Panel_port_2.setScaledContents(False)
        self.Panel_port_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Panel_port_2.setWordWrap(False)
        self.Panel_port_2.setObjectName("Panel_port_2")
        self.Panel_gamemode_2 = QtWidgets.QLabel(self.Panel_info)
        self.Panel_gamemode_2.setGeometry(QtCore.QRect(70, 80, 125, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_gamemode_2.setFont(font)
        self.Panel_gamemode_2.setScaledContents(False)
        self.Panel_gamemode_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Panel_gamemode_2.setWordWrap(False)
        self.Panel_gamemode_2.setObjectName("Panel_gamemode_2")
        self.Panel_difficulty_2 = QtWidgets.QLabel(self.Panel_info)
        self.Panel_difficulty_2.setGeometry(QtCore.QRect(70, 110, 125, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_difficulty_2.setFont(font)
        self.Panel_difficulty_2.setScaledContents(False)
        self.Panel_difficulty_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Panel_difficulty_2.setWordWrap(False)
        self.Panel_difficulty_2.setObjectName("Panel_difficulty_2")
        self.Panel_version_2 = QtWidgets.QLabel(self.Panel_info)
        self.Panel_version_2.setGeometry(QtCore.QRect(70, 50, 125, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_version_2.setFont(font)
        self.Panel_version_2.setScaledContents(False)
        self.Panel_version_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Panel_version_2.setWordWrap(False)
        self.Panel_version_2.setObjectName("Panel_version_2")
        self.Panel_state_2 = QtWidgets.QLabel(self.Panel_info)
        self.Panel_state_2.setGeometry(QtCore.QRect(70, 20, 125, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_state_2.setFont(font)
        self.Panel_state_2.setScaledContents(False)
        self.Panel_state_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Panel_state_2.setObjectName("Panel_state_2")
        self.Panel_levelname_2 = QtWidgets.QLabel(self.Panel_info)
        self.Panel_levelname_2.setGeometry(QtCore.QRect(70, 140, 125, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_levelname_2.setFont(font)
        self.Panel_levelname_2.setScaledContents(False)
        self.Panel_levelname_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Panel_levelname_2.setWordWrap(False)
        self.Panel_levelname_2.setObjectName("Panel_levelname_2")
        self.Panel_cpu = QtWidgets.QLabel(self.Panel_info)
        self.Panel_cpu.setGeometry(QtCore.QRect(12, 200, 71, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_cpu.setFont(font)
        self.Panel_cpu.setScaledContents(False)
        self.Panel_cpu.setWordWrap(False)
        self.Panel_cpu.setObjectName("Panel_cpu")
        self.Panel_cpu_2 = QtWidgets.QLabel(self.Panel_info)
        self.Panel_cpu_2.setGeometry(QtCore.QRect(70, 200, 125, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_cpu_2.setFont(font)
        self.Panel_cpu_2.setScaledContents(False)
        self.Panel_cpu_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Panel_cpu_2.setWordWrap(False)
        self.Panel_cpu_2.setObjectName("Panel_cpu_2")
        self.Panel_ram_2 = QtWidgets.QLabel(self.Panel_info)
        self.Panel_ram_2.setGeometry(QtCore.QRect(70, 230, 125, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_ram_2.setFont(font)
        self.Panel_ram_2.setScaledContents(False)
        self.Panel_ram_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Panel_ram_2.setWordWrap(False)
        self.Panel_ram_2.setObjectName("Panel_ram_2")
        self.Panel_ram = QtWidgets.QLabel(self.Panel_info)
        self.Panel_ram.setGeometry(QtCore.QRect(12, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Panel_ram.setFont(font)
        self.Panel_ram.setScaledContents(False)
        self.Panel_ram.setWordWrap(False)
        self.Panel_ram.setObjectName("Panel_ram")
        self.tabWidget.addTab(self.panel, "")
        self.regular = QtWidgets.QWidget()
        self.regular.setObjectName("regular")
        self.regularlist = QtWidgets.QTableWidget(self.regular)
        self.regularlist.setGeometry(QtCore.QRect(10, 10, 771, 381))
        self.regularlist.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.regularlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.regularlist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.regularlist.setObjectName("regularlist")
        self.regularlist.setColumnCount(4)
        self.regularlist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.regularlist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.regularlist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.regularlist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.regularlist.setHorizontalHeaderItem(3, item)
        self.regularlist.horizontalHeader().setStretchLastSection(True)
        self.regularlist.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.regular, "")
        self.plugins = QtWidgets.QWidget()
        self.plugins.setObjectName("plugins")
        self.pluginList = QtWidgets.QListWidget(self.plugins)
        self.pluginList.setGeometry(QtCore.QRect(10, 10, 771, 381))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pluginList.setFont(font)
        self.pluginList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pluginList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pluginList.setObjectName("pluginList")
        self.plugins_total = QtWidgets.QLabel(self.plugins)
        self.plugins_total.setGeometry(QtCore.QRect(10, 400, 591, 16))
        self.plugins_total.setObjectName("plugins_total")
        self.tabWidget.addTab(self.plugins, "")
        self.Bot = QtWidgets.QWidget()
        self.Bot.setObjectName("Bot")
        self.Bot_console = QtWebEngineWidgets.QWebEngineView(self.Bot)
        self.Bot_console.setGeometry(QtCore.QRect(180, 16, 601, 384))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Bot_console.setFont(font)
        self.Bot_console.setObjectName("Bot_console")
        self.Bot_control = QtWidgets.QGroupBox(self.Bot)
        self.Bot_control.setGeometry(QtCore.QRect(10, 240, 151, 161))
        self.Bot_control.setObjectName("Bot_control")
        self.Bot_stop = QtWidgets.QPushButton(self.Bot_control)
        self.Bot_stop.setGeometry(QtCore.QRect(20, 100, 111, 31))
        self.Bot_stop.setObjectName("Bot_stop")
        self.Bot_start = QtWidgets.QPushButton(self.Bot_control)
        self.Bot_start.setGeometry(QtCore.QRect(20, 40, 111, 31))
        self.Bot_start.setObjectName("Bot_start")
        self.Bot_info = QtWidgets.QGroupBox(self.Bot)
        self.Bot_info.setGeometry(QtCore.QRect(9, 10, 151, 191))
        self.Bot_info.setObjectName("Bot_info")
        self.Bot_state = QtWidgets.QLabel(self.Bot_info)
        self.Bot_state.setGeometry(QtCore.QRect(10, 30, 41, 16))
        self.Bot_state.setObjectName("Bot_state")
        self.Bot_qq = QtWidgets.QLabel(self.Bot_info)
        self.Bot_qq.setGeometry(QtCore.QRect(10, 60, 41, 16))
        self.Bot_qq.setObjectName("Bot_qq")
        self.Bot_receive = QtWidgets.QLabel(self.Bot_info)
        self.Bot_receive.setGeometry(QtCore.QRect(10, 120, 61, 21))
        self.Bot_receive.setObjectName("Bot_receive")
        self.Bot_send = QtWidgets.QLabel(self.Bot_info)
        self.Bot_send.setGeometry(QtCore.QRect(10, 150, 51, 21))
        self.Bot_send.setObjectName("Bot_send")
        self.line = QtWidgets.QFrame(self.Bot_info)
        self.line.setGeometry(QtCore.QRect(10, 90, 131, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Bot_receive_2 = QtWidgets.QLabel(self.Bot_info)
        self.Bot_receive_2.setGeometry(QtCore.QRect(59, 120, 71, 20))
        self.Bot_receive_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Bot_receive_2.setObjectName("Bot_receive_2")
        self.Bot_send_2 = QtWidgets.QLabel(self.Bot_info)
        self.Bot_send_2.setGeometry(QtCore.QRect(59, 150, 71, 20))
        self.Bot_send_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Bot_send_2.setObjectName("Bot_send_2")
        self.Bot_qq_2 = QtWidgets.QLabel(self.Bot_info)
        self.Bot_qq_2.setGeometry(QtCore.QRect(39, 60, 91, 20))
        self.Bot_qq_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Bot_qq_2.setObjectName("Bot_qq_2")
        self.Bot_state_2 = QtWidgets.QLabel(self.Bot_info)
        self.Bot_state_2.setGeometry(QtCore.QRect(49, 30, 81, 20))
        self.Bot_state_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Bot_state_2.setObjectName("Bot_state_2")
        self.tabWidget.addTab(self.Bot, "")
        self.setting = QtWidgets.QWidget()
        self.setting.setObjectName("setting")
        self.setting_scrollArea = QtWidgets.QScrollArea(self.setting)
        self.setting_scrollArea.setEnabled(True)
        self.setting_scrollArea.setGeometry(QtCore.QRect(0, 0, 797, 448))
        self.setting_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setting_scrollArea.setWidgetResizable(False)
        self.setting_scrollArea.setObjectName("setting_scrollArea")
        self.setting_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.setting_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -269, 800, 700))
        self.setting_scrollAreaWidgetContents.setObjectName("setting_scrollAreaWidgetContents")
        self.setting_start = QtWidgets.QGroupBox(self.setting_scrollAreaWidgetContents)
        self.setting_start.setGeometry(QtCore.QRect(10, 10, 761, 101))
        self.setting_start.setObjectName("setting_start")
        self.setting_file = QtWidgets.QLabel(self.setting_start)
        self.setting_file.setGeometry(QtCore.QRect(20, 20, 71, 16))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.setting_file.setFont(font)
        self.setting_file.setObjectName("setting_file")
        self.setting_filepath = QtWidgets.QLineEdit(self.setting_start)
        self.setting_filepath.setGeometry(QtCore.QRect(20, 40, 641, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.setting_filepath.setFont(font)
        self.setting_filepath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setting_filepath.setReadOnly(True)
        self.setting_filepath.setObjectName("setting_filepath")
        self.setting_selectfile = QtWidgets.QPushButton(self.setting_start)
        self.setting_selectfile.setGeometry(QtCore.QRect(670, 39, 81, 23))
        self.setting_selectfile.setObjectName("setting_selectfile")
        self.setting_autoRestart = QtWidgets.QCheckBox(self.setting_start)
        self.setting_autoRestart.setGeometry(QtCore.QRect(20, 70, 161, 16))
        self.setting_autoRestart.setObjectName("setting_autoRestart")
        self.setting_bot = QtWidgets.QGroupBox(self.setting_scrollAreaWidgetContents)
        self.setting_bot.setGeometry(QtCore.QRect(10, 220, 761, 131))
        self.setting_bot.setObjectName("setting_bot")
        self.setting_port1 = QtWidgets.QLabel(self.setting_bot)
        self.setting_port1.setGeometry(QtCore.QRect(20, 30, 51, 21))
        self.setting_port1.setObjectName("setting_port1")
        self.setting_port2 = QtWidgets.QLabel(self.setting_bot)
        self.setting_port2.setGeometry(QtCore.QRect(20, 60, 51, 21))
        self.setting_port2.setObjectName("setting_port2")
        self.setting_sendPort = QtWidgets.QSpinBox(self.setting_bot)
        self.setting_sendPort.setGeometry(QtCore.QRect(80, 30, 71, 22))
        self.setting_sendPort.setMinimum(1)
        self.setting_sendPort.setMaximum(65535)
        self.setting_sendPort.setProperty("value", 5700)
        self.setting_sendPort.setObjectName("setting_sendPort")
        self.setting_listenPort = QtWidgets.QSpinBox(self.setting_bot)
        self.setting_listenPort.setGeometry(QtCore.QRect(80, 60, 71, 22))
        self.setting_listenPort.setMinimum(1)
        self.setting_listenPort.setMaximum(65535)
        self.setting_listenPort.setProperty("value", 8080)
        self.setting_listenPort.setObjectName("setting_listenPort")
        self.setting_botFilepath = QtWidgets.QLineEdit(self.setting_bot)
        self.setting_botFilepath.setGeometry(QtCore.QRect(190, 50, 471, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.setting_botFilepath.setFont(font)
        self.setting_botFilepath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setting_botFilepath.setText("")
        self.setting_botFilepath.setReadOnly(True)
        self.setting_botFilepath.setObjectName("setting_botFilepath")
        self.setting_botSelectfile = QtWidgets.QPushButton(self.setting_bot)
        self.setting_botSelectfile.setGeometry(QtCore.QRect(670, 50, 81, 23))
        self.setting_botSelectfile.setObjectName("setting_botSelectfile")
        self.setting_botFile = QtWidgets.QLabel(self.setting_bot)
        self.setting_botFile.setGeometry(QtCore.QRect(190, 30, 71, 16))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.setting_botFile.setFont(font)
        self.setting_botFile.setObjectName("setting_botFile")
        self.setting_savePort = QtWidgets.QPushButton(self.setting_bot)
        self.setting_savePort.setGeometry(QtCore.QRect(20, 90, 131, 23))
        self.setting_savePort.setObjectName("setting_savePort")
        self.setting_logout = QtWidgets.QPushButton(self.setting_bot)
        self.setting_logout.setGeometry(QtCore.QRect(190, 90, 121, 23))
        self.setting_logout.setObjectName("setting_logout")
        self.setting_enableOutputMsgToLog = QtWidgets.QCheckBox(self.setting_bot)
        self.setting_enableOutputMsgToLog.setGeometry(QtCore.QRect(340, 90, 201, 21))
        self.setting_enableOutputMsgToLog.setObjectName("setting_enableOutputMsgToLog")
        self.line_2 = QtWidgets.QFrame(self.setting_bot)
        self.line_2.setGeometry(QtCore.QRect(153, 30, 31, 81))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.setting_console = QtWidgets.QGroupBox(self.setting_scrollAreaWidgetContents)
        self.setting_console.setGeometry(QtCore.QRect(10, 120, 761, 91))
        self.setting_console.setObjectName("setting_console")
        self.setting_color_style = QtWidgets.QLabel(self.setting_console)
        self.setting_color_style.setGeometry(QtCore.QRect(20, 30, 141, 16))
        self.setting_color_style.setObjectName("setting_color_style")
        self.setting_colorfulLogOut = QtWidgets.QComboBox(self.setting_console)
        self.setting_colorfulLogOut.setGeometry(QtCore.QRect(20, 50, 131, 22))
        self.setting_colorfulLogOut.setObjectName("setting_colorfulLogOut")
        self.setting_colorfulLogOut.addItem("")
        self.setting_colorfulLogOut.addItem("")
        self.setting_colorfulLogOut.addItem("")
        self.setting_enableOutputToLog = QtWidgets.QCheckBox(self.setting_console)
        self.setting_enableOutputToLog.setGeometry(QtCore.QRect(220, 30, 161, 16))
        self.setting_enableOutputToLog.setObjectName("setting_enableOutputToLog")
        self.setting_outputCommandToConsole = QtWidgets.QCheckBox(self.setting_console)
        self.setting_outputCommandToConsole.setGeometry(QtCore.QRect(220, 50, 201, 16))
        self.setting_outputCommandToConsole.setObjectName("setting_outputCommandToConsole")
        self.setting_msg = QtWidgets.QGroupBox(self.setting_scrollAreaWidgetContents)
        self.setting_msg.setGeometry(QtCore.QRect(10, 360, 761, 171))
        self.setting_msg.setObjectName("setting_msg")
        self.setting_groupList = QtWidgets.QPlainTextEdit(self.setting_msg)
        self.setting_groupList.setGeometry(QtCore.QRect(20, 50, 211, 101))
        self.setting_groupList.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.setting_groupList.setObjectName("setting_groupList")
        self.setting_listenGroup = QtWidgets.QLabel(self.setting_msg)
        self.setting_listenGroup.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.setting_listenGroup.setObjectName("setting_listenGroup")
        self.setting_permissionList = QtWidgets.QPlainTextEdit(self.setting_msg)
        self.setting_permissionList.setGeometry(QtCore.QRect(270, 50, 211, 101))
        self.setting_permissionList.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.setting_permissionList.setObjectName("setting_permissionList")
        self.setting_permission = QtWidgets.QLabel(self.setting_msg)
        self.setting_permission.setGeometry(QtCore.QRect(270, 30, 131, 16))
        self.setting_permission.setObjectName("setting_permission")
        self.setting_givePermissionToAllAdmin = QtWidgets.QCheckBox(self.setting_msg)
        self.setting_givePermissionToAllAdmin.setGeometry(QtCore.QRect(520, 50, 201, 16))
        self.setting_givePermissionToAllAdmin.setObjectName("setting_givePermissionToAllAdmin")
        self.setting_dylan = QtWidgets.QGroupBox(self.setting_scrollAreaWidgetContents)
        self.setting_dylan.setGeometry(QtCore.QRect(10, 540, 761, 131))
        self.setting_dylan.setObjectName("setting_dylan")
        self.setting_enableUpdate = QtWidgets.QCheckBox(self.setting_dylan)
        self.setting_enableUpdate.setGeometry(QtCore.QRect(20, 30, 171, 16))
        self.setting_enableUpdate.setObjectName("setting_enableUpdate")
        self.setting_enableAnnouncement = QtWidgets.QComboBox(self.setting_dylan)
        self.setting_enableAnnouncement.setEnabled(False)
        self.setting_enableAnnouncement.setGeometry(QtCore.QRect(50, 60, 121, 21))
        self.setting_enableAnnouncement.setObjectName("setting_enableAnnouncement")
        self.setting_enableAnnouncement.addItem("")
        self.setting_enableAnnouncement.addItem("")
        self.setting_enableAnnouncement.addItem("")
        self.setting_announcement = QtWidgets.QLabel(self.setting_dylan)
        self.setting_announcement.setGeometry(QtCore.QRect(20, 60, 41, 21))
        self.setting_announcement.setObjectName("setting_announcement")
        self.setting_reset = QtWidgets.QPushButton(self.setting_dylan)
        self.setting_reset.setGeometry(QtCore.QRect(210, 80, 81, 31))
        self.setting_reset.setObjectName("setting_reset")
        self.setting_chosenTheme = QtWidgets.QComboBox(self.setting_dylan)
        self.setting_chosenTheme.setGeometry(QtCore.QRect(50, 90, 121, 20))
        self.setting_chosenTheme.setObjectName("setting_chosenTheme")
        self.setting_chosenTheme.addItem("")
        self.setting_chosenTheme.addItem("")
        self.setting_chosenTheme.addItem("")
        self.setting_theme = QtWidgets.QLabel(self.setting_dylan)
        self.setting_theme.setGeometry(QtCore.QRect(20, 90, 31, 21))
        self.setting_theme.setObjectName("setting_theme")
        self.setting_state = QtWidgets.QPushButton(self.setting_dylan)
        self.setting_state.setEnabled(False)
        self.setting_state.setGeometry(QtCore.QRect(210, 40, 81, 31))
        self.setting_state.setObjectName("setting_state")
        self.setting_scrollArea.setWidget(self.setting_scrollAreaWidgetContents)
        self.tabWidget.addTab(self.setting, "")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.about_Dylan = QtWidgets.QLabel(self.about)
        self.about_Dylan.setGeometry(QtCore.QRect(110, 40, 661, 91))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(48)
        self.about_Dylan.setFont(font)
        self.about_Dylan.setOpenExternalLinks(True)
        self.about_Dylan.setObjectName("about_Dylan")
        self.about_info = QtWidgets.QLabel(self.about)
        self.about_info.setGeometry(QtCore.QRect(20, 170, 751, 251))
        self.about_info.setTextFormat(QtCore.Qt.RichText)
        self.about_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.about_info.setOpenExternalLinks(True)
        self.about_info.setObjectName("about_info")
        self.about_logo = QtWidgets.QLabel(self.about)
        self.about_logo.setGeometry(QtCore.QRect(20, 40, 80, 80))
        self.about_logo.setText("")
        self.about_logo.setObjectName("about_logo")
        self.tabWidget.addTab(self.about, "")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.setting_colorfulLogOut.setCurrentIndex(2)
        self.setting_enableAnnouncement.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dylan"))
        self.Panel_controls.setTitle(_translate("MainWindow", "控制"))
        self.Panel_start.setText(_translate("MainWindow", "▶ 启动"))
        self.Panel_stop.setText(_translate("MainWindow", "■ 停止"))
        self.Panel_forcestop.setText(_translate("MainWindow", "强制关闭"))
        self.Panel_restart.setText(_translate("MainWindow", "↻ 重启"))
        self.Panel_consolegroup.setTitle(_translate("MainWindow", "控制台"))
        self.Panel_input.setPlaceholderText(_translate("MainWindow", "> 在此输入指令..."))
        self.Panel_info.setTitle(_translate("MainWindow", "服务器信息"))
        self.Panel_state.setText(_translate("MainWindow", "状态："))
        self.Panel_version.setText(_translate("MainWindow", "版本："))
        self.Panel_gamemode.setText(_translate("MainWindow", "游戏模式："))
        self.Panel_difficulty.setText(_translate("MainWindow", "游戏难度："))
        self.Panel_levelname.setText(_translate("MainWindow", "存档名称："))
        self.Panel_port.setText(_translate("MainWindow", "端口："))
        self.Panel_port_2.setText(_translate("MainWindow", "- / -"))
        self.Panel_gamemode_2.setText(_translate("MainWindow", "-"))
        self.Panel_difficulty_2.setText(_translate("MainWindow", "-"))
        self.Panel_version_2.setText(_translate("MainWindow", "-"))
        self.Panel_state_2.setText(_translate("MainWindow", "未启动"))
        self.Panel_levelname_2.setText(_translate("MainWindow", "-"))
        self.Panel_cpu.setText(_translate("MainWindow", "CPU使用率："))
        self.Panel_cpu_2.setText(_translate("MainWindow", "-%"))
        self.Panel_ram_2.setText(_translate("MainWindow", "-%"))
        self.Panel_ram.setText(_translate("MainWindow", "内存使用率："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panel), _translate("MainWindow", "控制面板"))
        self.regularlist.setSortingEnabled(True)
        item = self.regularlist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "捕获域"))
        item = self.regularlist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "正则表达式"))
        item = self.regularlist.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "备注"))
        item = self.regularlist.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "执行命令"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.regular), _translate("MainWindow", "正则"))
        self.plugins_total.setText(_translate("MainWindow", "共0个插件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plugins), _translate("MainWindow", "插件管理"))
        self.Bot_control.setTitle(_translate("MainWindow", "控制"))
        self.Bot_stop.setText(_translate("MainWindow", "停止"))
        self.Bot_start.setText(_translate("MainWindow", "启动"))
        self.Bot_info.setTitle(_translate("MainWindow", "信息"))
        self.Bot_state.setText(_translate("MainWindow", "状态："))
        self.Bot_qq.setText(_translate("MainWindow", "QQ："))
        self.Bot_receive.setText(_translate("MainWindow", "已接收："))
        self.Bot_send.setText(_translate("MainWindow", "已发送："))
        self.Bot_receive_2.setText(_translate("MainWindow", "0"))
        self.Bot_send_2.setText(_translate("MainWindow", "0"))
        self.Bot_qq_2.setText(_translate("MainWindow", "-"))
        self.Bot_state_2.setText(_translate("MainWindow", "未启动"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bot), _translate("MainWindow", "Bot"))
        self.setting_start.setTitle(_translate("MainWindow", "启动"))
        self.setting_file.setText(_translate("MainWindow", "启动路径"))
        self.setting_selectfile.setText(_translate("MainWindow", "选择文件"))
        self.setting_autoRestart.setText(_translate("MainWindow", "异常关服自动重启"))
        self.setting_bot.setTitle(_translate("MainWindow", "Bot"))
        self.setting_port1.setText(_translate("MainWindow", "发送端口"))
        self.setting_port2.setText(_translate("MainWindow", "接收端口"))
        self.setting_botSelectfile.setText(_translate("MainWindow", "选择文件"))
        self.setting_botFile.setText(_translate("MainWindow", "启动路径"))
        self.setting_savePort.setText(_translate("MainWindow", "保存端口"))
        self.setting_logout.setText(_translate("MainWindow", "清空登录态和缓存"))
        self.setting_enableOutputMsgToLog.setText(_translate("MainWindow", "保存消息和数据包到日志文件"))
        self.setting_console.setTitle(_translate("MainWindow", "控制台"))
        self.setting_color_style.setText(_translate("MainWindow", "彩色输出样式"))
        self.setting_colorfulLogOut.setItemText(0, _translate("MainWindow", "禁用"))
        self.setting_colorfulLogOut.setItemText(1, _translate("MainWindow", "原彩色输出"))
        self.setting_colorfulLogOut.setItemText(2, _translate("MainWindow", "预设(style.css)"))
        self.setting_enableOutputToLog.setText(_translate("MainWindow", "保存到日志文件"))
        self.setting_outputCommandToConsole.setText(_translate("MainWindow", "输出执行的命令到控制台"))
        self.setting_msg.setTitle(_translate("MainWindow", "消息"))
        self.setting_listenGroup.setText(_translate("MainWindow", "监听群号列表"))
        self.setting_permission.setText(_translate("MainWindow", "管理权限列表"))
        self.setting_givePermissionToAllAdmin.setText(_translate("MainWindow", "赋予所有群主和管理员管理权限"))
        self.setting_dylan.setTitle(_translate("MainWindow", "Dylan"))
        self.setting_enableUpdate.setText(_translate("MainWindow", "启动时新版本更新提示"))
        self.setting_enableAnnouncement.setItemText(0, _translate("MainWindow", "总是收取（推荐）"))
        self.setting_enableAnnouncement.setItemText(1, _translate("MainWindow", "仅显示重要公告"))
        self.setting_enableAnnouncement.setItemText(2, _translate("MainWindow", "禁用"))
        self.setting_announcement.setText(_translate("MainWindow", "公告"))
        self.setting_reset.setText(_translate("MainWindow", "重置设置"))
        self.setting_chosenTheme.setItemText(0, _translate("MainWindow", "默认"))
        self.setting_chosenTheme.setItemText(1, _translate("MainWindow", "Fusion"))
        self.setting_chosenTheme.setItemText(2, _translate("MainWindow", "Fusion（深色）"))
        self.setting_theme.setText(_translate("MainWindow", "主题"))
        self.setting_state.setText(_translate("MainWindow", "统计"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), _translate("MainWindow", "设置"))
        self.about_Dylan.setText(_translate("MainWindow", "Dylan"))
        self.about_info.setText(_translate("MainWindow", "<html><head/><body><p><a name=\"main\"/>界面&amp;功能参考 : <a href=\"https://mcsmanager.com/\"><span style=\" text-decoration: underline; color:#2d94a7;\">MCSManager</span></a> , <a href=\"https://www.minebbs.com/threads/bds-naive.4860/\"><span style=\" text-decoration: underline; color:#2d94a7;\">Naive</span></a> , <a href=\"https://www.minebbs.com/resources/zeroclear.1820/\"><span style=\" text-decoration: underline; color:#2d94a7;\">ZeroClear</span></a></p><p>机器人功能支持 : <a href=\"https://github.com/Mrs4s/go-cqhttp\"><span style=\" text-decoration: underline; color:#2d94a7;\">https://github.com/Mrs4s/go-cqhttp</span></a></p><p>爱发电 : <a href=\"https://afdian.net/@Zaiton\"><span style=\" text-decoration: underline; color:#2d94a7;\">https://afdian.net/@Zaiton</span></a></p><p>最新版下载 : <a href=\"http://github.com/Zaiton233/Dylan/releases\"><span style=\" text-decoration: underline; color:#2d94a7;\">https://github.com/Zaiton233/Dylan/releases</span></a></p><p>Github : <a href=\"https://github.com/Zaiton233/Dylan\"><span style=\" text-decoration: underline; color:#2d94a7;\">https://github.com/Zaiton233/Dylan</span></a></p><p>帮助&amp;介绍文档 : <a href=\"https://docs.qq.com/doc/p/843b94ec1a19c9592dbcccc7b289e688013e05fc?dver=3.0.27447048\"><span style=\" text-decoration: underline; color:#2d94a7;\">腾讯文档-Dylan</span></a></p><p>讨论群 ： <a href=\"https://jq.qq.com/?_wv=1027&amp;k=XNZqPSPv\"><span style=\" text-decoration: underline; color:#2d94a7;\">954829203</span></a></p><hr/><p align=\"center\">Copyright © 2022 Zaiton233. All Rights Reserved. <br/>向着光，才能一直往前走。 </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("MainWindow", "关于"))
from PyQt5 import QtWebEngineWidgets
