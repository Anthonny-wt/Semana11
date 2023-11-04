import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# Crear una función para agregar un libro al inventario
def agregar_libro():
    categoria = categoria_var.get()
    genero = ""
    if genero_femenino_var.get():
        genero += "Femenino "
    if genero_masculino_var.get():
        genero += "Masculino "
    fecha = fecha_cal.get_date()
    monto = float(monto_entry.get())

    libro = {
        "Categoría": categoria,
        "Género": genero.strip(),  # Elimina los espacios en blanco adicionales
        "Fecha": fecha,
        "Monto": monto
    }
    inventario.append(libro)
    actualizar_lista()
    limpiar_campos()

# Crear una función para actualizar la lista de libros en la interfaz
def actualizar_lista():
    lista_text.delete(1.0, tk.END)
    for i, libro in enumerate(inventario, start=1):
        lista_text.insert(tk.END, f"Libro #{i}\n")
        lista_text.insert(tk.END, f"Categoría: {libro['Categoría']}\n")
        lista_text.insert(tk.END, f"Género: {libro['Género']}\n")
        lista_text.insert(tk.END, f"Fecha: {libro['Fecha']}\n")
        lista_text.insert(tk.END, f"Monto: ${libro['Monto']:.2f}\n")
        lista_text.insert(tk.END, "-----------\n")

# Crear una función para limpiar los campos de entrada
def limpiar_campos():
    categoria_var.set(categorias[0])
    genero_femenino_var.set(False)
    genero_masculino_var.set(False)
    fecha_cal.set_date("")  # Restablece la fecha a un valor vacío
    monto_entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Inventario de Libros")

# Crear un Menú desplegable para seleccionar la categoría
categorias = ["Ficción", "No ficción", "Ciencia", "Historia", "Autoayuda"]
categoria_label = tk.Label(root, text="Categoría:")
categoria_label.pack()
categoria_var = tk.StringVar(value=categorias[0])
categoria_menu = ttk.Combobox(root, textvariable=categoria_var, values=categorias)
categoria_menu.pack()

# Crear casillas de verificación para seleccionar el género
genero_label = tk.Label(root, text="Género:")
genero_label.pack()
genero_femenino_var = tk.BooleanVar()
genero_masculino_var = tk.BooleanVar()
genero_femenino_checkbox = tk.Checkbutton(root, text="Femenino", variable=genero_femenino_var)
genero_masculino_checkbox = tk.Checkbutton(root, text="Masculino", variable=genero_masculino_var)
genero_femenino_checkbox.pack()
genero_masculino_checkbox.pack()

# Crear un widget DateEntry para seleccionar la fecha
fecha_label = tk.Label(root, text="Fecha de adquisición:")
fecha_label.pack()
fecha_cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
fecha_cal.pack()

monto_label = tk.Label(root, text="Monto:")
monto_label.pack()
monto_entry = tk.Entry(root)
monto_entry.pack()

agregar_button = tk.Button(root, text="Agregar libro", command=agregar_libro)
agregar_button.pack()

# Crear una área de texto para mostrar la lista de libros
lista_text = tk.Text(root, height=10, width=40)
lista_text.pack()

# Crear una lista para almacenar los libros
inventario = []

root.mainloop()
