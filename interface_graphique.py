from tkinter import *
import tkinter as tk 
from tkinter.messagebox import showinfo

#WINDOW CHARACTERISTIQUE
window=Tk()
window.title("Vérification de la syntaxe d'une expression mathématique simple")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("EPSILON.ico")
window.config(bg='#4065A4')

#MENUBAR
def alert():
    showinfo("alerte", "Created by Othman el fessak HHHH !")
menubar = Menu(window)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=window.quit)
menubar.add_cascade(label="Fichier", menu=menu1)
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)
window.config(menu=menubar)


l = LabelFrame(window, text="Bienvenue", font=("Courrier", 25), bg='#4065A4', fg='White', padx=20, pady=20)
l.pack(fill="both", expand="yes")
Label(l, text="Veuillez saisir une expression mathématique", font=("Courrier", 25), bg='#4065A4', fg='White').pack()


r = StringVar()
value = StringVar()
entree = Entry(l, textvariable=value, font=("Courrier", 20), fg='#4065A4', bg='White', width=30)
entree.pack(expand="yes", anchor=CENTER)

def create_stack():
    return []

def empiler(x, stack):
    stack.append(x)

def depiler(stack):
    return stack.pop()

def height(stack):
    return len(stack)

def is_empty(stack):
    return height(stack)==0

def sommet(stack):
    return stack[-1]

def verify():
    exp=value.get()
    p=create_stack()
    for i in range(len(exp)):
        if exp[i]=='(':
            empiler(i, p)
        elif exp[i]==')':
            if is_empty(p):
                r.set(") à l'indice "+str(i)+" n'est pas ouverte !")
                empiler(i, p)                                                      # here
            else:
                j=depiler(p)
                r.set("Parenthése {} et {} correct".format(i,j))
    if is_empty(p):
        r.set("Parenthésage valide")
    else:
        r.set("à l'indice "+str(sommet(p))+" n'est pas fermée !")
    showinfo("Résultats", resultat.get())
resultat = Entry(l, textvariable=r, font=("Courrier", 20), fg='#4065A4', bg='White', width=30)


bouton = Button(l, text="Test", font=("Courrier", 20), fg='#4065A4', bg='White',  command=lambda:verify())
bouton.pack(expand="yes", anchor=CENTER)

window.mainloop()
