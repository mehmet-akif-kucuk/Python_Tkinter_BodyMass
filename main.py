import tkinter

window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=75, height=100)

# LABEL_KİLO
my_labelkilo = tkinter.Label(text="Ağırlığız (KG)", font=("Arial"))
my_labelkilo.config(fg="black")
my_labelkilo.grid(row=0, column=0)

# ENTRY_KİLO
my_entrykilo = tkinter.Entry(width=20)
my_entrykilo.grid(row=0, column=1)

# LABEL_BOY
my_labelboy = tkinter.Label(text="Boyunuz (M -ör: 1.80)", font=("Arial"))
my_labelboy.config(fg="black")
my_labelboy.grid(row=1, column=0)

# ENTRY_BOY
my_entryboy = tkinter.Entry(width=20)
my_entryboy.grid(row=1, column=1)

def hesapla_boykilo():

    if my_entryboy.get() and my_entrykilo.get() != "":
        kg = float(my_entrykilo.get())
        boy = float(my_entryboy.get())
        endex = kg / (boy*boy)
        print(kg)
        print(boy)
        print(endex)

        if endex < 18.5:
            message = "Çok Zayıfsınız"
        elif endex >= 18.5 and endex < 24.90:
            message = "Normalsiniz"
        elif endex >= 25.0 and endex < 29.90:
            message = "Fazla kilolu"
        elif endex >= 30.0 and endex < 34.90:
            message = "Obez (1. derece obezite)"
        elif endex >= 35.0 and endex < 39.90:
            message = "Aşırı obez (2. derece obezite)"
        else:
            message = "Morbid obez (3. derece obezite)"

        bilgi.config(text=f"{endex} {message}", fg="green")
        bilgi.grid(row=3, column=0)

    elif my_entrykilo.get() == "" and my_entryboy.get() != "":
        bilgi.config(text="Lütfen Ağırlığızı Giriniz", fg="orange")
        bilgi.grid(row=3, column=0)

    elif my_entryboy.get() == "" and my_entrykilo.get() != "":
        bilgi.config(text="Lütfen Boyunuzu Giriniz", fg="orange")
        bilgi.grid(row=3, column=0)

    elif my_entryboy.get() == "" and my_entrykilo.get() == "":
        bilgi.config(text="Lütfen Değer Giriniz", fg="orange")
        bilgi.grid(row=3, column=0)

    else:
        bilgi.config(text="HATALI ", fg="red")
        bilgi.grid(row=3, column=0)

# Label
bilgi = tkinter.Label(text="", font=("Arial"))

# Button
my_buttonHspla = tkinter.Button(text="Hey Tıkla !!", command=hesapla_boykilo)
my_buttonHspla.grid(row=3, column=1)

window.mainloop()
