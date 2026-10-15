import tkinter as tk
from tkinter import messagebox

class PilaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pila Gráfica")
        self.geometry("300x480")
        self.pila = []

        # Controles
        self.e = tk.Entry(self, font=("Arial", 12), justify="center"); self.e.pack(pady=10)
        tk.Button(self, text="Push (Apilar)", bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), command=self.push).pack(fill="x", padx=40, pady=2)
        tk.Button(self, text="Pop (Desapilar)", bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), command=self.pop).pack(fill="x", padx=40, pady=2)

        # Lienzo gráfico
        self.c = tk.Canvas(self, width=200, height=320, bg="white", highlightthickness=1, highlightbackground="gray")
        self.c.pack(pady=10)

    def actualizar(self):
        self.c.delete("all")
        # Contenedor gráfico
        self.c.create_line(40, 20, 40, 300, 160, 300, 160, 20, width=3, fill="#34495e")
        
        for i, val in enumerate(self.pila):
            y = 260 - (i * 45)
            color = "#e67e22" if i == len(self.pila) - 1 else "#3498db"
            self.c.create_rectangle(45, y, 155, y + 40, fill=color, outline="black")
            self.c.create_text(100, y + 20, text=str(val), fill="white", font=("Arial", 11, "bold"))

    def push(self):
        val = self.e.get().strip()
        if not val: return messagebox.showwarning("Aviso", "Ingresa un valor")
        if len(self.pila) >= 6: return messagebox.showerror("Error", "¡Pila Llena (Overflow)!")
        self.pila.append(val)
        self.e.delete(0, tk.END)
        self.actualizar()

    def pop(self):
        if not self.pila: return messagebox.showerror("Error", "¡Pila Vacía (Underflow)!")
        self.pila.pop()
        self.actualizar()

if __name__ == "__main__":
    PilaApp().mainloop()