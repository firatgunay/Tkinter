
import tkinter as tk

def fiyatHesaplama():
    arabaSecimi = car_var.get()
    secilen_ozellikler = feature_listbox.curselection()

    fiyat = 0

    if arabaSecimi == "Ford":
        fiyat += 800000

    elif arabaSecimi == "BMW":
        fiyat += 1800000

    elif arabaSecimi == "Audi":
        fiyat += 2000000

    for index in secilen_ozellikler:
        ozellik = feature_listbox.get(index)
        if ozellik == "çelik jant":
            fiyat += 20000
        elif ozellik == "sunroof":
            fiyat += 30000
        elif ozellik == "ses sistemi":
            fiyat += 15000
        elif ozellik == "kablosuz şarj":
            fiyat += 5000

    price_label.config(text="Fiyat: {} TL".format(fiyat))

window = tk.Tk()
window.geometry("300x300")
window.title("Araç Fiyat Hesaplama Sistemi")

car_label = tk.Label(window, text="Araç Seçin:")
car_label.pack()

car_var = tk.StringVar()
car_choices = ["Ford", "BMW", "Audi"]
car_dropdown = tk.OptionMenu(window, car_var, *car_choices)
car_dropdown.pack()

feature_label = tk.Label(window, text="İlave Özellikleri Seçin:")
feature_label.pack()

feature_listbox = tk.Listbox(window, selectmode="multiple")
feature_listbox.pack()

feature_choices = ["çelik jant", "sunroof", "ses sistemi", "kablosuz şarj"]
for feature in feature_choices:
    feature_listbox.insert(tk.END, feature)

calculate_button = tk.Button(window, text="Fiyatı Hesapla", command=fiyatHesaplama)
calculate_button.pack()

price_label = tk.Label(window, text=" Fiyatı: -")
price_label.pack()

window.mainloop()
