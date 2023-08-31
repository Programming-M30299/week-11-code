class Laptop:
    ramOptions = {
        4: 0,
        8: 50,
        16: 100,
        32: 200
    }

    def __init__(self, brand, basePrice):
        self.brand = brand
        self.basePrice = basePrice
        self.ram = 4

    def getBrand(self):
        return self.brand

    def getRam(self):
        return self.ram

    def getPrice(self):
        ramPrice = self.ramOptions[self.ram]
        return self.basePrice + ramPrice

    def setRam(self, ram):
        if ram in self.ramOptions:
            self.ram = ram

    def __str__(self):
        output = "{} Laptop with {} GB RAM".format(self.brand, self.ram)
        output += " priced at £{}".format(self.getPrice())
        return output


class ShoppingCart:
    def __init__(self):
        self.laptops = []
        self.total = 0

    def addLaptop(self, laptop):
        self.laptops.append(laptop)
        self.total += laptop.getPrice()


def testLaptop():
    laptop = Laptop("Dell", 999.99)
    print("laptop's brand is", laptop.getBrand())
    print("laptop's RAM is", laptop.getRam())
    print("laptop's price is", laptop.getPrice())

    laptop.setRam(32)
    print("laptop's RAM is now", laptop.getRam())
    laptop.setRam(30)
    print("laptop's RAM is still", laptop.getRam())

    print("laptop's price is now", laptop.getPrice())

    print(laptop)


def testShoppingCart():
    cart = ShoppingCart()
    dellLaptop = Laptop("Dell", 999.99)
    appleLaptop = Laptop("Apple", 1349.00)
    cart.addLaptop(dellLaptop)
    cart.addLaptop(appleLaptop)
