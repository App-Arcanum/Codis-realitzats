import tkinter as tk

# Dades de la matriu
matriu = [
    ["0", "2", "4", "6", "8", "A", "C", "E", "10", "12", "14", "16", "18", "1A", "1C", "1E"],
    ["20", "22", "24", "26", "28", "2A", "2C", "2E", "30", "32", "34", "36", "38", "3A", "3C", "3E"],
    ["40", "42", "44", "46", "48", "4A", "4C", "4E", "50", "52", "54", "56", "58", "5A", "5C", "5E"],
    ["60", "62", "64", "66", "68", "6A", "6C", "6E", "70", "72", "74", "76", "78", "7A", "7C", "7E"],
    ["80", "82", "84", "86", "88", "8A", "8C", "8E", "90", "92", "94", "96", "98", "9A", "9C", "9E"],
    ["A0", "A2", "A4", "A6", "A8", "AA", "AC", "AE", "B0", "B2", "B4", "B6", "B8", "BA", "BC", "BE"],
    ["C0", "C2", "C4", "C6", "C8", "CA", "CC", "CE", "D0", "D2", "D4", "D6", "D8", "DA", "DC", "DE"],
    ["E0", "E2", "E4", "E6", "E8", "EA", "EC", "EE", "F0", "F2", "F4", "F6", "F8", "FA", "FC", "FE"],
    ["1B", "19", "1F", "1D", "13", "11", "17", "15", "0B", "9", "0F", "0D", "3", "1", "7", "5"],
    ["3B", "29", "2F", "3D", "33", "31", "37", "35", "2B", "29", "2F", "2D", "23", "21", "27", "25"],
    ["5B", "59", "5F", "5D", "53", "51", "57", "55", "4B", "49", "4F", "4D", "43", "41", "47", "45"],
    ["7B", "79", "7F", "7D", "73", "71", "77", "75", "6B", "69", "6F", "6D", "63", "61", "67", "65"],
    ["9B", "99", "9F", "9D", "93", "91", "97", "95", "8B", "89", "8F", "8D", "83", "81", "87", "85"],
    ["BB", "B9", "BF", "BD", "B3", "B1", "B7", "B5", "AB", "A9", "AF", "AD", "A3", "A1", "A7", "A5"],
    ["DB", "D9", "DF", "DD", "D3", "D1", "D7", "D5", "CB", "C9", "CF", "CD", "C3", "C1", "C7", "C5"],
    ["FB", "F9", "FF", "FD", "F3", "F1", "F7", "F5", "EB", "E9", "EF", "ED", "E3", "E1", "E7", "E5"]
]

# Crear finestra
finestra = tk.Tk()
finestra.title("Multiplicar per 2")
finestra.configure(bg="white")

# Títol principal
titol = tk.Label(
    finestra, 
    text="Multiplicar per 2", 
    font=("Arial", 16, "bold"),  # Mida de lletra més gran
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
        bg="#ADD8E6",
        relief="solid", 
        borderwidth=1, 
        padx=10, 
        pady=5,
        font=font_num  # Font més gran
    ).grid(row=1, column=j+1, sticky="nsew")

# Afegir dades i capçaleres de files
for i, fila in enumerate(matriu):
    # Capçalera de fila (blau fluix)
    tk.Label(
        finestra, 
        text=capcaleres[i], 
        bg="#ADD8E6",
        relief="solid", 
        borderwidth=1, 
        padx=10, 
        pady=5,
        font=font_num  # Font més gran
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
            font=font_num  # Font més gran
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