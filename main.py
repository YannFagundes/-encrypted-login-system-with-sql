import customtkinter as tk
from banco import verificar_usuario, create_usuario

def validação():
    usuario = entry_user.get()
    senha = entry_passw.get()
    resultado = verificar_usuario(chave=usuario, senha=senha)
    if resultado:
        resultado_login.configure(text="Login bem-sucedido!", text_color="green")
        abrir_nova_janela()  
        login_screen.withdraw()
    else:
        resultado_login.configure(text="Usuário ou senha incorretos.", text_color="red")

def registrando():
    usuario = entry_user.get()
    senha = entry_passw.get()
    resultado = create_usuario(chave=usuario, senha=senha)
    if resultado:
        resultado_login.configure(text="Registro bem-sucedido!", text_color="green")
    else:
        resultado_login.configure(text="Erro ao registrar.", text_color="red")

def abrir_nova_janela():
    nova_janela = tk.CTkToplevel(login_screen) 
    nova_janela.title("Nova Janela")
    nova_janela.geometry("400x300")
    
    nova_janela.protocol("WM_DELETE_WINDOW", lambda: fechar_janelas(nova_janela)) 

    lb_pa = tk.CTkLabel(nova_janela, text="EM CONSTRUÇÃO")
    lb_pa.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")
    lb_pa = tk.CTkLabel(nova_janela, text="Feito por: Yann F.souza")
    lb_pa.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")

def fechar_janelas(nova_janela):
    nova_janela.destroy()
    login_screen.destroy()


login_screen = tk.CTk()
login_screen.title("Sistema de login")
login_screen.geometry("300x300")
login_screen.resizable(False, False)

login_screen.columnconfigure(0, weight=1)


lb_user = tk.CTkLabel(login_screen, text="Usuário:")
lb_user.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

entry_user = tk.CTkEntry(login_screen, placeholder_text="Digite sua chave privada")
entry_user.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

lb_password = tk.CTkLabel(login_screen, text="Senha:")
lb_password.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")



entry_passw = tk.CTkEntry(login_screen, placeholder_text="Digite sua senha", show="*")
entry_passw.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="ew")

frame_botoes = tk.CTkFrame(login_screen, fg_color="transparent")
frame_botoes.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
frame_botoes.columnconfigure(0, weight=1)
frame_botoes.columnconfigure(1, weight=1)

botão_login = tk.CTkButton(frame_botoes, text="Fazer login", command=validação)
botão_login.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

BotãoRegister = tk.CTkButton(frame_botoes, text="Registrar", command=registrando)
BotãoRegister.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

resultado_login = tk.CTkLabel(login_screen, text="")
resultado_login.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

login_screen.mainloop()
