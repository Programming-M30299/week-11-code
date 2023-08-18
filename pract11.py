class Laptop:
    def __init__(self, brand, basePrice):
        self.brand = brand
        self.basePrice = basePrice
        self.ram = 8
        self.ramOptions = {
            4: 0,
            8: 50,
            16: 100,
            32: 200
        }

    def getBrand(self):
        return self.brand

    def getRam(self):
        return self.ram

    def setRam(self, ram):
        if ram in self.ramOptions:
            self.ram = ram
            self.basePrice += self.ramOptions[ram]

    def getPrice(self):
        priceOfRam = self.ramOptions[self.ram]
        price = self.basePrice + priceOfRam
        return price

    def __str__(self):
        output = "{} Laptop with {} GB RAM".format(self.brand, self.ram)
        output += " priced at £{}".format(self.getPrice())
        return output


def testLaptop():
    laptop = Laptop("Dell", 999.99)
    print("The {} laptop with {} GB RAM costs £{}".format(
        laptop.getBrand(), laptop.getRam(), laptop.getPrice()))

    laptop.setRam(16)
    print("The RAM is now {} and the laptop costs £{}".format(
        laptop.getRam(), laptop.getPrice()))

    print(laptop)
