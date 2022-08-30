# used the tabulate module
from tabulate import tabulate

# created a class called Shoes
class Shoes:

    # intitialized variables with self and assinged them to themselves
    def __init__(self,country,code,product,cost,quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity 
        
    # created a function called get_cost(self) 
    def get_cost(self):
        return f"{int(self.cost)}"
        
    # created a function called get_quanty(self)    
    def get_quanty(self):
        return f"{int(self.quantity)}"
     
    # created a function called setQuantity(self)  
    def setQuantity(self, quantity):
        self.quantity = quantity
        
    # used the repr function to display class object as a string         
    def __repr__(self):
        return f"[{self.country},{self.code},{self.product},{self.cost},{self.quantity}]"
        
    # used the str function to display class object as a string  
    def __str__(self):
        return f"{self.country}|{self.code}|{self.product}|{self.cost}|{self.quantity}"

   
# craated an empy_list called shoes_list
shoes_list = []
# craated an empy_list called x_1
x_1 = []
# craated an empy_list called y_1
y_1 = [] 
# craated an empy_list called l_1
l_1 = []

# Reading the file and appending the data to the list.
# use the try method to catch the error
try:
 with open("inventory.txt", "r") as f: 
  y = f.readlines()[1:]
  # Reading the file and appending the data to the list.
  # Reading the file and appending the data to the list.
  for i in y:
   my_var = i.split(",")
   # Creating an object of the class Shoes and assigning it to the variable qty_1.
   # Created an object
   qty_1 = Shoes(my_var[0],my_var[1],my_var[2],my_var[3],my_var[4].replace("\n", ""))
   # appended the list
   shoes_list.append(qty_1)
   # to change object value 
   my_x = qty_1.get_quanty()
   my_y = qty_1.get_cost()
   my_l = (qty_1.product).replace("\n","")
   x_1.append(my_x)
   y_1.append(my_y)
   l_1.append(my_l)
# if the following Error is ture than the following will be executed
except FileNotFoundError:
 print("File not found")

''' Created variables and then shoes_list from index '''
var_a = x_1[1:]
var_b = y_1[1:]
var_c = l_1[1:]

'''Used map() function to convert those values to an integer and stirng'''
final_1 = list(map(int,var_a))
final_2 = list(map(int,var_b))
final_3 = list(map(str,var_c))


''' created a function called read_shoes_data() '''
def read_shoes_data():
 print(shoes_list)

 
"""
It finds the smallest quantity of shoes in the list and then asks the user to input a new quantity
for that shoe.
"""
''' created a function called re_stock()'''
def re_stock():
  opt_quest = input("If you want to re_stock pick (yes): ").lower()
  if opt_quest == "yes":
   smallest = shoes_list[0]
   for jm in shoes_list:
    if int(jm.quantity) <= int(smallest.quantity):
       smallest = jm
   print(f"Smallest object is {smallest}")
   new_quantity = input("New Quantity: ")
   smallest.setQuantity(new_quantity)
   print(smallest)
  else:
   pass
 
"""
It takes the list of objects and creates a list of lists, then prints the list of lists using the
tabulate function
"""
''' created a function called view_all()'''  
def view_all():
 fg_list = []
 '''created a loop with a variable fg, for all values in shoes_list '''
 for fg in shoes_list:
  var_fg = [fg.country,fg.code,fg.product,fg.cost,fg.quantity]
  fg_list.append(var_fg)
 print(tabulate(fg_list, headers=["Country","Code","Product","Cost","Quantity"], tablefmt='grid')) 
 
"""
It takes the values from the lists final_3, final_1 and final_2 and multiplies them together and
prints the result
""" 
''' created a function called value_per_item() '''
def value_per_item():
 for m,n,o in zip(final_3,final_1,final_2):
  print(f"Value of  {m} is R{n*o}")
  
''' created a function called higest_qty() '''
def higest_qty():
 emp1 = []
 for m,n in zip(final_1,final_3):
  emp1.append((m,n))
 emp_dict = dict(emp1)
 max_dict1 = max(emp_dict.keys())
 print(emp_dict[max_dict1] + " " + " the shoe is for sale")


"""
This function captures the details of a shoe and adds it to the list of shoes.
"""
''' created a function called higest_qty() '''
def capture_shoes():
 ''' created variables requesting user input '''
 my_country = input("Enter name of country:")
 my_code = input("Enter code of shoe: ")
 my_product = input("Enter name of shoe:  ")
 my_cost = input("Enter cost of shoe: ")
 my_quantity = input("Enter quantity of shoe: ")
 my_var = Shoes(my_country,my_code,my_product,my_cost,my_quantity)
 shoes_list.append(my_var)
 print(shoes_list)

"""
It asks the user to input a shoe name, and then it searches the list of shoes for a shoe with that
name. If it finds one, it prints it
"""
''' created a function called search_shoe() '''
def search_shoe():
 search = input("Search for shoe: ")
 for j in shoes_list:
  if j.product == search:
   print(j)



while True:
   menu = input('''Select one of the following Options below:
          r - Read shoe data
          capt - Capture data
          va - View all data
          stock - Re-stock data quantity of the lowest quantity
          search - Search data product of data 
          value - Value price per item
          sale - Product of sale
          : ''').lower()

   ''' A menu that allows the user to select an option from the menu. '''
   if menu == "r":
    '''calling that fuction '''
    read_shoes_data()
   
   elif menu == "capt":
    capture_shoes()
   
   elif menu == "va":
    view_all()
   
   elif menu == "stock":
     re_stock()
   
   elif menu == "search":
    search_shoe()
   
   elif menu == "value":
     value_per_item()
     
   elif menu == "sale":
     higest_qty()
          