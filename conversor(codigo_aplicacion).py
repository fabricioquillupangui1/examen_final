import tkinter as tk
from tkinter import ttk  # Importa ttk para usar Combobox y widgets mejorados

# Crear ventana principal
ventana = tk.Tk()  # Inicializa la ventana principal de Tkinter
ventana.title("Conversor de Sistemas Numéricos")  # Establece el título de la ventana
ventana.geometry("400x620")  # Define el tamaño de la ventana (ancho x alto)
ventana.resizable(False, False)  # Desactiva el cambio de tamaño de la ventana
ventana.configure(bg="#e0f7fa")  # Color de fondo de la ventana

# Variables para manejar el número y el contador de dígitos
numero_actual = tk.StringVar(value="")  # Almacena el número ingresado por el usuario
contador_actual = tk.StringVar(value="0/30")  # Muestra la cantidad de dígitos ingresados
limites = {  # Limites máximos de dígitos por sistema numérico
    "Binario": 30,
    "Octal": 10,
    "Decimal": 9,
    "Hexadecimal": 7
}

# Función para actualizar el contador y mensaje de límite
def actualizar_contador():
    sistema = combo_sistema.get()  # Obtiene el sistema seleccionado en el combobox
    limite = limites.get(sistema, 30)  # Obtiene el límite de dígitos para ese sistema
    actual = len(numero_actual.get())  # Calcula la longitud del número ingresado
    contador_actual.set(f"{actual}/{limite}")  # Actualiza el contador visual
    if actual >= limite:  # Si se alcanza el límite
        mensaje_limite.config(text=" Has alcanzado el límite de dígitos")  # Mostrar mensaje
    else:
        mensaje_limite.config(text="")  # Limpiar mensaje si no hay límite alcanzado

# Función para agregar un carácter al número actual
def agregar_caracter(c):
    sistema = combo_sistema.get()  # Obtiene el sistema seleccionado
    limite = limites.get(sistema, 30)  # Obtiene el límite de dígitos
    actual = numero_actual.get()  # Obtiene el número actual
    if len(actual) < limite:  # Solo agregar si no se supera el límite
        numero_actual.set(actual + c)  # Concatenar el nuevo carácter
        actualizar_contador()  # Actualizar contador y mensaje

# Función para borrar el último carácter
def borrar_uno():
    actual = numero_actual.get()  # Obtiene el número actual
    numero_actual.set(actual[:-1])  # Elimina el último carácter
    actualizar_contador()  # Actualiza el contador

# Función para borrar todo el número y resetear resultados
def borrar_todo():
    numero_actual.set("")  # Vacía la variable del número
    actualizar_contador()  # Actualiza contador a 0
    mensaje_error.config(text="")  # Limpia mensaje de error
    # Reinicia los resultados de conversión
    resultado_decimal.config(text="Decimal: —")
    resultado_binario.config(text="Binario: —")
    resultado_octal.config(text="Octal: —")
    resultado_hex.config(text="Hexadecimal: —")

# Función para habilitar/deshabilitar botones según sistema seleccionado
def actualizar_botones(event=None):
    sistema = combo_sistema.get()  # Sistema seleccionado
    for boton in botones_teclado:  # Itera sobre todos los botones del teclado
        c = boton["text"]  # Obtiene el texto del botón
        activo = False  # Por defecto, botón desactivado
        if sistema == "Binario":
            activo = c in ['0', '1']  # Solo 0 y 1 activos
        elif sistema == "Octal":
            activo = c in [str(i) for i in range(8)]  # 0-7 activos
        elif sistema == "Decimal":
            activo = c in [str(i) for i in range(10)]  # 0-9 activos
        elif sistema == "Hexadecimal":
            activo = True  # Todos activos

        # Configura el estado y color de cada botón
        if activo:
            boton.config(state="normal", relief="raised", fg="white")
            boton.config(bg="#4CAF50" if c.isdigit() else "#FF9800")  # Verde para dígitos, naranja para letras
        else:
            boton.config(state="disabled", relief="flat", bg="#cfd8dc", fg="#555")  # Gris deshabilitado
    borrar_todo()  # Limpia el número al cambiar de sistema

# Crear título de la ventana
titulo = tk.Label(ventana, text="Conversor de Sistemas Numéricos", font=("Arial", 14, "bold"), bg="#e0f7fa")
titulo.pack(pady=10)  # Empaqueta el título con espacio vertical

# Cuadro de entrada para mostrar el número
entry_numero = tk.Entry(ventana, textvariable=numero_actual, font=("Courier", 18), justify="center", state="readonly", readonlybackground="white")
entry_numero.pack(pady=(5, 2), ipady=5, ipadx=5)  # Empaquetado con padding interno

# Contador de caracteres
label_contador = tk.Label(ventana, textvariable=contador_actual, font=("Arial", 10), bg="#e0f7fa")
label_contador.pack()

# Mensaje de límite de dígitos
mensaje_limite = tk.Label(ventana, text="", fg="red", bg="#e0f7fa", font=("Arial", 9, "italic"))
mensaje_limite.pack(pady=(0, 5))

# Frame para selección de sistema
frame_entrada = tk.Frame(ventana, bg="#e0f7fa")
frame_entrada.pack(pady=5)
tk.Label(frame_entrada, text="Sistema:", bg="#e0f7fa").grid(row=0, column=0, padx=5)
sistemas = ["Decimal", "Binario", "Octal", "Hexadecimal"]  # Opciones del combobox
combo_sistema = ttk.Combobox(frame_entrada, values=sistemas, state="readonly")
combo_sistema.current(0)  # Valor inicial Decimal
combo_sistema.grid(row=0, column=1)
combo_sistema.bind("<<ComboboxSelected>>", actualizar_botones)  # Llama función al cambiar sistema

# Frame para botones de caracteres
frame_botones = tk.Frame(ventana, bg="#e0f7fa")
frame_botones.pack(pady=10)

caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'A', 'B', 'C', 'D', 'E', 'F']  # Caracteres del teclado

botones_teclado = []  # Lista para guardar botones
fila = 0
col = 0
for c in caracteres:  # Crear botones dinámicamente
    boton = tk.Button(frame_botones, text=c, width=4, command=lambda c=c: agregar_caracter(c))
    boton.grid(row=fila, column=col, padx=3, pady=3)
    botones_teclado.append(boton)
    col += 1
    if col == 4:  # 4 botones por fila
        col = 0
        fila += 1

# Frame para botones de acciones (AC, borrar, igual)
frame_acciones = tk.Frame(ventana, bg="#e0f7fa")
frame_acciones.pack(pady=10)

boton_ac = tk.Button(frame_acciones, text="AC", command=borrar_todo, bg="#607d8b", fg="white", width=8)
boton_ac.grid(row=0, column=0, padx=5)

boton_borrar = tk.Button(frame_acciones, text="←", command=borrar_uno, bg="#f44336", fg="white", width=8)
boton_borrar.grid(row=0, column=1, padx=5)

boton_igual = tk.Button(frame_acciones, text="=", command=lambda: convertir(), bg="#9C27B0", fg="white", width=8)
boton_igual.grid(row=0, column=2, padx=5)

# Etiqueta para mostrar errores
mensaje_error = tk.Label(ventana, text="", fg="red", bg="#e0f7fa")
mensaje_error.pack()

# Frame para mostrar resultados de conversión
frame_resultados = tk.Frame(ventana, bg="#e0f7fa")
frame_resultados.pack(pady=10)

resultado_decimal = tk.Label(frame_resultados, text="Decimal: —", bg="#e0f7fa", font=("Arial", 10))
resultado_decimal.pack(pady=2)

resultado_binario = tk.Label(frame_resultados, text="Binario: —", bg="#e0f7fa", font=("Arial", 10))
resultado_binario.pack(pady=2)

resultado_octal = tk.Label(frame_resultados, text="Octal: —", bg="#e0f7fa", font=("Arial", 10))
resultado_octal.pack(pady=2)

resultado_hex = tk.Label(frame_resultados, text="Hexadecimal: —", bg="#e0f7fa", font=("Arial", 10))
resultado_hex.pack(pady=2)

# Función para convertir el número al resto de sistemas
def convertir():
    numero_str = numero_actual.get()  # Número ingresado
    sistema = combo_sistema.get()  # Sistema seleccionado

    try:
        # Convertir a decimal según sistema
        if sistema == "Decimal":
            decimal = int(numero_str)
        elif sistema == "Binario":
            decimal = int(numero_str, 2)
        elif sistema == "Octal":
            decimal = int(numero_str, 8)
        elif sistema == "Hexadecimal":
            decimal = int(numero_str, 16)
        else:
            raise ValueError()

        # Mostrar u ocultar etiquetas según sistema origen
        if sistema != "Decimal":
            resultado_decimal.config(text=f"Decimal: {decimal}")
            resultado_decimal.pack(pady=2)
        else:
            resultado_decimal.pack_forget()

        if sistema != "Binario":
            resultado_binario.config(text=f"Binario: {bin(decimal)[2:].zfill(6)}")
            resultado_binario.pack(pady=2)
        else:
            resultado_binario.pack_forget()

        if sistema != "Octal":
            resultado_octal.config(text=f"Octal: {oct(decimal)[2:]}")
            resultado_octal.pack(pady=2)
        else:
            resultado_octal.pack_forget()

        if sistema != "Hexadecimal":
            resultado_hex.config(text=f"Hexadecimal: {hex(decimal)[2:].upper()}")
            resultado_hex.pack(pady=2)
        else:
            resultado_hex.pack_forget()

        mensaje_error.config(text="")  # Limpiar mensaje de error

    except ValueError:
        # Mostrar guiones si el número es inválido
        resultado_decimal.config(text="Decimal: —")
        resultado_decimal.pack(pady=2)
        resultado_binario.config(text="Binario: —")
        resultado_binario.pack(pady=2)
        resultado_octal.config(text="Octal: —")
        resultado_octal.pack(pady=2)
        resultado_hex.config(text="Hexadecimal: —")
        resultado_hex.pack(pady=2)
        mensaje_error.config(text=" Número inválido para el sistema seleccionado.")

# Inicializar botones y contador al iniciar
actualizar_botones()
actualizar_contador()

# Ejecutar la ventana
ventana.mainloop()
