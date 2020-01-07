#----------------------------
#Shopping List
#Sydney Loerzel
#January 5, 2020
#----------------------------

#----------------Dicts-----------------------

#Creates/states what my list will be 
shop_list = {}

#----------------Functions-------------------

def add_item():
    done = False
    while done == False:
        key = input("What do you need to add? Type 'done' to exit > ").lower()
        if key == "butter":
            shop_list[key] = 4.98
        elif key == "brown sugar":
            shop_list[key] = 2.97
        elif key == "white sugar":
            shop_list[key] = 2.97
        elif key == "eggs":
            shop_list[key] = 5.27
        elif key == "vanilla":
            shop_list[key] = 3.97
        elif key == "baking soda":
            shop_list[key] = 1.47
        elif key == "salt":
            shop_list[key] = 1.97
        elif key == "flour":
            shop_list[key] = 2.97
        elif key == "chocolate chips":
            shop_list[key] = 3.57
        elif key != "done":
            print("I didn't catch that. Make sure to spell right and include spaces")
        elif key == "done":
            done = True

def discount():
    key = input("What item would you like to discount").lower()
    shop_list[key] = shop_list[key] - 0.20
    shop_list[key] = round(shop_list[key], 2)
    
def price():
    print(sum(shop_list.values()))
    

def main():
    print("You have been wonderfully told to make some cookies")
    print("Problem is. You don't know if you have all the ingredients")
    print("What you need is butter, brown sugar, white sugar, eggs, and vanilla")
    print("As well you need baking soda, salt, flour, chocolate chips")
    print("You go take a look at what you have. You are missing a few things")
    print("Time to make a shopping list")
    add_item()
    print("Now you are at the store.")
    print("Lets look at the items you need and the prices")
    print(shop_list)
    print("You grab everything you need,")
    print("At the cashier you get a 20 cent discount off any item you want")
    discount()
    print("You are the lucky person and can choose a second item to discount")
    discount()
    print("Lets look at all items and the prices")
    print(shop_list)
    print("Now lets look at the total cost")
    price()

#-------------------Main---------------------
    
main()