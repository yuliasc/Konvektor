from tkinter import *
from tkinter import ttk, messagebox
def convert():
    try:
        x = float(entry.get())
        if v.get() == 1:
            d = x * 38.55
            label3.config(text=f"Результат у доларах: {round(d, 2)} USD")
        elif v.get() == 2:
            c = 41.78
            d = x * c
            label3.config(text=f"Результат у євро: {round(d, 2)} UAH")
    except ValueError:
        messagebox.showwarning("Некоректна сума", "Йой,ти ввів щось не зрозуміле,введи коректну суму!!!😋")

def valuta():
    if v.get() == 0:
        messagebox.showwarning("Вибери валюту!", "Йой,ти не вибрав валюту.Вибери!!!😊")
    else:
        convert()

root = Tk()
root.geometry("400x300")
root.title("Конвертер валют")
photo = PhotoImage(file="many.png")
root.iconphoto(False,photo)

f = Frame(root, bd=2, relief=SOLID, padx=10, pady=10, bg="#b3b3b3")
f.grid(row=1, column=0, pady=(10, 0), sticky="ew")

label1 = Label(f, text="Виберіть валюту:", font=("Brush Script MT", 16), bd=2, fg="#000000", bg="#b3b3b3")
label1.grid(row=0, column=0, pady=(10, 0))
v = IntVar()
dollar = Radiobutton(f, text='Долар', font=("Brush Script MT", 10), bd=2, bg="#0d0d0d", fg="#ffff00", variable=v, value=1)
dollar.grid(row=0, column=1, padx=5, pady=5)
euro = Radiobutton(f, text='Євро', font=("Brush Script MT", 10), bd=2, bg="#0d0d0d", fg="#ffff00", variable=v, value=2)
euro.grid(row=0, column=2, padx=5, pady=5)

label2 = Label(root,text="Введіть суму:",font=("Brush Script MT", 16), bd=2, fg="#000000")
label2.grid(row=2, column=0, pady=(10, 0))
entry = Entry(root,font=("Brush Script MT", 14), bd=6, bg="#a6a6a6", fg="#ffff00")
entry.grid(row=3, column=0, padx=5, pady=5)
btn = Button(root, text="Згенерувати",font=("Brush Script MT", 12), bd=2, bg="#0d0d0d", fg="#ffff00",  command=valuta)
btn.grid(row=4, column=0,pady=(10, 0))

f2= Frame(root, bd=2, relief=SOLID, padx=10, pady=10, bg="#b3b3b3")
f2.grid(row=5, column=0, pady=(10, 0), sticky="ew")
label3 = Label(f2, text="",font=("Brush Script MT", 16), bd=2, fg="#000000", bg="#b3b3b3")
label3.grid(row=5, column=0, columnspan=3, pady=(10, 0))
root.mainloop()