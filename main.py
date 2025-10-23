#!/usr/bin/env python3
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create web view
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("https://www.youtube.com"))
        
        # Create navigation bar
        nav_bar = QToolBar()
        nav_bar.setMovable(False)
        self.addToolBar(nav_bar)
        
        # Back button
        back_btn = QAction('← Back', self)
        back_btn.triggered.connect(self.web_view.back)
        nav_bar.addAction(back_btn)
        
        # Forward button
        forward_btn = QAction('Forward →', self)
        forward_btn.triggered.connect(self.web_view.forward)
        nav_bar.addAction(forward_btn)
        
        # Reload button
        reload_btn = QAction('🔄 Reload', self)
        reload_btn.triggered.connect(self.web_view.reload)
        nav_bar.addAction(reload_btn)
        
        # Home button
        home_btn = QAction('🏠 YouTube', self)
        home_btn.triggered.connect(self.home)
        nav_bar.addAction(home_btn)
        
        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL or search YouTube...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)
        
        # Go button
        go_btn = QAction('🚀 Go', self)
        go_btn.triggered.connect(self.navigate_to_url)
        nav_bar.addAction(go_btn)
        
        # Connect signals
        self.web_view.urlChanged.connect(self.update_url)
        self.web_view.titleChanged.connect(self.update_title)
        self.web_view.loadProgress.connect(self.show_loading)
        
        # Set central widget
        self.setCentralWidget(self.web_view)
        
        # Status bar
        self.status = self.statusBar()
        self.status.showMessage("Ready - Loading YouTube...")
        
        # Window settings
        self.setGeometry(100, 100, 1400, 900)
        self.setWindowTitle('GitHub Browser - YouTube')
        
        # Apply dark theme
        self.apply_dark_theme()
        
    def apply_dark_theme(self):
        # Set dark style sheet
        dark_stylesheet = """
        QMainWindow {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        QToolBar {
            background-color: #2d2d2d;
            border: none;
            spacing: 5px;
            padding: 5px;
        }
        QAction {
            color: #ffffff;
            background-color: #3d3d3d;
            padding: 8px 12px;
            border-radius: 4px;
        }
        QAction:hover {
            background-color: #4d4d4d;
        }
        QLineEdit {
            background-color: #3d3d3d;
            color: #ffffff;
            border: 1px solid #555;
            border-radius: 4px;
            padding: 8px 12px;
            font-size: 14px;
        }
        QLineEdit:focus {
            border-color: #ff0000;
        }
        """
        self.setStyleSheet(dark_stylesheet)
        
    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        if not url:
            return
            
        if not url.startswith(('http://', 'https://')):
            if ' ' in url or '.' not in url:
                # Search YouTube
                url = f"https://www.youtube.com/results?search_query={url.replace(' ', '+')}"
            else:
                url = 'https://' + url
                
        self.web_view.load(QUrl(url))
        self.status.showMessage(f"Loading: {url}")
        
    def update_url(self, q):
        self.url_bar.setText(q.toString())
        
    def update_title(self, title):
        self.setWindowTitle(f'{title} - GitHub Browser')
        
    def show_loading(self, progress):
        if progress < 100:
            self.status.showMessage(f"Loading... {progress}%")
        else:
            self.status.showMessage("Ready")
        
    def home(self):
        self.web_view.load(QUrl("https://www.youtube.com"))
        self.status.showMessage("Loading YouTube homepage...")

def main():
    # Enable high DPI scaling
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    # For headless environments
    if os.environ.get('DISPLAY') is None:
        os.environ['QT_QPA_PLATFORM'] = 'xcb'
        os.environ['DISPLAY'] = ':1'
    
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("GitHub Browser")
    app.setApplicationVersion("1.0")
    app.setWindowIcon(QIcon.fromTheme('web-browser'))
    
    # Create and show browser
    browser = Browser()
    browser.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()