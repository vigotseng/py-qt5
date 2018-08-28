from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode
import os
import sys
import time

from PyQt5.QtGui import QPixmap

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 41))
        self.label.setObjectName("label")
        self.sourceEdit = QtWidgets.QTextEdit(Form)
        self.sourceEdit.setGeometry(QtCore.QRect(90, 10, 291, 31))
        self.sourceEdit.setObjectName("sourceEdit")
        self.picLab = QtWidgets.QLabel(Form)
        self.picLab.setGeometry(QtCore.QRect(30, 80, 221, 201))
        self.picLab.setObjectName("picLab")
        self.genButton = QtWidgets.QPushButton(Form)
        self.genButton.setGeometry(QtCore.QRect(300, 80, 75, 81))
        self.genButton.setObjectName("genButton")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(300, 200, 75, 81))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(Form)
        #退出按钮绑定的槽函数
        self.exitButton.clicked.connect(Form.close)
        #生成图片按钮绑定的自定义槽函数
        self.genButton.clicked.connect(self.generateImg)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "二维码生成"))
        self.label.setText(_translate("Form", "SourceCode"))
        self.genButton.setText(_translate("Form", "生成"))
        self.exitButton.setText(_translate("Form", "退出"))
        self.OkImage = os.getcwd() + r'\qrcode.png'

    def generateImg(self):
        qr.add_data(self.sourceEdit.toPlainText())
        qr.make(fit=True)
        #生成二维码图片
        img = qr.make_image()
        #需要注意的是，有序自身机制，使用png形式图片会相当方便，其他的格式在生成QPixmap形式时候会报null
        img.save('qrcode.png')
        #将已经生成的图片加载成为QPixmap格式
        qpic=QPixmap(self.OkImage).scaled(self.picLab.width(),self.picLab.height())
        self.picLab.setPixmap(qpic)
        #将已经生成的图片删除，不占用空间
        os.remove(self.OkImage)


if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())