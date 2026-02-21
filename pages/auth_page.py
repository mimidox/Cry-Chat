import tkinter as tk
from tkinter import ttk, messagebox
from recursos.styles import configure_styles

class AuthPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        configure_styles()
        
        self.configure(bg="#2c2c2c")
        
        # Frame principal
        main_frame = tk.Frame(self, bg="#2c2c2c", padx=40, pady=40)
        main_frame.pack(expand=True)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="Iniciar Sesión", 
            style="Title.TLabel"
        )
        title_label.pack(pady=(0, 30))
        
        # Formulario
        form_frame = tk.Frame(main_frame, bg="#2c2c2c")
        form_frame.pack()
        
        # Usuario
        user_label = ttk.Label(
            form_frame, 
            text="Usuario:", 
            style="Label.TLabel"
        )
        user_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.user_entry = ttk.Entry(
            form_frame, 
            style="Entry.TEntry",
            width=30
        )
        self.user_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Contraseña
        pass_label = ttk.Label(
            form_frame, 
            text="Contraseña:", 
            style="Label.TLabel"
        )
        pass_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.pass_entry = ttk.Entry(
            form_frame, 
            style="Entry.TEntry",
            show="*",
            width=30
        )
        self.pass_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Botón de inicio de sesión
        login_btn = ttk.Button(
            main_frame, 
            text="Ingresar", 
            style="Accent.TButton",
            command=self.login
        )
        login_btn.pack(pady=20)
        
        # Enlace para registro
        register_label = ttk.Label(
            main_frame, 
            text="¿No tienes cuenta? Regístrate", 
            style="Link.TLabel",
            cursor="hand2"
        )
        register_label.pack()
        register_label.bind("<Button-1>", lambda e: messagebox.showinfo("Registro", "Función de registro no implementada"))
    
    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        
        if username and password:
            self.controller.show_chat_page(username)
        else:
            messagebox.showerror("Error", "Por favor ingresa usuario y contraseña")