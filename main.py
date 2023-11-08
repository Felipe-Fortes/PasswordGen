import customtkinter
import random

customtkinter.FontManager.load_font("Torus Notched SemiBold.ttf")
customtkinter.FontManager.load_font("Akira-Expanded-Demo.ttf")

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

#funçoes
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

def lenghtdef():
    global lenghtq

root = customtkinter.CTk()
root.geometry("600x750")

def generate():
    all =""
    if upperq:
        all += uppercase
    if lowerq:
        all += lowercase
    if numsq:
        all += numbers
    if especq:
        all += especial

    lenght = int(cascatelenght.get())
    amount = int(cascateamount.get())

    passwords = []
    for x in range(amount):
        password = "".join(random.sample(all, lenght))
        passwords.append(password)
    
    textbox.delete("1.0","end")

    for password in passwords:
        textbox.insert("end", password + "\n")

def checkbutton():
    if upperq == False and lowerq == False and numsq == False and especq == False or cascatelenght.get() == "0" or cascateamount.get() == "0":
        button.configure(state="disabled")
    else:
        button.configure(state="normal")
    root.after(100,checkbutton)

#visual
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=25, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Gerador De Senhas", font=("AkiraExpanded-SuperBold", 30))
label.pack(pady=12, padx=10)

checkboxupper = customtkinter.CTkCheckBox(master=frame, text="Letras Maiusculas     ", command = upperdef)
checkboxupper.pack(pady=10, padx=10)

checkboxlower = customtkinter.CTkCheckBox(master=frame, text="Letras Minusculas     ", command = lowerdef)
checkboxlower.pack(pady=10, padx=10)

checkboxnums = customtkinter.CTkCheckBox(master=frame, text="Numeros                      ", command = numsdef)
checkboxnums.pack(pady=10, padx=10)

checkboxespec = customtkinter.CTkCheckBox(master=frame, text="Caracteres Especiais", command = especdef)
checkboxespec.pack(pady=10, padx=10)

labellennght = customtkinter.CTkLabel(master=frame, text="TAMANHO DAS SENHAS", font=("Torus Notched SemiBold", 16))
labellennght.pack(pady=12, padx=10)

cascatelenght = customtkinter.CTkOptionMenu(master=frame, values=["0","1","2","3","4","5","6","7","8","9","10"])
cascatelenght.pack(pady=12, padx=10)

labelamount = customtkinter.CTkLabel(master=frame, text="QUANTAS SENHAS DEVEM SER GERADAS?", font=("Torus Notched SemiBold", 16))
labelamount.pack(pady=12, padx=10)

cascateamount = customtkinter.CTkOptionMenu(master=frame, values=["0","1","2","3","4","5"])
cascateamount.pack(pady=12, padx=10)
    
button = customtkinter.CTkButton(master=frame, text="GERAR SENHAS", command=generate, state="disabled")
button.pack(pady=12, padx=10)

textbox = customtkinter.CTkTextbox(master=frame, height=200, width=200, font=("", 20))
textbox.pack(pady=12, padx=10)

root.after(100, checkbutton)
root.mainloop()