import tkinter.messagebox

from gerasenha import gerasenha, substituicao
import tkinter as tk

def mostrarsenha():
    senha = gerasenha()
    mensagem2.config(text=f"{senha}")

# Janela Principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("Diceware Password Generator")
janela.configure(bg='#191970')


mensagem = tk.Label(janela, text="DICEWARE PASSWORD GENERATOR", font=("Arial", 12), fg="lightblue", bg = "#191970")
mensagem.pack(pady=20)


botao = tk.Button(janela, text="Criar senha", command=mostrarsenha, width= 40, height=2)
botao.pack(pady=30)

mensagem2 = tk.Label(janela, text="", font=("Arial", 12), fg="black", relief="raised", bg="white")
mensagem2.pack(pady=10, padx=5  )


janela.mainloop()
