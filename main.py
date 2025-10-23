#!/usr/bin/env python3
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class YouTubeBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Set window properties
        self.setWindowTitle("YouTube Browser - GitHub Codespaces")
        self.resize(1400, 900)
        self.move(100, 100)
        
        # Create web view
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("https://www.youtube.com"))
        
        # Create navigation
        self.createNavigation()
        
        # Set central widget
        self.setCentralWidget(self.web_view)
        
        # Apply styling
        self.applyDarkTheme()
        
        # Connect signals
        self.web_view.urlChanged.connect(self.updateUrl)
        self.web_view.titleChanged.connect(self.updateTitle)
        self.web_view.loadProgress.connect(self.showProgress)
        
        print("✅ YouTube Browser started!")
        
    def createNavigation(self):
        nav_bar = QToolBar("Navigation")
        nav_bar.setMovable(False)
        self.addToolBar(nav_bar)
        
        # Back button
        back_btn = QAction('←', self)
        back_btn.setShortcut('Alt+Left')
        back_btn.triggered.connect(self.web_view.back)
        nav_bar.addAction(back_btn)
        
        # Forward button
        forward_btn = QAction('→', self)
        forward_btn.setShortcut('Alt+Right')
        forward_btn.triggered.connect(self.web_view.forward)
        nav_bar.addAction(forward_btn)
        
        # Reload button
        reload_btn = QAction('↻', self)
        reload_btn.setShortcut('Ctrl+R')
        reload_btn.triggered.connect(self.web_view.reload)
        nav_bar.addAction(reload_btn)
        
        # Home button
        home_btn = QAction('🏠', self)
        home_btn.setShortcut('Ctrl+H')
        home_btn.triggered.connect(self.goHome)
        nav_bar.addAction(home_btn)
        
        nav_bar.addSeparator()
        
        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter YouTube URL or search...")
        self.url_bar.returnPressed.connect(self.navigateToUrl)
        nav_bar.addWidget(self.url_bar)
        
        # Go button
        go_btn = QAction('Go', self)
        go_btn.setShortcut('Return')
        go_btn.triggered.connect(self.navigateToUrl)
        nav_bar.addAction(go_btn)
        
    def applyDarkTheme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
                color: white;
            }
            QToolBar {
                background-color: #2d2d2d;
                border: none;
                spacing: 5px;
                padding: 8px;
            }
            QAction {
                background-color: #404040;
                color: white;
                padding: 8px 12px;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QAction:hover {
                background-color: #505050;
            }
            QAction:disabled {
                background-color: #333;
                color: #777;
            }
            QLineEdit {
                background-color: #3a3a3a;
                color: white;
                border: 1px solid #555;
                border-radius: 4px;
                padding: 8px 12px;
                font-size: 14px;
                min-width: 400px;
            }
            QLineEdit:focus {
                border-color: #ff0000;
            }
        """)
        
    def navigateToUrl(self):
        url = self.url_bar.text().strip()
        if not url:
            return
            
        if not url.startswith(('http://', 'https://')):
            if ' ' in url or '.' not in url:
                # Search YouTube
                url = f"https://www.youtube.com/results?search_query={url.replace(' ', '+')}"
            else:
                url = 'https://' + url
                
        print(f"🌐 Loading: {url}")
        self.web_view.load(QUrl(url))
        
    def updateUrl(self, url):
        self.url_bar.setText(url.toString())
        
    def updateTitle(self, title):
        self.setWindowTitle(f"{title} - YouTube Browser")
        
    def showProgress(self, progress):
        if progress < 100:
            self.statusBar().showMessage(f"Loading... {progress}%")
        else:
            self.statusBar().showMessage("Ready")
            
    def goHome(self):
        self.web_view.load(QUrl("https://www.youtube.com"))

def main():
    print("🚀 Starting YouTube Browser...")
    
    # Setup environment
    os.environ['QT_QPA_PLATFORM'] = 'xcb'
    os.environ['DISPLAY'] = ':0'
    
    # Qt application setup
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    app.setApplicationName("YouTube Browser")
    app.setApplicationVersion("1.0")
    
    # Create and show browser
    browser = YouTubeBrowser()
    browser.show()
    
    print("✅ Browser window should be visible in Desktop Lite!")
    print("🎥 Enjoy YouTube!")
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()