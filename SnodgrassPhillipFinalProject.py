import tkinter as tk
from tkinter import ttk
import os

#Phillip snodgrass

#main window for program that holds the list of pizzas.
class OrderListWindow(tk.Tk):
  #initialize
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title("Pizza Pricer Tool")
    self.geometry("420x600")

    # attempt to use a tree while having no idea what i am doing
    self.pizzaTable = ttk.Treeview(self)
    #set the height of the table
    self.pizzaTable.configure(height = 20)
    #set up the title of each of the pizza parts
    self.pizzaTable["columns"] = ("size", "price")
    self.pizzaTable.heading("#0", text = "Pizza Name")
    self.pizzaTable.heading("size", text = "Size")
    self.pizzaTable.column("size", width = 100)
    self.pizzaTable.heading("price", text = "Price")
    self.pizzaTable.column("price", width = 100)
    #align the pizza table
    self.pizzaTable.grid(row = 2, column = 0)

    #add a scrollbar for the pizza table
    scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.pizzaTable.yview)
    #set the scroll value of the pizza table to the scrollbar that was just added
    self.pizzaTable.configure(yscroll=scrollbar.set)
    #align the scrollbar
    scrollbar.grid(row=2, column=1, sticky="ns")

    #pizza counter, counts how many pizzas have been made. used in the PizzaWindow for adding duplicate pizzas.
    self.pizzaCounter = 0
    #funny pizza image
    self.pizzaImage = tk.PhotoImage(file = "pizzayum.png")
    self.pizzaImageLabel = tk.Label(self, image = self.pizzaImage, text = "pizza")
    self.pizzaImageLabel.grid(row = 6, column = 0)
    
    #labels
    self.titleLabel = tk.Label(self, text = "Pizza Pricer")
    self.titleLabel.grid(row = 0, column = 0, sticky = "wn")
    self.toppingInstructionLabel = tk.Label(self, text = "Click the plus to view the toppings on a pizza.")
    self.toppingInstructionLabel.grid(row = 0, column = 0, sticky = "en")
    
    #button to remove a pizza
    self.removePizzaButton = ttk.Button(self, text = "Remove Pizza")
    self.removePizzaButton["command"] = self.removePizza
    self.removePizzaButton.grid(row = 3, column = 0, sticky = "S")

    #button to close the program
    self.closeButton = ttk.Button(self, text = "Exit")
    self.closeButton["command"] = self.closeProgram
    self.closeButton.grid(row = 3, column = 0, sticky = "SE")
    
    #button that adds pizza
    self.addPizzaButton = ttk.Button(self, text="Add pizza")
    self.addPizzaButton["command"] = self.openOrderWindow
    self.addPizzaButton.grid(row = 3, column = 0, sticky = "SW")

    #array that holds the name of each pizza for saving
    self.pizzaArray = []

    #opens the pizza ordering window
  def openOrderWindow(self):
    PizzaWindow()
    self.addPizzaButton["state"] = "disabled"
    self.closeButton["state"] = "disabled"
    self.removePizzaButton["state"] = "disabled"
    #remove a pizza
  def removePizza(self):
    if self.pizzaTable.focus() != "":
      self.pizzaTable.delete(self.pizzaTable.focus())
      #reset the pizza counter so it doesn't go negative if that ever becomes relevant
      if self.pizzaCounter >= 1:
        self.pizzaCounter -= 1
      if self.pizzaCounter <=0:
        self.pizzaCounter = 0

        #close the program
  def closeProgram(self):
    self.destroy()
    
    #pizza ordering window
class PizzaWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        #configure this window
        self.title("Create Pizza")
        self.geometry("310x300")

        #make sure if the user clicks the X the add pizza button is enabled.
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        
        #button that makes the pizza
        self.labelbutton = ttk.Button(self, text="Complete Pizza")
        self.labelbutton['command'] = self.addPizza
        self.labelbutton.grid(row = 6, column = 0, sticky = "SW")

        #button to close the program
        self.closeButton = ttk.Button(self, text = "Exit")
        self.closeButton["command"] = self.onClosing
        self.closeButton.grid(row = 6, column = 3, sticky = "SW")
        
        #add topping tickboxes
        self.hasSausage = tk.IntVar()
        self.sausageBox = tk.Checkbutton(self, text = "Sausage", variable = self.hasSausage).grid(row = 0, column = 3, sticky = "W")
        self.hasBacon = tk.IntVar()
        self.baconBox = tk.Checkbutton(self, text = "Bacon", variable = self.hasBacon).grid(row = 1, column = 3, sticky = "W")
        self.hasPepperoni = tk.IntVar()
        self.pepperoniBox = tk.Checkbutton(self, text = "Pepperoni", variable = self.hasPepperoni).grid(row = 2, column = 3, sticky = "W")
        self.hasPineapple = tk.IntVar()
        self.pineappleBox = tk.Checkbutton(self, text = "Pineapple", variable = self.hasPineapple).grid(row = 3, column = 3, sticky = "W")
        self.hasPeppers = tk.IntVar()
        self.peppersBox = tk.Checkbutton(self, text = "Peppers", variable = self.hasPeppers).grid(row = 4, column = 3, sticky = "W")
        self.hasAntimatter = tk.IntVar()
        self.antimatterBox = tk.Checkbutton(self, text = "Antimatter", variable = self.hasAntimatter).grid(row = 5, column = 3, sticky = "W")

        #add a textbox
        self.pizzaNameBox = tk.Entry(self)
        self.pizzaNameBox.grid(row = 0, column = 1)
        #label for textbox
        self.pizzaNameBoxLabel = tk.Label(self, text = "Pizza Name:")
        self.pizzaNameBoxLabel.grid(row = 0, column = 0, sticky = "WN")
        #funny pizza image
        self.pizzaImage = tk.PhotoImage(file = "pizza.png")
        self.pizzaImageLabel = tk.Label(self, image = self.pizzaImage, text = "pizza")
        self.pizzaImageLabel.grid(row = 6, column = 1)
        
        #radio buttons for pizza size
        self.pizzaSize = tk.StringVar()
        self.smallRadioButton = ttk.Radiobutton(self, text = "Small", variable = self.pizzaSize, value = "Small")
        self.mediumRadioButton = ttk.Radiobutton(self, text = "Medium", variable = self.pizzaSize, value = "Medium")
        self.largeRadioButton = ttk.Radiobutton(self, text = "Large", variable = self.pizzaSize, value = "Large")
        self.titanicRadioButton = ttk.Radiobutton(self, text = "Titanic", variable = self.pizzaSize, value = "Titanic")
        self.unreasonableRadioButton = ttk.Radiobutton(self, text = "Unreasonable", variable = self.pizzaSize, value = "Unreasonable")

        self.smallRadioButton.grid(row = 1, column = 0, sticky = "W")
        self.mediumRadioButton.grid(row = 2, column = 0, sticky = "W")
        self.largeRadioButton.grid(row = 3, column = 0, sticky = "W")
        self.titanicRadioButton.grid(row = 4, column = 0, sticky = "W")
        self.unreasonableRadioButton.grid(row = 5, column = 0, sticky = "W")

        

        #some variables
        #each topping is added to this array and then each value of this array is added as a child object to the pizza later
        self.toppingArray = []

        #total price used for pizza
        self.totalPrice = 0.0
        
        #this variable is set to false if any errors are found in the pizza the user tries to create.
        self.noError = True
        
        #if the user presses enter it submits the pizza.
        self.bind('<Return>', (lambda event: self.addPizza()))

        
    #add the pizza to the list
    def addPizza(self):
        #check for errors in user input
        if len(self.pizzaNameBox.get()) == 0:
           self.noError = False
        if self.pizzaSize.get() == "":
           self.noError = False
        
        if self.noError == True:
          #define name for pizza
          self.pizzaName = self.pizzaNameBox.get() + str(app.pizzaCounter)
          
          #add the pizza with the given name
          app.pizzaTable.insert("", "end" ,self.pizzaName, text = self.pizzaName.rstrip(self.pizzaName[-1]))
          
          #check for toppings
          if bool(self.hasSausage.get()):
            self.toppingArray.append("Sausage")
            self.totalPrice += 0.5
          if bool(self.hasBacon.get()):
            self.toppingArray.append("Bacon")
            self.totalPrice += 0.4
          if bool(self.hasPepperoni.get()):
            self.toppingArray.append("Pepperoni")
            self.totalPrice += 0.2
          if bool(self.hasPineapple.get()):
            self.toppingArray.append("Pineapple")
            self.totalPrice += 0.3
          if bool(self.hasPeppers.get()):
            self.toppingArray.append("Peppers")
            self.totalPrice += 0.6
          if bool(self.hasAntimatter.get()):
            self.toppingArray.append("Antimatter")
            self.totalPrice += 5000.0
          #scalable implementation for any number of toppings and adding the toppings to the table
          for top in self.toppingArray:
                app.pizzaTable.insert(self.pizzaName, "end", top + self.pizzaName, text = top)

          #set the size for the pizza
          app.pizzaTable.set(self.pizzaName, "size", self.pizzaSize.get())
          #add price for size
          match self.pizzaSize.get():
              case "Small":
                  self.totalPrice += 7.0
              case "Medium":
                  self.totalPrice += 10.0
              case "Large":
                  self.totalPrice += 15.0
              case "Titanic":
                  self.totalPrice += 30.0
              case "Unreasonable":
                  self.totalPrice += 100.0
          
          #add price to created pizza in table
          app.pizzaTable.set(self.pizzaName, "price", ("%0.2f" % self.totalPrice) + "$")
          #keep track of number of pizzas made
          app.pizzaCounter +=1
          #close the window so they don't click the button too many times
          self.destroy()
          
          #re-enable the base window's buttons
          app.addPizzaButton["state"] = "normal"
          app.removePizzaButton["state"] = "normal"
          app.closeButton["state"] = "normal"
          app.pizzaArray.append(self.pizzaName)
        self.noError = True
    #event to run upon the user clicking the X or the exit button
    def onClosing(self):
        app.addPizzaButton["state"] = "normal"
        app.removePizzaButton["state"] = "normal"
        app.closeButton["state"] = "normal"
        self.destroy()
#start the program
if __name__ == "__main__":
  app = OrderListWindow()
  app.mainloop()
