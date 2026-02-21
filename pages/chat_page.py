import tkinter as tk
from tkinter import ttk, scrolledtext
from recursos.styles import configure_styles

class ChatPage(tk.Frame):
    def __init__(self, parent, controller, username):
        super().__init__(parent)
        self.controller = controller
        self.username = username
        configure_styles()
        
        self.configure(bg="#2c2c2c")
        
        # Frame principal
        self.main_frame = tk.Frame(self, bg="#2c2c2c")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Barra superior
        top_bar = tk.Frame(self.main_frame, bg="#3c3c3c")
        top_bar.pack(fill="x", pady=(0, 10))
        
        user_label = ttk.Label(
            top_bar, 
            text=f"Usuario: {self.username}", 
            style="Label.TLabel"
        )
        user_label.pack(side="left", padx=10, pady=5)
        
        logout_btn = ttk.Button(
            top_bar, 
            text="Cerrar Sesión", 
            style="Accent.TButton",
            command=lambda: controller.show_auth_page()
        )
        logout_btn.pack(side="right", padx=10, pady=5)
        
        # Área de chat
        self.chat_area = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            state="disabled",
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            font=("Arial", 10),
            padx=10,
            pady=10
        )
        self.chat_area.pack(fill="both", expand=True)
        
        # Frame de entrada de mensaje
        input_frame = tk.Frame(self.main_frame, bg="#2c2c2c")
        input_frame.pack(fill="x", pady=(10, 0))
        
        self.message_entry = ttk.Entry(
            input_frame, 
            style="Entry.TEntry"
        )
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.message_entry.bind("<Return>", lambda e: self.send_message())
        
        send_btn = ttk.Button(
            input_frame, 
            text="Enviar", 
            style="Accent.TButton",
            command=self.send_message
        )
        send_btn.pack(side="right")
        
        # Mensaje de bienvenida
        self.add_message("Sistema", f"Bienvenido al chat, {self.username}!")
    
    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.add_message(self.username, message)
            self.message_entry.delete(0, tk.END)
    
    def add_message(self, sender, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)