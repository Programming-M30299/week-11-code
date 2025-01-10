class Laptop:

    ram_options = {
        4: 0,
        8: 50,
        16: 100,
        32: 200
    }

    def __init__(self, brand, base_price):
        self.brand = brand
        self.base_price = base_price
        self._ram = 4

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, new_ram):
        if new_ram in self.ram_options:  # Use class variable
            self._ram = new_ram

    def calculate_price(self):
        ram_price = self.ram_options[self.ram]
        total_price = self.base_price + ram_price
        return total_price

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM"
        output += f" priced at £{self.calculate_price()}"
        return output
    

class ShoppingCart:

    def __init__(self):
        self.laptops = []
        self.total = 0

    def add_laptop(self, laptop):
        self.laptops.append(laptop)
        laptop_price = laptop.calculate_price()
        self.total += laptop_price

    def __str__(self):
        output = "Shopping cart contains:\n"
        for laptop in self.laptops:
            output += f"{laptop}\n"
        output += f"Total price is £{self.total}"
        return output


class GamingLaptop(Laptop):

    gpu_options = {
        "NVIDIA GTX 1650": 0,
        "NVIDIA RTX 3070": 250,
        "NVIDIA RTX 4080": 350,
        "AMD RX 6800M": 280
    }

    def __init__(self, brand, basePrice):
        super().__init__(brand, basePrice)
        self._gpu = "NVIDIA GTX 1650"

    @property
    def gpu(self):
        return self._gpu
    
    @gpu.setter
    def gpu(self, new_gpu):
        if new_gpu in self.gpu_options:
            self._gpu = new_gpu

    def calculate_price(self):
        gpu_price = self.gpu_options[self.gpu]
        laptop_price = super().calculate_price()
        total_price = laptop_price + gpu_price
        return total_price

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM "
        output += f"and {self.gpu} priced at £{self.calculate_price()}"
        return output


def test_gaming_laptop():
    laptop = GamingLaptop("Razer", 2399.99)
    print(f"Laptop's brand is {laptop.brand}")
    print(f"Laptop's GPU is {laptop.gpu}")
    print(f"Laptop's RAM is {laptop.ram} GB")

    laptop.gpu = "NVIDIA RTX 3070"
    laptop.ram = 16

    print(f"Laptop's price is £{laptop.calculate_price()}")

    print(laptop)


def test_shopping_cart():
    cart = ShoppingCart()
    dell_laptop = Laptop("Dell", 999.99)
    apple_laptop = Laptop("Apple", 1349.00)
    cart.add_laptop(dell_laptop)
    cart.add_laptop(apple_laptop)

    print(f"Shopping cart's total is £{cart.total}")
    print(cart)


def test_laptop():
    laptop = Laptop("Dell", 999.99)
    print(f"Laptop's brand is {laptop.brand}")
    print(f"Laptop's RAM is {laptop.ram} GB")
    print(f"Laptop's price is £{laptop.calculate_price()}")

    laptop.ram = 99  # 'Laptop' has no attribute 'ram'
    print(f"Laptop's RAM is {laptop.ram} GB")

    print(f"Laptop's price is £{laptop.calculate_price()}") # 999.99

    print(laptop)
