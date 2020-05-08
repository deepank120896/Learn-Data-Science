class Customer:
	def __init__(self,name,email):
		self.name = name
		self.email = email
		self.purchases = []
	
	def purchase(self,inventory,product):
		inventory_dict = inventory.inventory
		if product in inventory_dict:
			if inventory_dict[product]>0:
				self.purchases.append(product)
				inventory_dict[product] -= 1
			else:
				print('Out of Stock')
		else:
			print('We don\'t have product')
			
	def print_Purchases(self):
		print("Customer has purchased ")
		for item in self.purchases:
			print(item.name)
		print()
		
class Product:
	def __init__(self,name,price):
		self.name = name
		self.price = price

		
class Inventory:
	def __init__(self):
		self.inventory = {}
	
	def add_Product(self,product,quantity):
		if product not in self.inventory:
			self.inventory[product] = quantity
		else:
			self.inventory[product] += quantity
			
	def print_Inventory(self):
		for key,value in self.inventory.items():
			print(str(key.name) + ' : ' + str(value))
		print()
		
		
customer = Customer('John','john.doe@gmail.com')


apple_watch = Product('Apple Watch',299)
mac = Product('Apple Mac',1199)


inventory = Inventory()
inventory.add_Product(apple_watch,10)
inventory.add_Product(mac,49)
inventory.print_Inventory()

customer.purchase(inventory, apple_watch)
inventory.print_Inventory()
customer.print_Purchases()
customer.purchase(inventory, mac)
inventory.print_Inventory()
customer.print_Purchases()