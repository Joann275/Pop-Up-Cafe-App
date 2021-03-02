import csv
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()   
host = os.environ.get("mysql_host") 
user = os.environ.get("mysql_user") 
password = os.environ.get("mysql_pass") 
database = os.environ.get("mysql_db")   
connection = pymysql.connect(   
    host,   
    user,   
    password,   
    database    
)   
cursor = connection.cursor()    

def print_products_list():
    print("Cafe Menu:\n")
    cursor.execute('SELECT id, product_name, product_price FROM products')       
    rows = cursor.fetchall()        
    for row in rows:        
        print(f'id: {str(row[0])}, Name: {row[1]}, Price: {row[2]}')    

def add_new_product():
    name_input = input('Please enter the name: ')
    price_input = input('Please enter the price: ')
    sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
    val = (name_input, price_input)
    cursor.execute(sql, val)
    connection.commit()
    main_product_menu()

def option_remove_product():
    cancel_input = input('\nPress 0 to cancel\nPress ENTER to continue')
    if cancel_input == '0':
        main_product_menu()
    if cancel_input == '':
        remove_product()
    else:
        print("Sorry this wasn't a valid input, please try again!")
        option_remove_product()

def remove_product():
    print("Cafe Menu:\n")
    print_products_list()
    sql = "DELETE FROM products WHERE id = %s"
    val = input('Please enter the id of the product you want to delete: ')
    cursor.execute(sql, val)
    connection.commit()
    print("The product was successfully removed")
    main_product_menu()

def option_change_product():
    cancel_input = input('\nPress 0 to cancel\nPress ENTER to continue')
    if cancel_input == '0':
        main_product_menu()
    if cancel_input == '':
        change_product()
    else:
        print("Sorry this wasn't a valid input, please try again!")
        option_change_product()

def change_product():
    try:
        print_products_list()
        id_input = int(input('Please enter the id of the product you want to change:'))
        name_input = input('Please enter the new name of the product: ')
        price_input = input('Please enter the new price of the product: ')
        sql = "UPDATE products SET product_name = %s, product_price = %s WHERE id = %s"
        val = (name_input, price_input, id_input)
        cursor.execute(sql, val)
        connection.commit()
    except:
        print("That was not in the List")
        change_product()
    main_product_menu()

def product_user_input(man_input):
    if man_input == 0:
        print('You are back in the main menu!')
        first_menu()
    if man_input == 1:
        print_products_list()
        main_product_menu()
    if man_input == 2:
        add_new_product()
    if man_input == 3:
        option_change_product()
    if man_input == 4:
        option_remove_product()
    else:
        print("Number not defined")
        main_product_menu()

def print_courier_list():
    print("Available courier:\n")
    cursor.execute('SELECT id, name, phone FROM courier')       
    rows = cursor.fetchall()        
    for row in rows:        
        print(f'id: {str(row[0])}, Name: {row[1]}, Phone: {row[2]}')    

def add_new_courier():
    name_input = input('Please enter the name: ')
    phone_input = input('Please enter the phone nummber: ')
    sql = "INSERT INTO courier (name, phone) VALUES (%s, %s)"
    val = (name_input, phone_input)
    cursor.execute(sql, val)
    connection.commit()
    main_courier_menu()

def remove_courier():
    print("Available courier:\n")
    print_courier_list()
    sql = "DELETE FROM courier WHERE id = %s"
    val = input('Please enter the id of the courier you want to delete: ')
    cursor.execute(sql, val)
    connection.commit()
    print("The courier was successfully removed")
    main_courier_menu()

def change_courier():
    print_courier_list()
    try:
        print_courier_list()
        id_input = int(input('Please enter the id of the courier you want to change:'))
        name_input = input('Please enter the new name of the courier: ')
        price_input = input('Please enter the new phone number of the courier: ')
        sql = "UPDATE courier SET name = %s, phone = %s WHERE id = %s"
        val = (name_input, price_input, id_input)
        cursor.execute(sql, val)
        connection.commit()
    except:
        print("That was not in the List")
        change_courier()
    main_courier_menu()
    print_courier_list()

def option_change_courier():
    delete_input = input('\nPress 0 to cancel\nPress ENTER to continue')
    if delete_input == "0":
        main_courier_menu()
    if delete_input == '':
        change_courier()
    else:
        print("Sorry this wasn't a valid input, please try again!")
        option_change_courier()

def option_remove_courier():
    delete_inputs = input('\nPress 0 to cancel\nPress ENTER to continue')
    if delete_inputs == '0':
        main_courier_menu()
    if delete_inputs == '':
        remove_courier()
    else:
        print("Sorry this wasn't a valid input, please try again!")
        option_remove_courier()

def courier_user_input(courier_input):
    if courier_input == 0:
        print('You are back in the main menu!')
        first_menu()
    if courier_input == 1:
        print_courier_list()
        main_courier_menu()
    if courier_input == 2:
        add_new_courier()
    if courier_input == 3:
        option_change_courier()
    if courier_input == 4:
        option_remove_courier()
    else:
        print("Number not defined")
        main_courier_menu()

def print_orderlist_by_courier():
    print("Current orders:\n")
    cursor.execute('SELECT id, customer_name, customer_address, customer_phone, courier, order_status, items FROM orders ORDER BY courier')       
    rows = cursor.fetchall()        
    for row in rows:        
        print(f'ID: {str(row[0])}, Name: {row[1]}, Address: {row[2]}, Phone number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]}, Items: {row[6]}')  

def print_orderlist_by_status():
    print("Current orders:\n")
    cursor.execute('SELECT id, customer_name, customer_address, customer_phone, courier, order_status, items FROM orders ORDER BY order_status')       
    rows = cursor.fetchall()        
    for row in rows:        
        print(f'ID: {str(row[0])}, Name: {row[1]}, Address: {row[2]}, Phone number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]}, Items: {row[6]}')  

def print_order_list():
    print("Current orders:\n")
    cursor.execute('SELECT id, customer_name, customer_address, customer_phone, courier, order_status, items FROM orders')       
    rows = cursor.fetchall()        
    for row in rows:        
        print(f'ID: {str(row[0])}, Name: {row[1]}, Address: {row[2]}, Phone number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]}, Items: {row[6]}')   

def option_print_menu():
    print_input = int(input('\nPlease enter a number to see the following options\n1: Orders sorted by ID\n2: Orders sorted by courier\n3: Orders sorted by status\n0: return back to the Order Menu'))
    if print_input == 1:
        print_order_list()
        option_print_menu()
    if print_input == 2:
        print_orderlist_by_courier()
        option_print_menu()
    if print_input == 3:
        print_orderlist_by_status()
        option_print_menu()
    if print_input == 0:
        main_order_menu()
    else:
        print("Sorry this wasn't a valid input, please try again!")
        option_print_menu()

def add_new_order():
    try:
        name_input = input('Please enter the name: ')
        address_input = input('Please enter the customers address: ')
        phone_input = input('Please enter the customers phone numer: ')
        print_courier_list()
        courier_input = input('Please enter the id of the courier: ')
        status_input = 'preparing'
        items_order = []
        def create_order():
            print("Cafe Menu:\n")
            print_products_list()
            while int:
                try:
                    order_input = int(input('Please enter the number of the product you want to order: '))
                except:
                    print('Sorry we do not recognize this number, please try again')
                    continue   
                if order_input == 0:
                    print('Sorry 0 is not a vaild input, please try again')
                    continue
                break
            items_order.append(order_input)
        create_order()
        def add_another_product():
            while int:
                try:
                    order_input = int(input('Please enter the number of the product you want to order or enter 0 to submit your order'))
                except:
                    print('Sorry we do not recognize this number, please try again')
                    continue   
                if order_input == 0:
                    break
                items_order.append(order_input)
        add_another_product()
        print("The order was succesfully entered")
        string = str(items_order).strip('[]')
        item_input = string
        sql = "INSERT INTO orders (customer_name, customer_address, customer_phone, courier, order_status, items) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name_input, address_input, phone_input, courier_input, status_input, item_input)
        cursor.execute(sql, val)
        connection.commit()
        print (string)
        # print (items_order)
    except:
        print('Sorry, we do not regognize this input! Please try it again :)')
        add_new_order()
    main_order_menu()

def updating_order_status_menu():
    update_input = input('\nPress 0 to cancel\nPress ENTER to continue')
    if update_input == "0":
        main_order_menu()
    if update_input == "":
        updating_order_status()

def updating_order_status():
    print('Order List:\n')
    print_order_list()
    id_input = int(input('Please enter the id of the order you want to update the status: '))
    print('Please choose one of the following status:\n "waiting for a courier", "out for delivery", "deliverd"')
    name_input = input('Please enter the new status: ')
    sql = "UPDATE orders SET order_status = %s WHERE id = %s"
    val = (name_input, id_input)
    cursor.execute(sql, val)
    connection.commit()
    main_order_menu()

# def amending_order():

def option_delete_order():
    delete_input = input('\nPress 0 to cancel\nPress ENTER to continue')
    if delete_input == "0":
        main_order_menu()
    if delete_input == '':
        delete_order()

def delete_order():
    print("Order List:\n")
    print_order_list()
    sql = "DELETE FROM courier WHERE id = %s"
    val = int(input('Please enter the id of the order you want to delete: '))
    cursor.execute(sql, val)
    connection.commit()
    print("The order was successfully removed")
    main_order_menu()

def order_user_input(order_input):
    if order_input == 0:
        print('You are back in the main menu!')
        first_menu()
    if order_input == 1:
        option_print_menu()
    if order_input == 2:
        add_new_order()
    if order_input == 3:
        updating_order_status_menu()
    if order_input == 4:
        main_order_menu() #amending_order()
    if order_input == 5:
        option_delete_order()
    else:
        print("Number not defined")
        main_order_menu()

def main_product_menu():
    print("\nPlease click '1' to see the products\nPlease click '2' to create a new product\nPlease click '3' to edit a product\nPlease click '4' to delete a product\nPlease click '0' to return to main menu")
    user_input = int(input())
    if user_input in (0, 1, 2, 3, 4):
        product_user_input(user_input)
    else:
        print("Number not defined")
        main_product_menu()

def main_courier_menu():
    print("\nPlease click '1' to see the courier\nPlease click '2' to create a new courier\nPlease click '3' to edit a courier\nPlease click '4' to delete a courier\nPlease click '0' to return to main menu")
    user_input = int(input())
    if user_input in (0, 1, 2, 3, 4):
        courier_user_input(user_input)
    else:
        print("Number not defined")
        main_courier_menu()

def main_order_menu():
    print("\nPlease enter '1' to see current orders\nPlease enter '2' to create a new order\nPlease enter '3' to update order status\nPlease enter '4' to update the order\nPlease enter '5' to delete an order\nPlease enter '0' to return to main menu")
    user_input = int(input())
    if user_input in (0, 1, 2, 3, 4, 5):
        order_user_input(user_input)
    else:
        print("Number not defined, please try again!:)")
        main_order_menu()

def first_menu():
    user_inputs = int(input("\nPlease click '1' to see the products\nPlease click '2' to see the courier list\nPlease enter '3' to see the order menu\nPlease click '0' to exit the app\n"))
    if user_inputs == 0:
        cursor.close()
        connection.close()
        exit("Thank you for visiting our app, have a nice day! :)")
    if user_inputs == 1:
        main_product_menu()
    if user_inputs == 2:
        main_courier_menu()
    if user_inputs == 3:
        main_order_menu()
    else:
        print("Number not defined")
        first_menu()

def start_app():
    print('\nHello to the Pop Up Cafe app!')
    first_menu()

start_app()