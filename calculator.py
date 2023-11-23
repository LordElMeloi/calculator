from tkinter import Tk, Label, Button, StringVar

class Calculator:
    def __init__(self, window):
        self.equation_text = StringVar()
        self.equation_label = Label(window, textvariable=self.equation_text, bg="white", font=("Arial", 16), width=22, height=2)
        self.equation_label.grid(row=0, column=0, columnspan=5)

        self.create_buttons(window)

    def press_button(self, num):
        current_text = self.equation_text.get()
        if current_text == "Error":
            self.equation_text.set("")
        self.equation_text.set(current_text + str(num))

    def equals(self):
        try:
            result = eval(self.equation_text.get())
            self.equation_text.set(str(result))
        except (ZeroDivisionError, SyntaxError):
            self.equation_text.set("Error")

    def clear_all(self):
        self.equation_text.set("")

    def erase_one(self):
        current_text = self.equation_text.get()
        if current_text:
            self.equation_text.set(current_text[:-1])  # Remove the last character

    def calculate_percentage(self):
        try:
            result = eval(self.equation_text.get()) / 100
            self.equation_text.set(str(result))
        except (ZeroDivisionError, SyntaxError):
            self.equation_text.set("Error")

    def calculate_square_root(self):
        try:
            result = eval(self.equation_text.get()) ** 0.5
            self.equation_text.set(str(result))
        except (ZeroDivisionError, SyntaxError):
            self.equation_text.set("Error")

    def calculate_fraction(self):
        try:
            result = 1 / eval(self.equation_text.get())
            self.equation_text.set(str(result))
        except (ZeroDivisionError, SyntaxError):
            self.equation_text.set("Error")

    def calculate_power_of_two(self):
        try:
            result = eval(self.equation_text.get()) ** 2
            self.equation_text.set(str(result))
        except (ZeroDivisionError, SyntaxError):
            self.equation_text.set("Error")

    def create_buttons(self, window):
        button_layout = [
            ['7', '8', '9', '/', 'Erase'],
            ['4', '5', '6', '*', 'Clear'],
            ['1', '2', '3', '-', '%'],
            ['0', '.', '=', '+', '√']
        ]

        for i, row in enumerate(button_layout):
            for j, button_text in enumerate(row):
                button = Button(window, text=button_text, height=2, width=5, font=("Arial", 16),
                                command=lambda text=button_text: self.button_click(text))
                button.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")

        fraction_button = Button(window, text='1/x', height=2, width=5, font=("Arial", 16), command=self.calculate_fraction)
        fraction_button.grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        power_button = Button(window, text='x^2', height=2, width=5, font=("Arial", 16), command=self.calculate_power_of_two)
        power_button.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

    def button_click(self, text):
        if text == '=':
            self.equals()
        elif text == 'Erase':
            self.erase_one()
        elif text == 'Clear':
            self.clear_all()
        else:
            self.press_button(text)


if __name__ == "__main__":
    window = Tk()
    window.title("Calculator program")
    window.geometry("400x600")

    calculator = Calculator(window)

    window.mainloop()
