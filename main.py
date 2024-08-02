from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QFileSystemWatcher, QTimer
from PyQt5.QtWebChannel import QWebChannel
from lib.web_channel import WebChannel
from jinja2 import Template
from pathlib import Path

import os

ROOT = Path(__file__).parent
TEMPLATE_FILE = ROOT / 'template/index.jinja'
DIST_DIRECTORY = ROOT / 'dist'
BUNDLE_FILE = ROOT / 'dist/bundle.js'

def load_html():
    with open(TEMPLATE_FILE) as file:
        return file.read()

def load_js():
    try:
        with open(BUNDLE_FILE) as file:
            return file.read()
    except FileNotFoundError:
        return ""
    
def render_template():
    template = Template((
        load_html()
    ))
    return template.render({
        'script': load_js()
    })

class MainWindow(QMainWindow):
    def __init__(self, debug = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_ui()

        if debug:
            self.timer = QTimer()
            self.timer.timeout.connect(self.check_if_bundle_exists)
            self.timer.start(1000)
            self.__setup_watcher()

    def check_if_bundle_exists(self):
        if os.path.exists(BUNDLE_FILE):
            self.watcher.addPath(str(BUNDLE_FILE))
            self.timer.stop()
            self.reload_web_view()

    def __init_ui(self):
        self.setWindowTitle('Title goes here')

        self.web_view = QWebEngineView()
        self.web_view.setHtml(
            render_template()
        )
        self.setCentralWidget(self.web_view)
        self.channel = QWebChannel()
        self.web_channel = WebChannel()
        self.channel.registerObject("qtObject", self.web_channel)
        self.web_view.page().setWebChannel(self.channel)

    def reload_web_view(self):
        self.web_view.reload()
        self.web_view.setHtml(render_template())
    
    def __setup_watcher(self):
        self.watcher = QFileSystemWatcher()
        self.watcher.fileChanged.connect(self.reload_web_view)

if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow(debug=True)
    win.show()
    exit(app.exec_())