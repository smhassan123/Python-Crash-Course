def makePizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with following toppings:")
    for topping in toppings:
        print(f"-{topping}")