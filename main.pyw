import tkinter as tk
from pages.auth_page import AuthPage

class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat App - Tkinter")
        self.geometry("800x600")
        self.resizable(False, False)
        
        # Contenedor principal
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Mostrar la página de autenticación inicialmente
        self.show_auth_page()
    
    def show_auth_page(self):
        auth_page = AuthPage(self.container, self)
        auth_page.grid(row=0, column=0, sticky="nsew")
        auth_page.tkraise()
    
    def show_chat_page(self, username):
        from pages.chat_page import ChatPage
        chat_page = ChatPage(self.container, self, username)
        chat_page.grid(row=0, column=0, sticky="nsew")
        chat_page.tkraise()

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()