# def add_nums(x, y):
#     total = x + y
#     return total

# print(add_nums(2,3))    

def get_melon_order_price(price, quantity):
    """Calculate the cost for an order of melons."""

    tax = 0.075

    print("$", price * quantity + (tax * price * quantity)) 

get_melon_order_price(3, 1)   