from tkinter import *
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        result_label.config(text=str(result))

    except ValueError:
        result_label.config(text="Invalid input")

def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    result_label.config(text="")

window = Tk()
window.title("Calculator")
window.config(bg="skyblue")

entry1 = Entry(window, width=20,  font=("Arial", 20, "bold"))
entry1.grid(row=0, column=0, padx=5, pady=5)

operator_var = StringVar()
operator_var.set("+")

operator_dropdown = OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_dropdown.grid(row=1, column=0, padx=5, pady=5)
operator_dropdown.configure(font=("Arial", 15, "bold"), width=5)

clr_btn = Button(window, text="Clear", command=clear, width=5, font=("Arial", 14, "normal"))
clr_btn.grid(row=4, column=1, padx=0, pady=0)

entry2 = Entry(window, width=20, font=("Arial", 20, "bold"))
entry2.grid(row=2, column=0, padx=5, pady=5)


calculate_button = Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, padx=5, pady=5)

result_label = Label(window, text="",  font=("Arial", 20, "bold"), relief="sunken", width=20)
result_label.grid(row=4, column=0, padx=5, pady=5)

window.mainloop()
