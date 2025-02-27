import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

def quotes(quote_label):
    response=requests.get('https://zenquotes.io/api/random')
    data=response.json()[0]

    quote=data['q'] + '\n-' + data['a']

    quote_label.setText(quote)


def gui_window():
    app=QApplication(sys.argv)
    window=QMainWindow()
    window.setWindowTitle('Xspire')
    window.setGeometry(400,200,700,400)
    window.setStyleSheet('background-color: #B6D094')
    content=QLabel(window)
    content.resize(800,100)
    content.setWordWrap(True)
    content.setText("\tWelcome to Xspire\nProviding just the motivation you need.\n")
    content.move(175,25)
    font=QFont()
    font.setFamily('Times New Roman')
    font.setPointSize(16)
    font.setBold(True)
    font.setUnderline(True)
    content.setFont(font)

    quote_label = QLabel("", window)  # Attach it to the window
    quote_label.setWordWrap(True)
    quote_label.setFont(QFont("Arial", 14))
    quote_label.setStyleSheet("""
        border: 2px solid black;
        padding: 10px;
        background-color: #f9f9f9;
        border-radius: 10px;
    """)
    quote_label.setGeometry(100, 150, 500, 100)  # Positioning

    # Get Quote button
    get_quote = QPushButton('Get New Quote', window)  # Attach it to the window
    get_quote.setGeometry(300, 300, 100, 40)  # Set button position
    get_quote.setStyleSheet('background-color: #BE8A60')
    get_quote.clicked.connect(lambda: quotes(quote_label))  # Pass QLabel to function

    copyright=QLabel(window)
    copyright.setText('(c) Harshit Raj')
    copyright.move(10,375)
    window.show()

    if __name__=='__main__':
        app.exec()


gui_window()