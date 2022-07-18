import tkinter as tk
from tkinter import ttk

#Phillip snodgrass
#Most of this stuff is for testing atm, will add other functionality later.

class OrderListWindow(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title("Main")
    self.geometry("1000x500")

    # attempt to use a tree while having no idea what i am doing
    self.pizzaTable = ttk.Treeview(self)
    #set the height of the table
    self.pizzaTable.configure(height = 20)
    #set up the title of each of the pizza parts
    self.pizzaTable["columns"] = ("toppings", "price")
    self.pizzaTable.heading("#0", text = "Pizza Name")
    self.pizzaTable.heading("toppings", text = "Toppings")
    self.pizzaTable.heading("price", text = "Price")
    #align the pizza table
    self.pizzaTable.grid(row = 2, column = 0)
    #add a scrollbar for the pizza table
    scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.pizzaTable.yview)
    #set the scroll value of the pizza table to the scrollbar that was just added
    self.pizzaTable.configure(yscroll=scrollbar.set)
    #align the scrollbar
    scrollbar.grid(row=2, column=1, sticky="ns")

    #pizza counter, counts how many pizzas have been made
    self.pizzaCounter = 0
    # label

    # button
    self.button = ttk.Button(self, text="Click Me")
    #button that opens the order window
    self.button['command'] = self.openOrderWindow
    self.button.grid(row = 1, column = 2)

    
  def openOrderWindow(self):
    PizzaWindow()
class PizzaWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        #configure this window
        self.title("Create Pizza")
        self.geometry("500x500")
        #add a button
        self.labelbutton = ttk.Button(self, text="Click Me")
        self.labelbutton['command'] = self.addPizza
        self.labelbutton.pack()
        #add a tickbox
        self.hasSausage = tk.IntVar()
        self.sausageBox = tk.Checkbutton(self, text = "Sausage", variable = self.hasSausage).pack()
        #each topping is added to this string
        self.toppingArray = []
        #and is later added to this string to be used for the toppings value
        self.toppingString = ""
    #add the pizza to the list
    def addPizza(self):
        app.pizzaTable.insert("", "end", "mypizza" + str(app.pizzaCounter), text = "sausage" + str(app.pizzaCounter))
        #check for toppings
        print(self.hasSausage.get())
        if bool(self.hasSausage.get()):
            self.toppingArray.append("Sausage")
        #scalable implementation for any number of toppings
        for top in self.toppingArray:
            self.toppingString = self.toppingString + top
        #add the pizza to the pizza table
        app.pizzaTable.set("mypizza" + str(app.pizzaCounter), "toppings", self.toppingString)
        #keep track of number of pizzas made
        app.pizzaCounter +=1
        #close the window so they don't click the button too many times
        self.destroy()
#start the program
if __name__ == "__main__":
  app = OrderListWindow()
  app.mainloop()
