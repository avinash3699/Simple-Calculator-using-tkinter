# Python program to create a Simple Calculator GUI using tkinter

#importing everything from tkinter module
from tkinter import *

# creating a GUI window
window = Tk()

# restricting the user to change the dimensions of the window using 'resizable' method
window.resizable(width=FALSE, height=FALSE)

# setting the title of GUI window from default to 'Simple Calculator using tkinter' using 'title' method
window.title("Simple Calculator using tkinter")

# setting the background color using 'configure' method
window.configure(background = "#000000")

# global declaration of 'expression' variable
expression = ""

# function executed when buttons other than 'equal to' and 'clear' is clicked
def clicked(number):
	global expression
	expression += number
	equation.set(expression)

# function to clear the input field
def clear_input_field():
 	equation.set("")
 	global expression
 	expression = ""

#function to calculate the final expression
def calculate():
	global expression

	try:

		# converting an operand if it starts with 0
		final_expression = ""
		for i in expression:
			if i.isdigit(): final_expression += i
			else:operator=i;final_expression += " "
		temp = final_expression.split(" ")
		expression = str(int(temp[0])) + operator + str(int(temp[1]))
	
		# calculating the answer using 'eval' function and displaying it
		result = str(eval(expression))
		equation.set(result)
		expression = ""

	# handling 'ZeroDivisionError' that arises when second operand is zero while dividing
	except ZeroDivisionError:
		equation.set("∞")

	except:
		equation.set("Please Enter a Valid Expression")

equation = StringVar()
equation.set("Enter the expression")
input_ = Entry(window, textvariable = equation,bd=0)
input_.grid(row=0, column=0, columnspan=3)

# creating buttons for numbers, operators and clear(C) using 'Button' function
button_1 = Button(window, text = '1', command = lambda: clicked('1'), height = 2, width = 5)
button_2 = Button(window, text = '2', command = lambda: clicked('2'), height = 2, width = 5)
button_3 = Button(window, text = '3', command = lambda: clicked('3'), height = 2, width = 5)
button_4 = Button(window, text = '4', command = lambda: clicked('4'), height = 2, width = 5)
button_5 = Button(window, text = '5', command = lambda: clicked('5'), height = 2, width = 5)
button_6 = Button(window, text = '6', command = lambda: clicked('6'), height = 2, width = 5)
button_7 = Button(window, text = '7', command = lambda: clicked('7'), height = 2, width = 5)
button_8 = Button(window, text = '8', command = lambda: clicked('8'), height = 2, width = 5)
button_9 = Button(window, text = '9', command = lambda: clicked('9'), height = 2, width = 5)
button_0 = Button(window, text = '0', command = lambda: clicked('0'), height = 2, width = 5)
button_sum = Button(window, text = '+', command = lambda: clicked('+'), height = 2, width = 5)
button_sub = Button(window, text = '-', command = lambda: clicked('-'), height = 2, width = 5)
button_mul = Button(window, text = '*', command = lambda: clicked('*'), height = 2, width = 5)
button_div = Button(window, text = '/', command = lambda: clicked('/'), height = 2, width = 5)
button_equal = Button(window, text = '=', command = lambda: calculate(), height = 2, width = 5)
button_clear = Button(window, text = 'C', command = lambda: clear_input_field(), height = 2, width = 5)
button_point = Button(window, text = '.', command = lambda: clicked('.'), height = 2, width = 5)

# displaying the buttons onto the window and placing them using 'grid' method
button_1.grid(row = 1, column = 0)
button_2.grid(row = 1, column = 1)
button_3.grid(row = 1, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 3, column = 0)
button_8.grid(row = 3, column = 1)
button_9.grid(row = 3, column = 2)
button_point.grid(row = 4, column = 0)
button_0.grid(row = 4, column = 1)
button_equal.grid(row = 4, column = 2)
button_sum.grid(row = 1, column = 3)
button_sub.grid(row = 2, column = 3)
button_mul.grid(row = 3, column = 3)
button_div.grid(row = 4, column = 3)
button_clear.grid(row =0 , column = 3)

# to start the GUI window, 'mainloop' method is used
window.mainloop()