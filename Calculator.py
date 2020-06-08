from tkinter import *

# CONFIG DETAILS

root = Tk()
root.title("Calculator")
display = Entry(root, width = 35, borderwidth = 5)
display.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

# INITIAL STATS

running_total = 0
old_additive_operator = "+"
current_additive_operator = "+"

running_subtotal = 0
old_multiplicative_operator = None
current_multiplicative_operator = None

current_number = 0

display.insert(0, 0)

"""
CURRENT: 

This version can perform basic arithmetic.

It also cannot handle division by 0 yet (probably would crash), and there is no
button to change sign, you have to create negative numbers manually.
"""

# MAIN METHODS

def updateDisplay(input_value):
    global current_number

    old_content = str(display.get())

    if input_value != "." and old_content == "0":
        old_content = old_content[1:]
        output = str(old_content) + str(input_value)
    else:
        output = str(old_content) + str(input_value)

    display.delete(0, END)
    display.insert(0, output)
    current_number = float(output)

def add():
    global old_multiplicative_operator
    global running_subtotal
    global current_number
    global current_multiplicative_operator
    global old_additive_operator
    global current_additive_operator
    global running_total

    display.delete(0, END)
    if current_multiplicative_operator == None:
        running_subtotal += current_number
    elif current_multiplicative_operator == "*":
        running_subtotal *= current_number
    else:
        running_subtotal /= current_number
    old_multiplicative_operator = None
    current_multiplicative_operator = None

    if current_additive_operator == "+":
        running_total += running_subtotal
    else:
        running_total -= running_subtotal
    running_subtotal = 0

    old_additive_operator = current_additive_operator
    current_additive_operator = "+"
    
def subtract():
    global old_multiplicative_operator
    global running_subtotal
    global current_number
    global current_multiplicative_operator
    global old_additive_operator
    global current_additive_operator
    global running_total

    display.delete(0, END)
    if current_multiplicative_operator == None:
        running_subtotal += current_number
    elif current_multiplicative_operator == "*":
        running_subtotal *= current_number
    else:
        running_subtotal /= current_number
    old_multiplicative_operator = None
    current_multiplicative_operator = None

    if current_additive_operator == "+":
        running_total += running_subtotal
    else:
        running_total -= running_subtotal
    running_subtotal = 0

    old_additive_operator = current_additive_operator
    current_additive_operator = "-"
    
def multiply():
    global old_multiplicative_operator
    global current_multiplicative_operator
    global running_subtotal
    global current_number

    display.delete(0, END)

    if current_multiplicative_operator == None:
        running_subtotal += current_number
    elif current_multiplicative_operator == "*":
        running_subtotal *= current_number
    else:
        """
        insert something here for division by 0
        """
        running_subtotal /= current_number
    
    old_multiplicative_operator = current_multiplicative_operator
    current_multiplicative_operator = "*"
    
def divide():
    global old_multiplicative_operator
    global current_multiplicative_operator
    global running_subtotal
    global current_number

    display.delete(0, END)

    if current_multiplicative_operator == None:
        running_subtotal += current_number
    elif current_multiplicative_operator == "*":
        running_subtotal *= current_number
    else:
        """
        insert something here for division by 0
        """
        running_subtotal /= current_number
    
    old_multiplicative_operator = current_multiplicative_operator
    current_multiplicative_operator = ":"
        
def equals():
    global old_multiplicative_operator
    global running_subtotal
    global current_number
    global current_multiplicative_operator
    global old_additive_operator
    global running_total
    global current_additive_operator

    display.delete(0, END)
    if current_multiplicative_operator == None:
        running_subtotal += current_number
    elif current_multiplicative_operator == "*":
        running_subtotal *= current_number
    else:
        """
        put a try/catch here: "DIVISION BY 0 ERROR"
        """
        running_subtotal /= current_number
    old_multiplicative_operator = None
    current_multiplicative_operator = None

    if current_additive_operator == "+":
        running_total += running_subtotal
    else:
        running_total -= running_subtotal
    running_subtotal = 0

    old_additive_operator = "+"
    current_additive_operator = "+"
    output = None
    
    if int(running_total) == float(running_total):
        output = int(running_total)
    else:
        output = running_total
    running_total = 0
    display.insert(0, output)
    current_number = float(output)

def clearDisplay():
    global running_total
    global old_additive_operator
    global current_additive_operator
    global running_subtotal
    global old_multiplicative_operator
    global current_multiplicative_operator
    global current_number

    running_total = 0
    old_additive_operator = "+"
    current_additive_operator = "+"

    running_subtotal = 0
    old_multiplicative_operator = None
    current_multiplicative_operator = None

    current_number = 0

    display.delete(0, END)
    display.insert(0, 0)

# FURTHER CONFIG DETAILS

button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: updateDisplay(0))
button0.grid(row = 4, column = 0)

button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: updateDisplay(1))
button1.grid(row = 3, column = 0)

button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: updateDisplay(2))
button2.grid(row = 3, column = 1)

button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: updateDisplay(3))
button3.grid(row = 3, column = 2)

button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: updateDisplay(4))
button4.grid(row = 2, column = 0)

button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: updateDisplay(5))
button5.grid(row = 2, column = 1)

button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: updateDisplay(6))
button6.grid(row = 2, column = 2)

button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: updateDisplay(7))
button7.grid(row = 1, column = 0)

button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: updateDisplay(8))
button8.grid(row = 1, column = 1)

button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: updateDisplay(9))
button9.grid(row = 1, column = 2)

button_point = Button(root, text = ".", padx = 40, pady = 20, command = lambda: updateDisplay("."))
button_point.grid(row = 6, column = 1)

button_plus = Button(root, text = "+", padx = 39, pady = 20, command = add)
button_plus.grid(row = 5, column = 0)

button_minus = Button(root, text = "-", padx = 39, pady = 20, command = subtract)
button_minus.grid(row = 5, column = 2)

button_times = Button(root, text = "*", padx = 39, pady = 20, command = multiply)
button_times.grid(row = 5, column = 1)

button_divided_by = Button(root, text = ":", padx = 39, pady = 20, command = divide)
button_divided_by.grid(row = 6, column = 0)

button_equals = Button(root, text = "=", padx = 39, pady = 20, command = equals)
button_equals.grid(row = 6, column = 2)

button_clear = Button(root, text = "Clear", padx = 79, pady = 20, command = clearDisplay)
button_clear.grid(row = 4, column = 1, columnspan = 2)

# FINAL SETTINGS

root.mainloop()
