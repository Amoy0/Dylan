from my_window_effect import WindowEffect
from PyQt5.QtCore import QEvent,Qt
from PyQt5.QtWidgets import QMenu

class Menu(QMenu):
    """ 自定义菜单 """
    windowEffect = WindowEffect()

    def __init__(self, string='', parent=None):
        super().__init__(string, parent)
        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.Popup | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground | Qt.WA_StyledBackground)
        self.setQss()

    def event(self, e: QEvent):
        if e.type() == QEvent.WinIdChange:
            self.hWnd = int(self.winId())
            self.setMenuEffect()
        return QMenu.event(self, e)

    def setMenuEffect(self):
        """ 开启特效 """
        self.windowEffect.setAeroEffect(self.hWnd)
        self.windowEffect.setShadowEffect(self,True)

    def setQss(self):
        """ 设置层叠样式 """
        self.setStyleSheet('''
QMenu {
    background-color: rgba(242, 242, 242,0.7);
    /*background-color: white;*/
    font: 12px "Microsoft YaHei";
    padding: 5px 0px 16px 0px;
    border: 1px solid rgb(196, 199, 200);
    border-radius: 0px;
}

QMenu::item {  
    padding: 5px 20px 5px 10px;
    /*background-color: transparent;*/
}

QMenu::item:selected {
    border-width: 1px;
    border-color: rgb(212, 212, 212);
    background: rgb(218, 218, 218);
}''')

