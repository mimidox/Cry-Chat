from tkinter import ttk

def configure_styles():
    style = ttk.Style()
    
    # Configuración general
    style.theme_use("clam")
    
    # Colores
    dark_bg = "#2c2c2c"
    darker_bg = "#1e1e1e"
    accent_color = "#8a2be2"  # Morado
    light_text = "#ffffff"
    dark_text = "#000000"
    entry_bg = "#3c3c3c"
    
    # Estilo para títulos
    style.configure("Title.TLabel", 
                   font=("Arial", 16, "bold"),
                   foreground=light_text,
                   background=dark_bg)
    
    # Estilo para etiquetas normales
    style.configure("Label.TLabel",
                   font=("Arial", 10),
                   foreground=light_text,
                   background=dark_bg)
    
    # Estilo para enlaces
    style.configure("Link.TLabel",
                   font=("Arial", 10, "underline"),
                   foreground=accent_color,
                   background=dark_bg)
    
    # Estilo para entradas de texto
    style.configure("Entry.TEntry",
                   fieldbackground=entry_bg,
                   foreground=light_text,
                   insertcolor=light_text,
                   bordercolor=accent_color,
                   lightcolor=accent_color,
                   darkcolor=accent_color,
                   padding=5)
    
    # Estilo para botones normales
    style.configure("TButton",
                   font=("Arial", 10),
                   foreground=dark_text,
                   background=accent_color,
                   bordercolor=accent_color,
                   focusthickness=3,
                   focuscolor=accent_color,
                   padding=6)
    
    # Estilo para botones de acento (resaltados)
    style.configure("Accent.TButton",
                   font=("Arial", 10, "bold"),
                   foreground=light_text,
                   background=accent_color,
                   bordercolor=accent_color,
                   focusthickness=3,
                   focuscolor=accent_color,
                   padding=8)
    
    # Estilo para el mapa de botones
    style.map("Accent.TButton",
             background=[("active", "#9b30ff"), ("pressed", "#7d26cd")])
    style.map("TButton",
             background=[("active", "#9b30ff"), ("pressed", "#7d26cd")])