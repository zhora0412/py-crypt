from cesar import *
from cesar_func import *
from send import *

import sys
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()



def crypting():
    textFor = ui.textEdit.toPlainText()
    keyFor = int(ui.spinBox.value())
    mailFor = ui.textEdit_2.toPlainText()
    criptText = crypt(textFor, keyFor)
    key = str(keyFor)
    sendMessage(criptText, key, mailFor)

def decrypting():
    textFor = ui.textEdit.toPlainText()
    keyFor = int(ui.spinBox.value())
    z = decrypt(textFor, keyFor)
    ui.textBrowser.insertPlainText(z)




def on_сlick():
    if ui.radioButton.isChecked():
        crypting()
    elif ui.radioButton_2.isChecked():
        decrypting()
    else :
        print("please chose")


ui.pushButton.clicked.connect(on_сlick)


sys.exit(app.exec_())





