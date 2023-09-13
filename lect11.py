class Pizza:
    # Class Variable
    pizzaPrices = {"small": 8, "medium": 10, "large": 12}

    # Constructor
    def __init__(self, size):
        self.toppings = set()  # Instance Variable
        self.size = "small"  # Default size
        if size.lower() in self.pizzaPrices:  # Check if size is valid
            self.size = size.lower()  # Instance Variable

    # Methods
    def addTopping(self, topping):
        self.toppings.add(topping.lower())

    def removeTopping(self, topping):
        self.toppings.remove(topping)

    def setSize(self, newSize):
        if newSize.lower() in self.pizzaPrices:
            self.size = newSize.lower()

    def getSize(self):
        return self.size

    def getPrice(self):
        return self.pizzaPrices[self.size]

    def getToppings(self):
        return self.toppings

    # String representation
    def __str__(self):
        output = "A {} pizza with toppings:".format(self.size)
        for topping in self.toppings:
            output += "\n- {}".format(topping)
        output += "\nPrice: £{}\n".format(self.getPrice())
        return output


class StuffedCrustPizza(Pizza):
    # Class Variable
    crustTypes = ("cheese", "garlic", "hot dog")

    # Constructor
    def __init__(self, size, crust):
        super().__init__(size)  # Call to parent constructor
        self.crust = "cheese"  # Default crust
        if crust.lower() in self.crustTypes:
            self.crust = crust.lower()  # Instance Variable

    # Methods
    def setCrust(self, newCrust):
        if newCrust in self.crustTypes:
            self.crust = newCrust

    def getPrice(self):
        return super().getPrice() + 2  # Stuffed crust is £2 more

    def __str__(self):
        output = "A {} stuffed crust pizza with toppings:".format(self.size)
        for topping in self.toppings:
            output += "\n- {}".format(topping)
        output += "\nCrust type: {}".format(self.crust)
        output += "\nPrice: £{}\n".format(self.getPrice())
        return output


class Order:
    # Constructor
    def __init__(self):
        self.pizzas = []  # Instance Variable

    # Methods
    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getTotalPrice(self):
        totalPrice = 0
        for pizza in self.pizzas:
            totalPrice += pizza.getPrice()
        return totalPrice

    def __str__(self):
        output = "Your order contains:\n"
        for pizza in self.pizzas:
            output += "{}\n".format(pizza)
        output += "Total price of the order: £{}\n".format(
            self.getTotalPrice())
        return output


# Test the classes
def test():
    myOrder = Order()
    pizza1 = Pizza("small")
    pizza1.addTopping("Pepperoni")
    pizza1.addTopping("Jalapenos")
    pizza1.setSize("large")

    pizza2 = StuffedCrustPizza("Medium", "Cheese")
    pizza2.addTopping("Ham")
    pizza2.addTopping("Mushrooms")
    pizza2.setCrust("Garlic")

    myOrder.addPizza(pizza1)
    myOrder.addPizza(pizza2)

    print(myOrder)


test()
