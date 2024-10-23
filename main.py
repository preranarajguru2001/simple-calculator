import customtkinter as ctk

root = ctk.CTk()
root.title("Calculator")
root.geometry("350x470")
root.resizable(False, False)
root.configure(bg="#17161b")

# Use the .ico file for the window icon
root.iconbitmap("Calculator_31111.ico")  # Make sure the icon is in the same directory as this script

equation = ""

def show(value):
    global equation
    equation += value
    label_result.configure(text=equation)

def clear():
    global equation
    equation = ""
    label_result.configure(text=equation)

def clearone():
    global equation
    equation = equation[:-1]
    label_result.configure(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.configure(text=result)

label_result = ctk.CTkLabel(root, width=300, height=50, text="", font=('arial', 30), text_color="white")
label_result.pack(pady=20)

def create_button(text, command, x, y):
    return ctk.CTkButton(root, text=text, width=70, height=70, border_width=0, corner_radius=15, font=("arial", 20, 'bold'),
                         fg_color="#2a2b36", text_color="#fff", hover_color="#fe9037", command=command).place(x=x, y=y)

create_button("AC", clear, 9, 80)
create_button("C", clearone, 95, 80)
create_button("/", lambda: show("/"), 183, 80)
create_button("%", lambda: show("%"), 270, 80)
create_button("*", lambda: show("*"), 270, 160)

create_button("7", lambda: show("7"), 9, 160)
create_button("8", lambda: show("8"), 95, 160)
create_button("9", lambda: show("9"), 183, 160)
create_button("-", lambda: show("-"), 270, 240)

create_button("4", lambda: show("4"), 9, 240)
create_button("5", lambda: show("5"), 95, 240)
create_button("6", lambda: show("6"), 183, 240)
create_button("+", lambda: show("+"), 270, 319)

create_button("1", lambda: show("1"), 9, 319)
create_button("2", lambda: show("2"), 95, 319)
create_button("3", lambda: show("3"), 183, 319)

ctk.CTkButton(root, text="0", width=160, height=70, border_width=0, corner_radius=15, font=("arial", 20, 'bold'),
              fg_color="#2a2b36", text_color="#fff", hover_color="#fe9037", command=lambda: show("0")).place(x=9, y=396)

create_button(".", lambda: show("."), 185, 396)
create_button("=", calculate, 270, 396)

root.mainloop()
