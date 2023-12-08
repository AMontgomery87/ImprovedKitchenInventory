from tkinter import*

root1 = Tk()
root1.geometry("500x500")
root1.title("Kitchen Inventory Helper")



def cookButtonClick():
    return

def recipeButtonClick():
    return

def receiveButtonClick():
    return

def availableButtonClick():
    return

def yesButtonClick():
    return

def noButtonClick():
    return



cook_button = Button(root1, text="Cook", padx=40, pady=20)
cook_button.grid(row=5, column=0, columnspan=1, )

recipe_button = Button(root1, text="Recipe", padx=40, pady=20)
recipe_button.grid(row=5, column=2, columnspan=1, )

receive_button = Button(root1, text="Receive", padx=30, pady=20)
receive_button.grid(row=6, column=0, columnspan=1, )

available_button = Button(root1, text="Available", padx=35, pady=20)
available_button.grid(row=5, column=1, columnspan=1, )

yes_button = Button(root1, text="Yes", padx=55, pady=20)
yes_button.grid(row=6, column=1, columnspan=1, )

no_button = Button(root1, text="no", padx=54, pady=20)
no_button.grid(row=6, column=2, columnspan=1, )


root1.mainloop()