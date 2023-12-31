import tkinter as tk

root1 = tk.Tk()
root1.geometry("600x500")
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
    home_frame = tk.Frame(main_frame, padx=1, pady=1)
    home_frame.configure(height=500, width=500)
    lb = tk.Label(home_frame,
                      text="Cooking\n\n\nWhat are we cooking?",
                      font=('Bold', 15))
    lb.pack()
    home_frame.pack(pady=20)

def gList_page():
    home_frame = tk.Frame(main_frame, padx=1, pady=1)
    home_frame.configure(height=500, width=500)
    lb = tk.Label(home_frame,
                      text="Current\nGrocery\nList",
                      font=('Bold', 15))
    lb.pack()
    home_frame.pack(pady=20)

def future_page():
    home_frame = tk.Frame(main_frame, padx=1, pady=1)
    home_frame.configure(height=500, width=500)
    lb = tk.Label(home_frame,
                      text="What do you plan on cooking?",
                      font=('Bold', 15))
    lb.pack()
    home_frame.pack(pady=20)

def receive_page():
    home_frame = tk.Frame(main_frame, padx=1, pady=1)
    home_frame.configure(height=500, width=500)
    lb = tk.Label(home_frame,
                      text="Receive Groceries",
                      font=('Bold', 15))
    lb.pack()
    home_frame.pack(pady=20)

def inventory_page():
    home_frame = tk.Frame(main_frame, padx=1, pady=1)
    home_frame.configure(height=500, width=500)
    lb = tk.Label(home_frame,
                      text="Current\nInventory",
                      font=('Bold', 15))
    lb.pack()
    home_frame.pack(pady=20)

def exit_page():
    home_frame = tk.Frame(main_frame, padx=1, pady=1)
    home_frame.configure(height=500, width=500)
    lb = tk.Label(home_frame,
                      text="EXIT",
                      font=('Bold', 25))
    lb.pack()
    home_frame.pack(pady=20)

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

#yes_button = Button(root1, text="Yes", padx=55, pady=20)
#yes_button.grid(row=6, column=1, columnspan=1, )

#no_button = Button(root1, text="no", padx=54, pady=20)
#no_button.grid(row=6, column=2, columnspan=1, )


root1.mainloop()