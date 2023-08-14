import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

# armazenar senhas
pwd_history = []


def generate_pwd(size=12):
    char = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(char) for _ in range(size))
    return pwd


def generate_and_show():
    pwd_size = int(size_entry.get())
    if pwd_size < 1:
        messagebox.showerror("Erro", "Digite um tamanho válido para a senha.")
        return

    generated_pwd = generate_pwd(pwd_size)
    pwd_label.config(text="Senha gerada: " + generated_pwd)

    # copiar a senha para a área de transferência
    pyperclip.copy(generated_pwd)
    messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência.")

    # adicionar ao historico
    pwd_history.append(generated_pwd)

    # manter as 5 senhas geradas
    if len(pwd_history) > 5:
        pwd_history.pop(0)

    update_history()


def update_history():
    history_text.config(state=tk.NORMAL)
    history_text.delete(1.0, tk.END)
    for pwd in pwd_history:
        history_text.insert(tk.END, pwd + "\n")
    history_text.config(state=tk.DISABLED)


# configuração da janela
root = tk.Tk()
root.title("PassKeeper")

title_label = tk.Label(root, text="PassKeeper", font=("Helvetica", 16))
title_label.pack(pady=10)

size_label = tk.Label(root, text="Tamanho da senha:")
size_label.pack()

size_entry = tk.Entry(root)
size_entry.pack()

gerar_button = tk.Button(root, text="Gerar Senha", command=generate_and_show)
gerar_button.pack(pady=10)

pwd_label = tk.Label(root, text="", font=("Helvetica", 12))
pwd_label.pack()

history_label = tk.Label(root, text="Últimas 5 senhas geradas:")
history_label.pack()

history_text = tk.Text(root, height=5, width=40, state=tk.DISABLED)
history_text.pack()

# abrir a interface gráfica
root.mainloop()