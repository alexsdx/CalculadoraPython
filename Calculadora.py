import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("300x450")  # Aumentar altura para la nueva fila
        self.ventana.configure(bg="#f0f0f0")
        
        # Variable para almacenar el primer número, operador y estado
        self.num1 = None
        self.operador = None
        self.esperando_segundo_numero = False
        
        # Campo de entrada para mostrar números y resultados
        self.entry = tk.Entry(ventana, width=15, font=("Arial", 20), bd=5, relief="sunken", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # Botones de la calculadora
        self.crear_botones()
    
    def crear_botones(self):
        # Estilo de botones
        estilo_numero = {"font": ("Arial", 14), "bg": "#4a90e2", "fg": "white", "bd": 2, "relief": "raised"}
        estilo_operador = {"font": ("Arial", 14), "bg": "#f28c38", "fg": "white", "bd": 2, "relief": "raised"}
        estilo_limpiar = {"font": ("Arial", 14), "bg": "#d9534f", "fg": "white", "bd": 2, "relief": "raised"}
        
        # Definir botones en una lista (texto, fila, columna, estilo, comando)
        botones = [
            ("7", 1, 0, estilo_numero, lambda: self.agregar_digito("7")),
            ("8", 1, 1, estilo_numero, lambda: self.agregar_digito("8")),
            ("9", 1, 2, estilo_numero, lambda: self.agregar_digito("9")),
            ("/", 1, 3, estilo_operador, lambda: self.seleccionar_operador("/")),
            ("4", 2, 0, estilo_numero, lambda: self.agregar_digito("4")),
            ("5", 2, 1, estilo_numero, lambda: self.agregar_digito("5")),
            ("6", 2, 2, estilo_numero, lambda: self.agregar_digito("6")),
            ("*", 2, 3, estilo_operador, lambda: self.seleccionar_operador("*")),
            ("1", 3, 0, estilo_numero, lambda: self.agregar_digito("1")),
            ("2", 3, 1, estilo_numero, lambda: self.agregar_digito("2")),
            ("3", 3, 2, estilo_numero, lambda: self.agregar_digito("3")),
            ("-", 3, 3, estilo_operador, lambda: self.seleccionar_operador("-")),
            ("0", 4, 0, estilo_numero, lambda: self.agregar_digito("0")),
            (".", 4, 1, estilo_numero, lambda: self.agregar_digito(".")),
            ("C", 5, 3, estilo_limpiar, self.limpiar),
            ("+", 4, 3, estilo_operador, lambda: self.seleccionar_operador("+")),
            ("=", 4, 2, estilo_operador, self.calcular),
        ]
        
        # Crear y posicionar botones
        for texto, fila, columna, estilo, comando in botones:
            btn = tk.Button(self.ventana, text=texto, command=comando, **estilo)
            btn.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
        
        # Configurar peso de filas y columnas para que los botones se ajusten
        for i in range(6):  # Aumentar a 6 filas
            self.ventana.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.ventana.grid_columnconfigure(i, weight=1)
    
    def agregar_digito(self, digito):
        if self.esperando_segundo_numero:
            self.entry.delete(0, tk.END)
            self.esperando_segundo_numero = False
        current = self.entry.get()
        if digito == "." and "." in current:
            return
        self.entry.insert(tk.END, digito)
    
    def seleccionar_operador(self, operador):
        try:
            self.num1 = float(self.entry.get())
            self.operador = operador
            self.esperando_segundo_numero = True
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido")
    
    def calcular(self):
        try:
            num2 = float(self.entry.get())
            if self.operador == "+":
                resultado = self.num1 + num2
            elif self.operador == "-":
                resultado = self.num1 - num2
            elif self.operador == "*":
                resultado = self.num1 * num2
            elif self.operador == "/":
                if num2 == 0:
                    messagebox.showerror("Error", "No se puede dividir por cero")
                    return
                resultado = self.num1 / num2
            else:
                messagebox.showerror("Error", "Selecciona una operación primero")
                return
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(resultado))
            self.num1 = resultado
            self.operador = None
            self.esperando_segundo_numero = True
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido")
    
    def limpiar(self):
        self.entry.delete(0, tk.END)
        self.num1 = None
        self.operador = None
        self.esperando_segundo_numero = False

# Crear y ejecutar la calculadora
if __name__ == "__main__":
    ventana = tk.Tk()
    app = Calculadora(ventana)
    ventana.mainloop()