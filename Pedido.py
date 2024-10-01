import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title('Quer algo?')
root.geometry('600x600')
root.configure(background='#3399FF')

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo('Obrigado por querer', ' Obrigado por querer')

def denied():
    button_1.destroy()

margin = tk.Canvas(root, width=500, bg='#3399FF', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = tk.Label(root, bg='#3399FF', text='quer algo?', fg='#000000', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#3333FF', command=denied, relief='ridge', bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
button_1.place(x=250, y=250)  # inicialmente coloquei o botão no centro da tela
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text='Aceito', bg='#3333FF', relief='ridge', bd=3, command=accepted, font=('Montserrat', 14, 'bold'))
button_2.pack()

root.mainloop()