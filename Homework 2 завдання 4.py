class Device:
    def __init__(self, name: str):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"Пристрій {self.name} увімкнено.")

    def turn_off(self):
        self.is_on = False
        print(f"Пристрій {self.name} вимкнено.")


class Laptop(Device):
    def __init__(self, name: str, model: str):
        super().__init__(name)
        self.model = model

    def turn_on(self):
        super().turn_on()
        print(f"Ноутбук {self.model} завантажує операційну систему...")


class Smartphone(Device):
    def __init__(self, name: str, phone_number: str):
        super().__init__(name)
        self.phone_number = phone_number

    def make_call(self, target_number: str):
        if self.is_on:
            print(f"Телефонуємо на {target_number} з номера {self.phone_number}...")
        else:
            print("Неможливо здійснити дзвінок: смартфон вимкнено!")



if __name__ == "__main__":
    laptop = Laptop("Мій Ноутбук", "Asus")
    phone = Smartphone("Мій Смартфон", "+876547654376")

    print(" Робота з ноутбуком ")
    laptop.turn_on()
    laptop.turn_off()

    print("\n Робота зі смартфоном ")
    phone.make_call("+876547654376")
    phone.turn_on()
    phone.make_call("+887442154654")
    phone.turn_off()