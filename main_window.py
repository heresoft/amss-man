import tkinter as tk
import azure_server as az


class MainWindow:
    def __init__(self):
        self.server = None
        self.main_window = tk.Tk()
        title = tk.Label(text="AMSS Man")
        title.pack()
        run_button = tk.Button(text="Start Server")
        run_button.bind("<Button-1>", self.run_button_click)
        run_button.pack()

    def run(self):
        self.main_window.mainloop()

    def run_button_click(self, event):
        self.server = az.AzureServer()
        res = self.server.start()
