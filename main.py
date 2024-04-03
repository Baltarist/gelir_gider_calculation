from tkinter import *

window = Tk()
window.geometry("300x500")

window.title("Gelir Gider Hesaplama")

gelir = Label(text="Gelir Tutarı:")
gelir.pack()

gelir_tutar = Entry(window, width=30)
gelir_tutar.pack()

gider = Label(text="Gider Tutarı:")
gider.pack()

gider_tutar = Entry(window, width=30)
gider_tutar.pack()


def total():
    a = gelir_tutar.get()
    b = gider_tutar.get()

    if a == "" or b == "":
        result_label.config(text="Enter gelir and gider")

    else:
        toplam = int(a) - int(b)
        result_label.config(text=f"Sonuç: {toplam}")

hesap = Button(window, text="Calculate", command=total)
hesap.pack()

result_label = Label()
result_label.pack()



window.mainloop()
