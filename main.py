import tkinter as tk
from app_core import FaceAntiFakeApp

if __name__ == "__main__":
    window = tk.Tk()
    app = FaceAntiFakeApp(window)
    window.mainloop()