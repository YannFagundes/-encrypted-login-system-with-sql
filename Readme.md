# Sistema de Login com Chaves Privadas e Hash de Senhas

Este é um sistema de login simples em Python que utiliza chaves privadas como identificadores de usuário e hash para criptografia de senhas.

## Bibliotecas Utilizadas

-   `sqlalchemy`: Para interação com o banco de dados SQLite.
-   `customtkinter`: Para a interface gráfica do usuário (GUI).
-   `bcrypt`: Para criptografia de senhas usando hash.

## Funcionalidades

-   **Login com Chave Privada**: Os usuários fazem login utilizando suas chaves privadas como identificadores únicos.
-   **Registro Simplificado**: Novos usuários podem se registrar fornecendo uma chave privada e senha.
-   **Criptografia de Senhas**: As senhas são criptografadas usando hash com `bcrypt` para segurança.
-   **Interface Gráfica**: Uma interface simples criada com `customtkinter` para login e registro.
-   **Banco de Dados SQLite**: Os dados dos usuários são armazenados em um banco de dados SQLite local.

## Como Executar

1.  **Instale as dependências**:

    ```bash
    pip install sqlalchemy customtkinter bcrypt
    ```

2.  **Execute o script**:

    ```bash
    python nome_do_seu_script.py
    ```

    (Substitua `nome_do_seu_script.py` pelo nome do arquivo do seu script Python).

## Detalhes Técnicos

-   **Criptografia de Senhas**:
    -      As senhas são criptografadas usando `bcrypt`, que gera um hash único para cada senha, mesmo que senhas iguais sejam usadas.
    -      O `salt` é gerado automaticamente pelo `bcrypt`, aumentando a segurança.
-   **Banco de Dados**:
    -      O sistema utiliza SQLite, um banco de dados leve e fácil de usar, ideal para pequenos projetos.
    -      A biblioteca `sqlalchemy` é usada como um ORM (Object-Relational Mapping) para interagir com o banco de dados de forma mais eficiente.
-   **Interface do Usuário**:
    -      `customtkinter` foi escolhido para criar uma interface moderna e responsiva.
    -   O uso de chaves privadas como login torna o sistema mais seguro em relação a ataques de força bruta, já que chaves privadas são muito mais complexas do que nomes de usuário tradicionais.

## Visão do Projeto

-   **Integração com Web3**:
    -      Plano futuro para integrar a verificação de usuários através da blockchain, utilizando Web3, para aumentar a segurança e descentralização.
-   **Testes de Criptografia**:
    -      Exploração e testes de diferentes métodos de criptografia para garantir a máxima segurança do sistema.

## Código


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
# DATABASE
