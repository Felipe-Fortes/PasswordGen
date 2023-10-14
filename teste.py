import customtkinter
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
especial = "!@#%&*()+={}[]?/:;><.,-_"

upperq = False
lowerq = False
numsq = False
especq = False


def upperdef():
    global upperq
    if checkboxupper.get() == 1:
        upperq = True
    else:
        upperq = False

def lowerdef():
    global lowerq
    if checkboxlower.get() == 1:
        lowerq = True
    else:
        lowerq = False

def numsdef():
    global numsq
    if checkboxnums.get() == 1:
        numsq = True
    else:
        numsq = False

def especdef():
    global especq
    if checkboxespec.get() == 1:
        especq = True
    else:
        especq = False

root = customtkinter.CTk()
root.geometry("400x500")

def gerar():
    all =""
    if upperq:
        all += uppercase
    if lowerq:
        all += lowercase
    if numsq:
        all += numbers
    if especq:
        all += especial

    print(all)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Gerador De Senha", font=("Roboto", 24))
label.pack(pady=12, padx=10)

checkboxupper = customtkinter.CTkCheckBox(master=frame, text="Letras Maiusculas", command = upperdef)
checkboxupper.pack(pady=12, padx=10)

checkboxlower = customtkinter.CTkCheckBox(master=frame, text="Letras Minusculas", command = lowerdef)
checkboxlower.pack(pady=12, padx=10)

checkboxnums = customtkinter.CTkCheckBox(master=frame, text="Numeros", command = numsdef)
checkboxnums.pack(pady=12, padx=10)

checkboxespec = customtkinter.CTkCheckBox(master=frame, text="Caracteres Especiais", command = especdef)
checkboxespec.pack(pady=12, padx=10)

cascatelenght = customtkinter.CTkOptionMenu(master=frame, values=["Tamanho Das Senhas","1"])
cascatelenght.pack(pady=12, padx=10)


cascateamount = customtkinter.CTkOptionMenu(master=frame, values=["Quantas Senhas Serao Geradas","1"])
cascateamount.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Gerar Senhas", command=gerar)
button.pack(pady=12, padx=10)

root.mainloop()