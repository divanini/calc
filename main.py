
import tkinter as tk


from app.calculator import Calculator

if __name__ == '__main__':
    master = tk.Tk()
    main = Calculator(master)
    main.start()
