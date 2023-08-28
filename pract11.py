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

    def getGPU(self):
        return self.gpu

    def setGPU(self, gpu):
        if gpu in self.gpuOptions:
            self.gpu = gpu
            self.basePrice += self.gpuOptions[gpu]

    def getPrice(self):
        price = super().getPrice()
        priceOfGPU = self.gpuOptions[self.gpu]
        price = self.basePrice + priceOfGPU
        return price

    def __str__(self):
        output = "{} Gaming Laptop with {} GB RAM and {} GPU".format(
            self.brand, self.ram, self.gpu)
        output += " priced at £{}".format(self.getPrice())
        return output


def testGamingLaptop():
    gamingLaptop = GamingLaptop("Alienware", 1499.99)
    print("gaming laptop's brand is ", gamingLaptop.getBrand())
    print("gaming laptop's RAM is ", gamingLaptop.getRam())
    print("gaming laptop's GPU is ", gamingLaptop.getGPU())
    print("gaming laptop's price is ", gamingLaptop.getPrice())

    gamingLaptop.setRam(32)
    gamingLaptop.setGPU("NVIDIA RTX 3070")
    print("gaming laptop's RAM is now ", gamingLaptop.getRam())
    print("gaming laptop's GPU is now ", gamingLaptop.getGPU())

    print(gamingLaptop)


def testLaptop():
    laptop = Laptop("Dell", 999.99)
    print("laptop's brand is ", laptop.getBrand())
    print("laptop's RAM is ", laptop.getRam())
    print("laptop's price is ", laptop.getPrice())

    laptop.setRam(16)
    print("laptop's RAM is now ", laptop.getRam())
    print("laptop's price is now ", laptop.getPrice())

    print(laptop)
