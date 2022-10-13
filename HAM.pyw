from select import select
import tkinter as tk
from remp import *

window=tk.Tk()
window.attributes('-topmost',True)
window.title("Herramienta de calculo Almacen")
window.geometry("300x200")
descu=[35,30]
variable = tk.StringVar()
variable.set(descu[0])

def cop(c):
    window.clipboard_clear()
    window.clipboard_append(c)
    window.update()

def cal (event):

    valR.delete(0,"end")
    val_venta.delete(0,"end")

    art = float (Val_articulo.get())
    des = int (descuento.get())
    choice = int (variable.get())
    choice = 1+(choice/100)

    art=round(art-(art*des/100),2)
    valR.insert(0,remp(art))

    valor = round(art*choice*1.19,2)
    val_venta.insert(0,remp(valor))

tk.Label(window, text="Valor articulo C/U").grid(row=0, column=0)
Val_articulo=tk.Entry(window)
Val_articulo.insert(0,"0")
Val_articulo.focus()
Val_articulo.bind("<Return>", cal)
Val_articulo.grid(row=0, column=1)

tk.Label(window, text="Descuento %").grid(row=1, column=0)
descuento=tk.Entry(window)
descuento.insert(0,"0")
descuento.grid(row=1, column=1)
descuento.bind("<Return>", cal)

tk.Label(window, text="Valor Real").grid(row=2, column=0)
valR = tk.Entry(window)
valR.grid(row=2, column=1)

tk.Label(window, text="Porcentaje de ganancia").grid(row=3, column=0)
btmenu = tk.OptionMenu (window, variable, *descu, command=cal)
btmenu.config(bg="#c0d6e4")
btmenu.grid(row=3, column=1)

tk.Label(window, text="Precio De venta").grid(row=4, column=0)
val_venta = tk.Entry(window)
val_venta.grid(row=4, column=1)

btmenu = tk.Button (window, bg="#abd98c", text="/\\", command=lambda: cop(valR.get())).grid(row=2, column=2)
btmenu = tk.Button (window, bg="#abd98c", text="/\\", command=lambda: cop(val_venta.get())).grid(row=4, column=2)

window.mainloop()