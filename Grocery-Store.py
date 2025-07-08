# Grocery-Simulator.py

import random

item1 = 'Apple'
item2 = 'Banana'
item3 = 'Orange'
item4 = 'Pear'

item1_price = 0.50
item2_price = 0.30
item3_price = 0.60
item4_price = 0.40

cart_items = []
fruit_items = [item1, item2, item3, item4]
cart_prices = []

# print('\033[31m' + item1 + '\033[33m ' + item2 + '\033[31m + 33m ' + item3)

def print_items():   
    print(item1 + ' ' + '$' + str(item1_price) + ' USD')
    print(item2 + ' ' + '$' + str(item2_price) + ' USD')
    print(item3 + ' ' + '$' + str(item3_price) + ' USD')  
    print(item4 + ' ' + '$' + str(item4_price) + ' USD\n')

def item_count(price):
    while True:
        number = input('How many do you want? \n')
        try:
            multiply = round((int(number) * price), 2)
            cart_prices.append(multiply)
            print('You have added ' + str(number) + ' to your cart worth $' + str(multiply) + ' USD.')
            cart_items.append(number)
            grab_another_item()
            return
        except ValueError:
            print('Please enter a valid number.')
            item_count(price)

def view_cart():
    if len(cart_items) == 0:
        print('Your cart is empty.\n')
        choices()
    else:
        for i, item in enumerate(cart_items):
            print(f"{i + 1}. {item} - ${cart_prices[i]:.2f} USD\n")
        choices()

def checkout():
    total = round(sum(cart_prices), 2)
    if total == 0:
        print('Your cart is empty. Add items to your cart before checking out or leave.')
        choices()
        return
    else: 
        print('Your total is $' + str(total) + ' USD.')
        payment()

def payment():
    method = input('How would you like to pay? \n 1. [Cash]' + '     ' + ' 2. [Card] \n')
    if method == '1':
        print('You look in your wallet and only find a $100 bill. The store does not have change for that bill.')
        payment()
    elif method == '2':
        print('You insert the card. It declines.')
        card()
    else:
        print('Please enter 1 or 2.')
        payment()
        return

def card():
    user = input('1. [Try Again]     2. [Leave without paying] \n')
    if user == '1':
        chance = decline_chance()
        if chance <= 50:
            print('The card is accepted. You pay $' + str(sum(cart_prices)) + ' USD.')
            print('Thank you for shopping with us!')
            raise SystemExit
        else:
            print('It declines.')
            card()
    elif user == '2':
        print('You leave the store with your items without paying.')
        raise SystemExit
    else:
        print('Please enter 1 or 2.')
        card()
        return

def loading():
    pass

def decline_chance():
    return random.randint(0, 100)  

def item_selection():
    user_input = input('What item do you want to grab? \n')
    if user_input == 'Apple':
        item_count(item1_price)
    elif user_input == 'Banana':
        item_count(item2_price)
    elif user_input == 'Orange':
        item_count(item3_price)
    elif user_input == 'Pear':
        item_count(item4_price)
    else:
        print('That item is not available.')
        item_selection()
        return

def grab_another_item():
    another_item = input('Do you want to grab another item? \n 1. [Yes]     2. [No(Checkout)] \n')
    if another_item == '1':
        print_items()
        item_selection()
    elif another_item == '2':
         checkout()
    else:
        print('Please enter 1 or 2.')
        grab_another_item()
        return

def choices():
    choice = input('1. [View Cart]    2. [Grab An item]    3. [Checkout]     4. [Leave]\n')
    if choice == '1':
        view_cart()
    elif choice == '2':
        print_items()
        item_selection()
    elif choice == '3':
        checkout()
    elif choice == '4':
        if len(cart_items) == 0:
            print('You leave the store without buying anything.')
            raise SystemExit
        elif len(cart_items) > 0:
            print('You leave the store with your items without paying.')
            raise SystemExit
    else:
        print('Please enter 1, 2, or 3.')
        choices()
        return

# Start of program
print('\n')
print('-----Welcome to Walmart!----- \n')
choices()