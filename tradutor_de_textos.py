import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit

# Importa o tradutor da biblioteca googletrans
from googletrans import Translator

# Define a classe principal da aplicação
class TradutorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configura a janela principal
        self.setWindowTitle("Tradutor de Texto")
        self.setGeometry(100, 100, 400, 200)

        # Cria um widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Cria um layout vertical para organizar os elementos da interface
        layout = QVBoxLayout(central_widget)

        # Cria um rótulo e uma área de texto para o texto original
        self.texto_original_label = QLabel("Texto Original:")
        self.texto_original = QTextEdit(self)

        # Cria um rótulo e uma área de texto para a tradução
        self.traducao_label = QLabel("Tradução:")
        self.traducao = QTextEdit(self)
        self.traducao.setReadOnly(True)

        # Cria um botão para iniciar a tradução
        self.traduzir_button = QPushButton("Traduzir", self)
        self.traduzir_button.clicked.connect(self.traduzir_texto)

        # Adiciona os elementos à interface no layout
        layout.addWidget(self.texto_original_label)
        layout.addWidget(self.texto_original)
        layout.addWidget(self.traducao_label)
        layout.addWidget(self.traducao)
        layout.addWidget(self.traduzir_button)

    # Função para traduzir o texto do campo original para o campo de tradução
    def traduzir_texto(self):
        texto = self.texto_original.toPlainText()
        tradutor = Translator()

        try:
            # Traduz do inglês ('en') para o português ('pt')
            resultado = tradutor.translate(texto, src='en', dest='pt')
            self.traducao.setPlainText(resultado.text)
        except Exception as e:
            # Em caso de erro, exibe uma mensagem de erro no campo de tradução
            self.traducao.setPlainText("Erro na tradução: " + str(e))

# Ponto de entrada da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tradutor_app = TradutorApp()
    tradutor_app.show()
    sys.exit(app.exec())
