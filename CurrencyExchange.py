import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QComboBox
import Helper
import requests
from PyQt5.QtCore import Qt
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Currency Converter",self)
        self.label2 = QLabel("Currency 1: ",self)
        self.label3 = QLabel("Currency 2: ",self)
        self.combo1 = QComboBox(self)
        self.combo1.addItems(Helper.country_names)
        self.combo2 = QComboBox(self)
        self.combo2.addItems(Helper.country_names)
        self.button = QPushButton("Submit",self)
        self.label4 = QLabel(self)
        
        self.initUI()
    def initUI(self):
        self.label.setObjectName("label")
        self.label2.setObjectName("label2")
        self.label3.setObjectName("label3")
        self.label4.setObjectName("label4")
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label2)
        hbox1.addWidget(self.label3)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.combo1)
        hbox2.addWidget(self.combo2)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.button,alignment=Qt.AlignCenter)
        vbox.addWidget(self.label4)
        self.setLayout(vbox)
        self.button.setFixedWidth(80)
        self.label.setAlignment(Qt.AlignCenter)
        #self.button.setAlignment(Qt.AlignCenter)
        self.label4.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                            QLabel#label{font-size:60px;
                                        border:2px solid hsl(222,100%,69%);
                                        background-color:hsl(222,100%,58.3%);             
                                        padding:10px;}
                            QLabel#label2{font-size:30px;}
                            QLabel#label3{font-size:30px;}
                            QComboBox{font-size:15px;}
                            QPushButton{font-size:10px;
                                        padding:5px 10px;
                                        border:1px solid;
                                        border-radius:5px;}
                            QPushButton:hover{font-size:12px;}
                            QLabel#label4{font-size:30px;}
                                    """)
        
        self.button.clicked.connect(self.conversion)
    def conversion(self):
        
        url = f"https://v6.exchangerate-api.com/v6/c67aaf16e1b3fc94eda8f517/latest/{Helper.country_currency_data[self.combo1.currentText()]}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data['result']=='success':
                self.display(data)
        except Exception as e:
            self.label4.setText(f"Error: {e}")

    def display(self,data):
        self.label4.setText(f"1 {Helper.country_currency_data[self.combo1.currentText()]} is worth {data['conversion_rates'][Helper.country_currency_data[self.combo2.currentText()]]:.2f} {Helper.country_currency_data[self.combo2.currentText()]}")
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())