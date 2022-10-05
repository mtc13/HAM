from select import select
import tkinter as tk
from remp import *

window=tk.Tk()
window.title("Herramienta de calculo Almacen")
window.geometry("300x200")
descu=[35,30]
variable = tk.StringVar()
variable.set(descu[0])

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
btmenu.grid(row=3, column=1)

tk.Label(window, text="Precio De venta").grid(row=4, column=0)
val_venta = tk.Entry(window)
val_venta.grid(row=4, column=1)

window.mainloop()