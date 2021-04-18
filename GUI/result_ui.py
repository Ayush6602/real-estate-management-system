import tkinter as tk

class ResultUi(tk.Canvas):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.title('Result')
        self.geometry('1280x720')
        res_font = f'ariel {min(720, 1280) // 50}'
        tk.Label(self,text = self.result, font = res_font, fg='green', background='black').pack(fill='both', expand=1)
        self.mainloop()