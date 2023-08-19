import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class SimpleGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create a QPushButton widget
        button = QPushButton('Click me', self)

        # Connect the button's clicked signal to the custom function
        button.clicked.connect(self.on_button_click)

        # Set window properties
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Simple PyQt5 Program')
        
        # Show the window
        self.show()

    def on_button_click(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SimpleGUI()
    sys.exit(app.exec_())
