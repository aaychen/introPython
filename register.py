#Anna Chen
#May 30, 2019
#zyLab 9.12 The Evil Register (extends online shopping cart program (zyLab 9.11))
#Prompts user for items to purchase and prints a receipt of the items in an evil or good style.

#ItemToPurchase class
class ItemToPurchase:
	def __init__(self, name='none', price=0, qty=0): #constructor
		self.item_name = name #assign attributes (item_name, item_price, item_quantity) to parameters (default or passed values)
		self.item_price = price
		self.item_quantity = qty

	def __lt__(self, other): #implemented to allow for sorting ItemToPurchase objects
		return self.get_item_cost() < other.get_item_cost() #will sort in ascending order of item cost normally ("default" is evil)

	#Prints total cost of a specific item.
	def print_item_cost(self):
		total = self.get_item_cost() #get total of item by calling own get_item_cost() function
		print('%s %d @ $%d = $%d' %(self.item_name , self.item_quantity, self.item_price, total)) #prints info and total cost of item
		return

	#Returns total cost of a specific item.
	def get_item_cost(self):
		return self.item_price * self.item_quantity #price*qty=total

#Receipt class
class Receipt:
	def __init__(self, name='Real Human', date='Today', items_list=[]): #constructor
		self.customer_name = name #assign attributes (customer_name, date, cart_items) to parameters (default or passed values)
		self.date = date
		self.cart_items = items_list

	#Adds an item to the receipt
	def add_item(self, item):
		self.cart_items.append(item) #adds item to cart_items list
		return

	#Prints the receipt with an evil/good greeting and costs of items.
	def print_receipt(self, isevil=True): #by default, isevil is True
		if(isevil): #if evil, print evil greeting
			print('Welcome to EvilMart,', self.customer_name)
			print(self.date)
			print('Have an EVIL day!')
		else: #otherwise, print good greeting
			print('Welcome to GoodCo,', self.customer_name)
			print(self.date)
			print('Have a GOOD day!')

		total_cost = 0 #accumulator for total cost of all items
		if(isevil): #if evil, sort ItemToPurchase objects in default order (ascending costs)
			self.cart_items = sorted(self.cart_items)
		else: #if not evil, sort in reverse order (descending costs)
			self.cart_items = sorted(self.cart_items, reverse=True)
		for item in self.cart_items: #iterates over each ItemToPurchase object in cart_items
			item.print_item_cost() #uses ItemToPurchase's print_item_cost() method to output each item and saves total cost of just that item
			total_cost += item.get_item_cost() #adds total of item to total cost by calling the get_item_cost() function of the item object
		print("Total: $%d" % total_cost) #prints total cost
		return total_cost

#main function
def main():
	customer_name, date, is_evil = get_customer_info() #get customer info and store the returned values through unpacking
	receipt = Receipt(customer_name, date) #creates Receipt object using customer_name and date
	while(True): #infinite loop
		item = get_item() #call get_items() to prompt user for items and save returned value 
		if(item==None): #means the user didn't enter anything for name of item
			break #exit the loop
		receipt.add_item(item) #if entered an item, add to the receipt
	receipt.print_receipt(is_evil) #print receipt by calling receipt object's print_receipt() function

#Prompts user for customer info (name, date, and whether he/she is evil).
def get_customer_info():
	name = input('Enter Customer Name:\n') #prompts for name
	date = input("Enter Today's Date:\n") #prompts for date
	evil_answer = input('Are you evil?\n') #asks if evil or not
	if('y' in evil_answer.lower()): #if 'y' is in the answer to evil, then is evil
		evil_status = True
	else: #otherwise, not evil
		evil_status = False
	return name, date, evil_status

#Prompts user to enter item's name, price, and quantity and creates an object of class ItemToPurchase.
def get_item():
	name = input("Enter the item name:\n") #prompt user for name of item
	if(name==''): #if user doesn't enter anything for name, return None
		return None
	price = int(input("Enter the item price:\n")) #prompt user for item's price
	qty = int(input("Enter the item quantity:\n")) #prompt user for item's quantity
	item = ItemToPurchase(name, price, qty) #creates ItemToPurchase object using user-entered data
	return item


if(__name__ == '__main__'): #module check
	main()


