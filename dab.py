import tkinter as tk
from trigger import activate

def dab():
    led = activate()

    led.trigger(4)

    print("dab")

class dabMachine():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("dab.exe")
        self.win.geometry("300x300")

        self.app = tk.Label(text="press the button to dab on those haters")

        self.button = tk.Button(text="i\'m ready to dab", command=dab)

    def build(self):
        self.app.place(x=10, y=10)

        self.button.place(x=10, y=30)

        self.win.mainloop()

if __name__ == "__main__":
    readyToDab = dabMachine()

    readyToDab.build()
