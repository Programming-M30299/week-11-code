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

    def getLaptops(self):
        return self.laptops

    def getTotal(self):
        return self.total

    def __str__(self):
        output = "Shopping cart contains:\n"
        for laptop in self.laptops:
            output += str(laptop) + "\n"
        output += "Total price is £{}".format(self.total)
        return output


class GamingLaptop(Laptop):
    gpuOptions = {
        "NVIDIA GTX 1650": 0,
        "NVIDIA RTX 3070": 250,
        "NVIDIA RTX 4080": 350,
        "AMD RX 6800M": 280
    }

    def __init__(self, brand, basePrice):
        super().__init__(brand, basePrice)
        self.gpu = "NVIDIA GTX 1650"


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

    # laptops = cart.getLaptops()
    # print("Shopping cart contains:")
    # for laptop in laptops:
    #     print(laptop)

    # print("Total price is £{}".format(cart.getTotal()))

    print(cart)


def testGamingLaptop():
    gamingLaptop = GamingLaptop("Razer", 2399.99)
    print("Gaming laptop's brand is", gamingLaptop.getBrand())
    print("Gaming laptop's price is", gamingLaptop.getPrice())
    print("Gaming laptop's ram is", gamingLaptop.getRam())
    print(gamingLaptop)