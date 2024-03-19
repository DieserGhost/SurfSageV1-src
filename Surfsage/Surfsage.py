import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SurfSage")
        self.setGeometry(0, 0, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.layout.addWidget(self.url_bar)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(self.go_forward)
        self.layout.addWidget(self.forward_button)

        self.browser = QWebEngineView()
        self.browser.page().setWebChannel(self.browser.page().webChannel()) 
        self.browser.page().createWindow = self.create_new_window
        self.layout.addWidget(self.browser)

        self.navigate_to_url("https://www.google.de")

    def navigate_to_url(self, url=None):
        if url is None:
            url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))
        self.url_bar.setText(url)

    def go_back(self):
        self.browser.back()

    def go_forward(self):
        self.browser.forward()

    def create_new_window(self, webWindowType):
        new_window = WebBrowser()
        new_window.show()
        return new_window.browser

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
