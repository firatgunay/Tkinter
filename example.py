
import tkinter as tk

def calculate_price():
    selected_car = car_var.get()
    selected_feature = feature_var.get()

    if selected_car == "Ford":
        if selected_feature == "çelik jant":
            price = 800000 + 20000
        elif selected_feature == "sunroof":
            price = 800000 + 30000
        elif selected_feature == "ses sistemi":
            price = 800000 + 15000
        elif selected_feature == "kablosuz şarj":
            price = 800000 + 5000
        else:
            price = 800000

    elif selected_car == "BMW":
        if selected_feature == "çelik jant":
            price = 1800000 + 40000
        elif selected_feature == "sunroof":
            price = 1800000 + 45000
        elif selected_feature == "ses sistemi":
            price = 1800000 + 25000
        elif selected_feature == "kablosuz şarj":
            price = 1800000 + 10000
        else:
            price = 1800000

    elif selected_car == "Audi":
        if selected_feature == "çelik jant":
            price = 2000000 + 70000
        elif selected_feature == "sunroof":
            price = 2000000 + 75000
        elif selected_feature == "ses sistemi":
            price = 2000000 + 55000
        elif selected_feature == "kablosuz şarj":
            price = 2000000 + 20000
        else:
            price = 2000000

    price_label.config(text="Fiyat: {} TL".format(price))

root = tk.Tk()
root.title("Araç Fiyat Hesaplama sistemi")

car_label = tk.Label(root, text="Araç Seçin:")
car_label.pack()

car_var = tk.StringVar()
car_choices = ["Ford", "BMW", "Audi"]
car_dropdown = tk.OptionMenu(root, car_var, *car_choices)
car_dropdown.pack()

feature_label = tk.Label(root, text="İlave Özellik Seçin:")
feature_label.pack()

feature_var = tk.StringVar()
feature_choices = ["çelik jant", "sunroof", "ses sistemi", "kablosuz şarj"]
feature_dropdown = tk.OptionMenu(root, feature_var, *feature_choices)
feature_dropdown.pack()

calculate_button = tk.Button(root, text="Fiyatı Hesapla", command=calculate_price)
calculate_button.pack()

price_label = tk.Label(root, text=" Fiyatı: -")
price_label.pack()

root.mainloop()
