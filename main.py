from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,  QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot, Qt
from datetime import datetime
import sys

class JanelaPrinciapl(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(1200, 800)
        self.setWindowTitle("Jogo da forca")
        self.central_widget = QWidget(self)

        self.setCentralWidget(self.central_widget)

        self.titulo = QLabel(self)
        self.titulo.setText("Jogo da forca")
        self.titulo.setStyleSheet("font-size: 32px;")
        self.titulo.setAlignment(Qt.AlignCenter)

        inp_layout = QHBoxLayout()
        self.enviar_letra = QPushButton(text="Verificar")
        self.label_letra = QLineEdit()
        inp_layout.addWidget(self.label_letra)
        inp_layout.addWidget(self.enviar_letra)

        self.boneco_img = QPixmap('./images/0_inicio')
        self.boneco = QLabel()
        self.boneco.setPixmap(self.boneco_img)
        self.boneco.setAlignment(Qt.AlignCenter)

        self.user_inps = QWidget()
        self.user_inps.setLayout(inp_layout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.titulo)
        self.layout.addWidget(self.boneco)
        self.layout.addWidget(self.user_inps)

        self.central_widget.setLayout(self.layout)



    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela_principal = JanelaPrinciapl()
    espaco_disp = janela_principal.screen().availableGeometry()
    janela_principal.resize(espaco_disp.width() * 2 / 3, espaco_disp.height() * 2 / 3)
    janela_principal.show()
    sys.exit(app.exec())