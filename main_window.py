from tkinter import *
from tkinter.ttk import *
import action_manager


class MainWindow:
    def __init__(self):
        self.action_man = action_manager.ActionManager(self.post_status_update)
        self.main_window = Tk()
        self.main_window.state('zoomed')
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.columnconfigure(1, weight=1)
        self.main_window.columnconfigure(2, weight=1)
        self.main_window.columnconfigure(3, weight=1)
        self.title = Label(text="Streaming & Recording Manager", font=("Arial, 25"))
        self.title.grid(column=0, columnspan=4, row=0)
        self.start_service_button = Button(text="Service Start")
        self.start_service_button.bind("<Button-1>", self.start_service_button_click)
        self.start_service_button.grid(column=0, row=1)
        self.start_sermon_button = Button(text="Sermon Start")
        self.start_sermon_button.bind("<Button-1>", self.start_sermon_button_click)
        self.start_sermon_button.grid(column=1, row=1)
        self.end_sermon_button = Button(text="Sermon End")
        self.end_sermon_button.bind("<Button-1>", self.end_sermon_button_click)
        self.end_sermon_button.grid(column=2, row=1)
        self.end_service_button = Button(text="End Service")
        self.end_service_button.bind("<Button-1>", self.end_service_button_click)
        self.end_service_button.grid(column=3, row=1)
        self.current_status = Entry()
        self.current_status.grid(column=0, columnspan=4, row=2)
        self.status_history = Text()
        self.status_history.grid(column=0, columnspan=4, row=3)

    def run(self):
        self.main_window.mainloop()

    def start_service_button_click(self, event):
        self.action_man.start_service()

    def start_sermon_button_click(self, event):
        #self.action_man.start_sermon()
        self.action_man.status_test()

    def end_sermon_button_click(self, event):
        self.action_man.end_sermon()

    def end_service_button_click(self, event):
        self.action_man.end_service()

    def post_status_update(self, status):
        self.main_window.after(0, self._post_status_update, status)

    def _post_status_update(self, status):
        #self.status_history.insert(0, self.current_status.get())
        self.current_status.delete(0)
        self.current_status.insert(0, status)