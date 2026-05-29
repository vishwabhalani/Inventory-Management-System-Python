import json
import os
products={}
file_name="products.json"

def load_data():
	global products
	if os.path.exists(file_name):
		with open(file_name,"r") as file:
			data=json.load(file)
			products={
			int(key):value
			for key,value in data.items()
			}
	else:
		products={}

def Save_Data():
	with open(file_name,"w") as file:
		json.dump(products,file,indent=4)

def Add_Product():
	product_id=int(input("Enter Product ID:"))
	if product_id in products:
		print("Already Exists")
	else:
		name=input("Enter Product Name:")
		price=int(input("Enter Product Price:"))
		stock=int(input("Enter Product Stock:"))
		products[product_id]={
		"name":name,
		"price":price,
		"stock":stock,
		"sold":0
		}
		Save_Data()
		print("Product Added Successfully")
		print()

def Search_Product():
	product_id=int(input("Enter Product ID:"))
	if product_id in products:
		print("Product Found")
		print("Product Name:",products[product_id]["name"])
		print("Product Price:",products[product_id]["price"])
		print("Product Stock:",products[product_id]["stock"])
		print("Product Sold:",products[product_id]["sold"])
	else:
		print("Product Not Found")
	print()
def Update_Stock():
	product_id=int(input("Enter Product ID:"))
	if product_id in products:
		new_stock=int(input("Enter New Stock:"))
		products[product_id]["stock"]=products[product_id]["stock"]+new_stock
		Save_Data()
		print("Stock Added Successfully")
	else:
		print("Product Not Found")
	print()

def Sell_Product():
	product_id=int(input("Enter Product ID:"))
	if product_id in products:
		qty=int(input("Enter Quantity to Sell:"))
		if products[product_id]["stock"]<qty:
			print("Insufficient Stock")
		else:
			products[product_id]["stock"]=products[product_id]["stock"]-qty
			products[product_id]["sold"]=products[product_id]["sold"]+qty
			total=qty*products[product_id]["price"]
			Save_Data()
			print("--------BILL--------")
			print("Product Name:",products[product_id]["name"])
			print("Quantity:",qty)
			print("Total:",total)
			print("Product Sold Successfully")
	else:
		print("Product Not Found")
	print()

def Delete_Product():
	product_id=int(input("Enter Product ID:"))
	if product_id in products:
		del products[product_id]
		Save_Data()
		print("Product Deleted Successfully")
	else:
		print("Product Not Found")
	print()

def View_All_Products():
	if len(products)==0:
		print("No Products are there")
	else:
		for product_id,details in products.items():
			print("Product ID:",product_id)
			print("Product Name:",details["name"])
			print("Product Price:",details["price"])
			print("Product Stock:",details["stock"])
			print("Product Sold:",details["sold"])
			if details["stock"]<5:
				print("Low Stock Warning")
	print()

def Sales_Report():
	total_sales=0
	most_sold_product=None
	highest_sold=0
	for product_id,details in products.items():
		sales=details["sold"]*details["price"]
		total_sales=total_sales+sales
		if details["sold"]>highest_sold:
			highest_sold=details["sold"]
			most_sold_product=details["name"]
	print("--------Sales Report--------")
	print("Total Sales:",total_sales)
	if most_sold_product:
		print("Most Sold Product:",most_sold_product)
	else:
		print("No Products Sold Yet")
	print()

load_data()
while(True):
	print("========Inventory Management System========")
	print("1.Add Products")
	print("2.Search Product")
	print("3.Update Stock")
	print("4.Sell Product")
	print("5.Delete Product")
	print("6.View All Products")
	print("7.Sales Report")
	print("8.Exit")
	print()
	choice=int(input("Enter Your Choice:"))
	if choice==1:
		Add_Product()
	elif choice==2:
		Search_Product()
	elif choice==3:
		Update_Stock()
	elif choice==4:
		Sell_Product()
	elif choice==5:
		Delete_Product()
	elif choice==6:
		View_All_Products()
	elif choice==7:
		Sales_Report()
	elif choice==8:
		print("Exit.Bye")
		break
	else:
		print("Invalid Choice")
		print()

