import tkinter as tk

# 1 - Criar a Janela
windows = tk.Tk()
windows.geometry("300x150")
windows.title("Gerencia Frases")


# 2 - Criar um Frame
frame = tk.Frame(windows)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionar um Label
label = tk.Label(frame, text=" ")
label.pack(fill='x', expand=True)

# 4 - Adicionando o input text
frase_lab = tk.Label(frame, text="Frase:")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Funcionalidade do botão
def click():
    label.config(text=frase_inp.get())
    frase_inp.delete(0, tk.END)  # Limpa o campo de entrada após clicar no botão

# 6 - Adicionando o botão
button = tk.Button(frame, text="Adicionar Frase", command=click)
button.pack()




windows.mainloop()