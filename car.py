class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"Вот такой бренд: {self.brand}, вот такая модель: {self.model}, новехонькая: {self.year}")

red_car = Car("pipi", "pupur", 2021)
red_car2 = Car("pipi2", "pupur2", 2022)
red_car3 = Car("pipi3", "pupur3", 2023)

red_car.print_car_info()
red_car2.print_car_info()
red_car3.print_car_info()
