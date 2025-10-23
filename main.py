import tkinter as tk
from tkinter import ttk
import cefpython3 as cef
import platform
import threading

class BrowserFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.browser = None
        self.bind("<Configure>", self.on_configure)
        self.nav_bar = self.create_nav_bar()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
    def create_nav_bar(self):
        nav_bar = tk.Frame(self)
        nav_bar.pack(fill=tk.X)
        
        # Back button
        back_btn = tk.Button(nav_bar, text="←", command=self.go_back)
        back_btn.pack(side=tk.LEFT)
        
        # Forward button
        forward_btn = tk.Button(nav_bar, text="→", command=self.go_forward)
        forward_btn.pack(side=tk.LEFT)
        
        # Reload button
        reload_btn = tk.Button(nav_bar, text="↻", command=self.reload)
        reload_btn.pack(side=tk.LEFT)
        
        # URL entry
        self.url_entry = tk.Entry(nav_bar)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.url_entry.bind("<Return>", self.load_url)
        
        # Go button
        go_btn = tk.Button(nav_bar, text="Go", command=self.load_url)
        go_btn.pack(side=tk.LEFT)
        
        # YouTube button
        yt_btn = tk.Button(nav_bar, text="YouTube", command=self.load_youtube)
        yt_btn.pack(side=tk.LEFT)
        
        return nav_bar
        
    def embed_browser(self):
        window_info = cef.WindowInfo()
        window_info.SetAsChild(self.main_frame.winfo_id(), 
                              [0, 0, self.winfo_width(), self.winfo_height()-50])
        self.browser = cef.CreateBrowserSync(window_info, url="https://www.youtube.com")
        
    def on_configure(self, event):
        if self.browser:
            self.browser.SetBounds(0, 0, event.width, event.height-50)
            
    def go_back(self):
        if self.browser:
            self.browser.GoBack()
            
    def go_forward(self):
        if self.browser:
            self.browser.GoForward()
            
    def reload(self):
        if self.browser:
            self.browser.Reload()
            
    def load_url(self, event=None):
        if self.browser:
            url = self.url_entry.get()
            if not url.startswith('http'):
                url = 'https://' + url
            self.browser.LoadUrl(url)
            
    def load_youtube(self):
        if self.browser:
            self.browser.LoadUrl("https://www.youtube.com")

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GitHub Browser - YouTube")
        self.root.geometry("1200x800")
        
        # Initialize CEF
        settings = {
            "multi_threaded_message_loop": False,
        }
        cef.Initialize(settings)
        
        self.browser_frame = BrowserFrame(self.root)
        self.browser_frame.pack(fill=tk.BOTH, expand=True)
        
        # Embed browser after mainloop starts
        self.root.after(100, self.browser_frame.embed_browser)
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def on_close(self):
        if self.browser_frame.browser:
            self.browser_frame.browser.CloseBrowser()
        cef.Shutdown()
        self.root.destroy()
        
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()
