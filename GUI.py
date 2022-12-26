from tkinter import *
from tkinter.messagebox import showinfo
import os

# STACK
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

OPENING_PARENTHESES = ['(', '[', '{', '<']
CLOSING_PARENTHESES = [')', ']', '}', '>']

# WINDOW CHARACTERISTICS
window = Tk()
window.title("Expression Syntax Checker")
window.geometry("1080x720")
window.minsize(800, 450)
window.iconbitmap("assets/icon.ico")
window.config(bg="#363537")

# MENUBAR

def new_window():
    os.system("python GUI.py")

def help():
    showinfo("Help", "This is a simple syntax checker for mathematical expressions. \n"
        "It checks if the expression is valid or not by checking if the parentheses are balanced.\n\n"
        "Syntax: \n"
        "1. The expression must be written in infix notation.\n"
        "2. The expression may contain numbers, alphabets, and various operators.\n"
        "3. The expression must contain only parentheses: (), [], {}, <>"
    )
    
def about():
    showinfo("About", "Made with passion by two 'Fessaka' at CPGE Salmane AL Farissi " + chr(0x00A9) + " 2021")

def copy():
    window.clipboard_clear()
    window.clipboard_append(input_entry.selection_get())
    return "break"

def paste():
    input_entry.insert("insert", window.clipboard_get())
    return "break"

def cut():
    window.clipboard_clear()
    window.clipboard_append(input_entry.selection_get())
    input_entry.delete("sel.first", "sel.last")
    return "break"

def select_all():
    input_entry.select_range(0, 'end')
    return "break"

menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New", command=new_window)
menu1.add_separator()
menu1.add_command(label="Copy", command=copy)
menu1.add_command(label="Cut", command=cut)
menu1.add_command(label="Paste", command=paste)
menubar.add_cascade(label="File", menu=menu1)
menu1.add_separator()
menu1.add_command(label="Quit", command=window.quit)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Help", command=help)
menubar.add_cascade(label="Help", menu=menu2)
window.config(menu=menubar)

menu3 = Menu(menubar, tearoff=0)
menubar.add_command(label="About", command=about)
window.config(menu=menubar)

# Callback function to display the context menu
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

# Create the context menu
context_menu = Menu(window, tearoff=0)
context_menu.add_command(label="Copy", command=copy)
context_menu.add_command(label="Cut", command=cut)
context_menu.add_command(label="Paste", command=paste)
context_menu.add_separator()
context_menu.add_command(label="Select All", command=select_all)

#Main frame
main_frame = LabelFrame(window, bd=0, font=("Trebuchet MS", 25), bg='#363537', fg='White', padx=20, pady=20)
main_frame.pack(expand=True, anchor=CENTER)

# HEADER
header_frame = Frame(main_frame, bg="#363537", padx=20, pady=20)
header_frame.pack(fill="x")

header_label = Label(header_frame, text="Welcome to the Expression Syntax Checker", font=("Trebuchet MS", 25), bg="#363537", fg="white")
header_label.pack(side="top", fill="x")

subheader_label = Label(header_frame, text="Enter a mathematical expression to check its syntax", font=("Trebuchet MS", 20), bg="#363537", fg="white")
subheader_label.pack(side="top", fill="x")

# INPUT
input_frame = Frame(main_frame, bg="#363537", padx=20, pady=20)
input_frame.pack(fill="x")


# Create the entry widget and bind the right mouse button click event to the callback function
input_var = StringVar()
input_entry = Entry(input_frame, textvariable=input_var, font=("Trebuchet MS", 20), fg="black", bg="white", width=30)
input_entry.bind("<Button-3>", show_context_menu)
input_entry.pack(expand=True, anchor=CENTER)


# RESULT
result_var = StringVar()
result_frame = Frame(main_frame, bg="#363537", padx=20, pady=20)
result_frame.pack(fill="x")

result_label = Label(result_frame, textvariable=result_var, font=("Trebuchet MS", 20), bg="#363537", fg="white")
result_label.pack(expand=True, anchor=CENTER)

# SYNTAX CHECK
def verify():
    result_var.set(chr(0x2714) + " Valid Syntax")
    exp=input_var.get()
    p=create_stack()
    for i in range(len(exp)):
        if exp[i] in OPENING_PARENTHESES:
            empiler(i, p)
        elif exp[i] in CLOSING_PARENTHESES:
            if is_empty(p):
                result_var.set(chr(0x274C) + f'  Invalid Syntax: \nA closing parenthesis at index {i+1} is not opened!\nConsider adding an opening parenthesis before this position')
                break
            else:
                j=depiler(p)
        if is_empty(p):
            result_var.set(chr(0x2714) + " Valid Syntax")
        else:
            result_var.set(chr(0x274C) + f' Invalid Syntax: \nAn opening parenthesis at index {sommet(p)+1} is not closed!\nConsider adding a closing parenthesis after this position')

#Clears the input field
def clear_input():
    input_var.set("")
    result_var.set("")

# BUTTON
button_frame = Frame(main_frame, bg="#363537", padx=20, pady=20)
button_frame.pack(fill="x")

# Use grid to position the buttons
Check_button = Button(button_frame, text="Verify", bd=1, bg='#696969', fg='white',
                    font=('Helvetica', 17, 'bold'), relief=FLAT, command=verify)
Check_button.grid(row=0, column=0, ipadx=5, padx=5, sticky=E)  # Set padx to add space between buttons

# Another Button for Reset Entry
Clear_button = Button(button_frame, text="Clear", bd=1, bg='#696969', fg='white',
                    font=('Helvetica', 17, 'bold'),relief=FLAT, command=clear_input)
Clear_button.grid(row=0, column=1, ipadx=5, sticky=W)

# Center the buttons in the window
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)


# FOOTER
footer_frame = Frame(main_frame, bg="#363537", padx=20, pady=20)
footer_frame.pack(fill="x")

footer_label = Label(footer_frame, text="Made with passion by two 'Fessaka' at CPGE Salmane AL Farissi " + chr(0x00A9) + " 2021", font=("Trebuchet MS", 15), bg="#363537", fg="white")
footer_label.pack(side="bottom", fill="x")

window.mainloop()
