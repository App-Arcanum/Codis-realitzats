import tkinter as tk

# Crear finestra principal
finestra = tk.Tk()
finestra.title("Matriu MixColumns AES")
finestra.configure(bg="white")  # Fons blanc

# Definir la matriu fixa MixColumns
matriu_mixcolumns = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

# Colors suaus per cada fila
colors_fila = ["#FFEBEE", "#E3F2FD", "#E8F5E9", "#FFF3E0"]

# Crear un frame per organitzar la matriu
frame_matriu = tk.Frame(finestra, bg="white", padx=20, pady=20)
frame_matriu.pack()

# Mostrar la matriu amb colors
for i in range(4):
    for j in range(4):
        etiqueta = tk.Label(
            frame_matriu,
            text=str(matriu_mixcolumns[i][j]),
            font=("Arial", 24, "bold"),
            width=4,
            height=2,
            bg=colors_fila[i],  # Color de la fila
            fg="black",
            relief="solid",
            bd=1
        )
        etiqueta.grid(row=i, column=j, padx=5, pady=5)

# Executar la finestra
finestra.mainloop()
