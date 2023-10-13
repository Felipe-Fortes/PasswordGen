import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("400x500")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Gerador De Senha", font=("Roboto", 24))
label.pack(pady=12, padx=10)

checkboxupper = customtkinter.CTkCheckBox(master=frame, text="Letras Maiusculas")
checkboxupper.pack(pady=12, padx=10)

checkboxlower = customtkinter.CTkCheckBox(master=frame, text="Letras Minusculas")
checkboxlower.pack(pady=12, padx=10)

checkboxnums = customtkinter.CTkCheckBox(master=frame, text="Numeros")
checkboxnums.pack(pady=12, padx=10)

checkboxespec = customtkinter.CTkCheckBox(master=frame, text="Caracteres Especiais")
checkboxespec.pack(pady=12, padx=10)

cascatelenght = customtkinter.CTkOptionMenu(master=frame, values=["Tamanho Das Senhas","1"])
cascatelenght.pack(pady=12, padx=10)


cascateamount = customtkinter.CTkOptionMenu(master=frame, values=["Quantas Senhas Serao Geradas","1"])
cascateamount.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Gerar Senhas")
button.pack(pady=12, padx=10)

root.mainloop()