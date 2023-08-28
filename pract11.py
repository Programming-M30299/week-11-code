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
        return self.basePrice


def testLaptop():
    laptop = Laptop("Dell", 999.99)
    print("laptop's brand is ", laptop.getBrand())
    print("laptop's RAM is ", laptop.getRam())
    print("laptop's price is ", laptop.getPrice())


testLaptop()
