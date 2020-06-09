from tkinter import *
expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:

		global expression
		total = str(eval(expression))#Evaluates expression directly so that we don't need to write different or separate functions for evaluation

		equation.set(total)

		expression = ""

	except:

		equation.set(" ERROR ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	PPB = Tk()

	# set the background colour of GUI window
	PPB.configure(background="black")

	# set the title of GUI window
	PPB.title("Simple Calculator")

	# set the configuration of GUI window
	PPB.geometry("350x250")


	equation = StringVar()


	expression_field = Entry(PPB, textvariable=equation)

	expression_field.grid(columnspan=4, ipadx=70)

	equation.set('Enter')

	button1 = Button(PPB, text=' 1 ', fg='black', bg='red',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(PPB, text=' 2 ', fg='black', bg='red',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(PPB, text=' 3 ', fg='black', bg='red',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(PPB, text=' 4 ', fg='black', bg='red',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(PPB, text=' 5 ', fg='black', bg='red',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(PPB, text=' 6 ', fg='black', bg='red',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(PPB, text=' 7 ', fg='black', bg='red',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(PPB, text=' 8 ', fg='black', bg='red',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(PPB, text=' 9 ', fg='black', bg='red',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(PPB, text=' 0 ', fg='black', bg='red',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(PPB, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(PPB, text=' - ', fg='black', bg='red',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(PPB, text=' * ', fg='black', bg='red',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(PPB, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(PPB, text=' = ', fg='black', bg='red',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	Decimal = Button(PPB, text='.', fg='black', bg='red',
					 command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=5, column=1)
	clear = Button(PPB, text='Clear', fg='black', bg='red',
				command=clear, height=1, width=7)
	clear.grid(row=6, column='0')


	PPB.mainloop()
