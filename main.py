import program
import functions
import tkinter as tk


def on_button_click():
    url = url_entry.get()
    label.config(text="Trwa przetwarzanie danych...")
    program.main(url)
    label.config(text="Operacja zakończona!")
    fouls_amount = functions.getFouls()
    name = functions.getName()
    name_label.config(text=f"Imię: {name}")
    fouls_label.config(text=f"Łączna liczba fauli: {fouls_amount}")
    for match in program.list_of_matches:
        print(f"Faule: {match[0]}, Informacje o meczu: {match[1]}")




window = tk.Tk()
window.title("BukBet")
window.iconbitmap("assets/icon.ico")
window_width = 400
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

label = tk.Label(window, text="Witaj w aplikacji BukBet!", font=("Arial", 14))
label.pack(pady=20)
url_entry = tk.Entry(window, font=('calibre', 10, 'bold'))
url_entry.pack(pady=10)
name_label = tk.Label(window, text="", font=("Arial", 14))
name_label.pack(pady=10)
fouls_label = tk.Label(window, text="", font=("Arial", 14))
fouls_label.pack(pady=10)




button = tk.Button(window, text="Szukaj", font=("Arial", 12), command=on_button_click)
button.pack(pady=10)

window.mainloop()

#nie działa pobranie naz drużyny