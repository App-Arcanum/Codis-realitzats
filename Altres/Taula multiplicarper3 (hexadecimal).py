import tkinter as tk

# Dades de la nova matriu
matriu = [
    ["0", "3", "6", "5", "C", "F", "A", "9", "18", "1B", "1E", "1D", "14", "16", "12", "11"],
    ["30", "33", "36", "35", "3C", "3F", "3A", "39", "28", "2B", "2E", "2D", "24", "27", "22", "21"],
    ["60", "63", "66", "65", "6C", "6A", "6C", "69", "78", "7B", "7E", "7D", "74", "77", "72", "71"],
    ["50", "53", "56", "55", "5C", "5F", "5A", "59", "48", "4B", "4E", "4D", "44", "47", "42", "41"],
    ["C0", "C3", "C6", "C5", "CC", "CF", "CA", "C9", "D8", "DB", "DE", "DD", "D4", "D7", "D2", "D1"],
    ["F0", "F3", "F6", "F5", "FC", "FF", "FA", "F9", "E8", "EB", "EE", "ED", "E4", "E7", "E2", "E1"],
    ["A0", "A3", "A6", "A5", "AC", "AF", "AA", "A9", "B8", "BB", "BE", "BD", "B4", "B7", "B2", "B1"],
    ["90", "93", "96", "95", "9C", "9F", "9A", "99", "88", "8B", "8E", "8D", "84", "87", "82", "81"],
    ["9B", "98", "9D", "9E", "97", "94", "91", "92", "83", "80", "85", "86", "8F", "8C", "89", "8A"],
    ["AB", "A8", "AD", "AE", "A7", "A4", "A1", "A2", "B3", "B0", "B5", "B6", "BF", "BC", "B9", "BA"],
    ["FB", "F8", "FD", "FE", "F7", "F4", "F1", "F2", "E3", "E0", "E5", "E6", "EF", "EC", "E9", "EA"],
    ["CB", "C8", "CD", "CE", "C7", "C4", "C1", "C2", "D3", "D0", "D5", "D6", "DF", "DC", "D9", "DA"],
    ["5B", "58", "5D", "5E", "57", "54", "51", "52", "43", "40", "45", "46", "4F", "4C", "49", "4A"],
    ["6B", "68", "6D", "6E", "67", "64", "61", "62", "73", "50", "75", "76", "7F", "7C", "79", "7A"],
    ["3B", "38", "3D", "3E", "37", "34", "31", "32", "23", "20", "25", "26", "2F", "2C", "29", "2A"],
    ["0B", "8", "0D", "0E", "7", "4", "1", "2", "13", "10", "15", "16", "1F", "1C", "19", "1A"]
]

# Crear finestra
finestra = tk.Tk()
finestra.title("Multiplicar per 3")
finestra.configure(bg="white")

# Títol principal
titol = tk.Label(
    finestra, 
    text="Multiplicar per 3", 
    font=("Arial", 16, "bold"),
    bg="white"
)
titol.grid(row=0, column=0, columnspan=17, pady=10)

# Capçaleres de columnes (0-F)
capcaleres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# Configuració de font per als números
font_num = ("Arial", 16)

# Afegir capçaleres de columnes (fila 1)
for j, valor in enumerate(capcaleres):
    tk.Label(
        finestra, 
        text=valor, 
        bg="#ADD8E6",  # Blau fluix
        relief="solid", 
        borderwidth=1, 
        padx=10, 
        pady=5,
        font=font_num
    ).grid(row=1, column=j+1, sticky="nsew")

# Afegir dades i capçaleres de files
for i, fila in enumerate(matriu):
    # Capçalera de fila (blau fluix)
    tk.Label(
        finestra, 
        text=capcaleres[i], 
        bg="#ADD8E6",  # Blau fluix
        relief="solid", 
        borderwidth=1, 
        padx=10, 
        pady=5,
        font=font_num
    ).grid(row=i+2, column=0, sticky="nsew")
    
    # Valors de la matriu (quadrícula)
    for j, valor in enumerate(fila):
        tk.Label(
            finestra, 
            text=valor, 
            relief="solid", 
            borderwidth=1, 
            padx=10, 
            pady=5,
            font=font_num
        ).grid(row=i+2, column=j+1, sticky="nsew")

# Centrar la finestra a la pantalla
finestra.update_idletasks()
amplada = finestra.winfo_width()
alcada = finestra.winfo_height()
pos_x = (finestra.winfo_screenwidth() // 2) - (amplada // 2)
pos_y = (finestra.winfo_screenheight() // 2) - (alcada // 2)
finestra.geometry(f"+{pos_x}+{pos_y}")

# Fer que les cel·les s'ajustin al expandir la finestra
for i in range(17):
    finestra.grid_columnconfigure(i, weight=1)
for i in range(18):
    finestra.grid_rowconfigure(i, weight=1)

finestra.mainloop()