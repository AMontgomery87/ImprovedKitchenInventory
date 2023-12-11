import tkinter as tk
from Recipes import*
from collections import Counter

grocery_fileR = [open("GroceryList", "r+")]

with open("GroceryList") as f:
    grocery_fileR = f.read().splitlines()
    grocery_counter = Counter(grocery_fileR)



root1 = tk.Tk()
root1.geometry("615x500")
root1.title("Kitchen Inventory Helper")

def hide_indicators():
    home_indicate.config(bg="green")
    cook_indicate.config(bg="green")
    grocerylist_indicate.config(bg="green")
    future_indicate.config(bg="green")
    receive_indicate.config(bg="green")
    inventory_indicate.config(bg="green")
    exit_indicate.config(bg="green")

def indicate(lb, page):
    hide_indicators()
    lb.config(bg="blue")
    delete_pages()
    page()

options_frame = tk.Frame(root1, bg='green')


options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=112, height=500)

main_frame=tk.Frame(root1, highlightbackground='red', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=500, width=500)


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def home_page():
    home_frame = tk.Frame(main_frame, padx=1, pady=1)
    home_frame.configure(height=500, width=500)
    lb = tk.Label(home_frame,
                      text="Home\n\n\nWelcome to your Kitchen!",
                      font=('Bold', 15))
    lb.pack()
    home_frame.pack(pady=20)

def cook_page():
    cook_frame = tk.Frame(main_frame, padx=1, pady=1)
    cook_frame.configure(height=500, width=500)
    lb = tk.Label(cook_frame,
                      text="Cooking\n\n\nWhat are we cooking?",
                      font=('Bold', 15))
    lb.pack()
    cook_frame.pack(pady=20)

#trying to print line for line, grocery_counter with item:quantity
def gList_page():
    gList_frame = tk.Frame(main_frame, padx=1, pady=1)
    gList_frame.configure(height=500, width=500)
    lb = tk.Label(gList_frame,
                      text="Current\nGrocery\nList",
                      font=('Bold', 15))
    lb.pack()
    def grocery_list_print():
        for grocery in grocery_counter:
            lb2 = tk.Label(gList_frame, text = grocery)
            lb3 = tk.Label(gList_frame, text= "\n", font= ("bold", 1))
            lb2.pack(pady=1)
            lb3.pack(pady=0)
    grocery_list_print()
    gList_frame.pack(pady=20)

def future_page():
    future_frame = tk.Frame(main_frame, padx=1, pady=1)
    future_frame.configure(height=500, width=500)
    lb = tk.Label(future_frame,
                      text="What do you plan on cooking?",
                      font=('Bold', 15))
    lb.pack()
    future_frame.pack(pady=20)

def receive_page():
    receive_frame = tk.Frame(main_frame, padx=1, pady=1)
    receive_frame.configure(height=500, width=500)
    lb = tk.Label(receive_frame,
                      text="Receive Groceries",
                      font=('Bold', 18))
    lb.grid(row=0, column=1, columnspan=3)
#attempting to get yes_press to answer 'yes' and no_press to answer 'no' to trigger item removal from groceryList
#and add to Inventory

    def yes_press():
        return

    def no_press():
        return

#currently will add items in reverse order and continuously into the entry field. Need to make a loop that gets input
#from the user before adding the next item being added to the entry field
    def grocery_receive():
        for grocery in grocery_counter:
            e.insert(-1, "Did you receive "+ grocery + "? ")





    e = tk.Entry(receive_frame, width=30, borderwidth=3, font=("bold", 16))
    e.grid(row=1, column= 1, columnspan=3, padx=10, pady=10)
    grocery_receive()

    yes_button = tk.Button(receive_frame, text="Yes", padx=55, pady=20, command=yes_press)
    yes_button.grid(row=2, column=1)

    no_button = tk.Button(receive_frame, text="no", padx=54, pady=20, command=no_press)
    no_button.grid(row=2, column=3)
    receive_frame.pack(pady=20)

def inventory_page():
    inventory_frame = tk.Frame(main_frame, padx=1, pady=1)
    inventory_frame.configure(height=500, width=500)
    lb = tk.Label(inventory_frame,
                      text="Current\nInventory",
                      font=('Bold', 15))
    lb.pack()
    inventory_frame.pack(pady=20)

def exit_page():
    exit_frame = tk.Frame(main_frame, padx=1, pady=1)
    exit_frame.configure(height=500, width=500)
    lb = tk.Label(exit_frame,
                      text="EXIT",
                      font=('Bold', 25))
    lb.pack()

    exit_frame.pack(pady=20)
home_page()

#options for frames and indicator
home_button = tk.Button(options_frame, text="Home", bd=0, bg='green', highlightbackground='green', padx=20, pady=20,
                        command=lambda: indicate(home_indicate, home_page))
home_button.place(x=10, y=10)

home_indicate= tk.Label(options_frame, text='', bg="green", height=3)
home_indicate.place(x=2, y=12)

cook_button = tk.Button(options_frame, text="Cook", bd=0, bg='green', highlightbackground='green', padx=23, pady=20,
                        command=lambda: indicate(cook_indicate, cook_page))
cook_button.place(x=10, y=75)

cook_indicate= tk.Label(options_frame, text='', bg="green", height=3)
cook_indicate.place(x=2, y=77)

seeGroceryList_button = tk.Button(options_frame, text="See\nGrocery\nList", bd=0, bg='green', highlightbackground='green', padx=14, pady=10,
                                  command=lambda: indicate(grocerylist_indicate, gList_page))
seeGroceryList_button.place(x=10, y=140)

grocerylist_indicate= tk.Label(options_frame, text='', bg="green", height=3)
grocerylist_indicate.place(x=2, y=142)

future_button = tk.Button(options_frame, text="Future\nRecipes", bd=0, bg='green', highlightbackground='green', padx=14, pady=10,
                          command=lambda: indicate(future_indicate, future_page))
future_button.place(x=10, y=220)

future_indicate= tk.Label(options_frame, text='', bg="green", height=3)
future_indicate.place(x=2, y=222)

receiveGrocery_button = tk.Button(options_frame, text="Receive\nGroceries", bd=0, bg='green', highlightbackground='green', padx=9, pady=15,
                                  command=lambda: indicate(receive_indicate, receive_page))
receiveGrocery_button.place(x=10, y=290)

receive_indicate= tk.Label(options_frame, text='', bd=0, bg="green", height=3)
receive_indicate.place(x=2, y=292)

seeInventory_button = tk.Button(options_frame, text="See\nInventory", bd=0, bg='green', highlightbackground='green', padx=9, pady=15,
                                command=lambda: indicate(inventory_indicate, inventory_page))
seeInventory_button.place(x=10, y=363)

inventory_indicate= tk.Label(options_frame, text='', bg="green", height=3)
inventory_indicate.place(x=2, y=365)

exit_button = tk.Button(options_frame, text="EXIT", bd=0, bg='green', highlightbackground='green', padx=26, pady=20,
                        command=lambda: indicate(exit_indicate, exit_page))
exit_button.place(x=10, y=435)

exit_indicate= tk.Label(options_frame, text='', bg="green", height=3)
exit_indicate.place(x=2, y=437)



root1.mainloop()

