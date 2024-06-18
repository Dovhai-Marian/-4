class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

my_car = Car("Honda", "Civic", 1972)

for _ in range(5):
    my_car.accelerate()
    print(f"Поточна швидкість після прискорення: {my_car.get_speed()} км/год")

for _ in range(5):
    my_car.brake()
    print(f"Поточна швидкість після гальмування: {my_car.get_speed()} км/год")


class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer.extend(a)
        while len(self.buffer) >= 5:
            sum_of_five = sum(self.buffer[:5])
            print(f"Сума наступної п'ятірки: {sum_of_five}")
            self.buffer = self.buffer[5:]

    def get_current_part(self):
        return self.buffer

buffer = Buffer()
buffer.add(1, 2, 3)
print(f"Поточні елементи: {buffer.get_current_part()}")
buffer.add(4, 5, 6)
print(f"Поточні елементи: {buffer.get_current_part()}")
buffer.add(7, 8, 9, 10)
print(f"Поточні елементи: {buffer.get_current_part()}")
buffer.add(11)
print(f"Поточні елементи: {buffer.get_current_part()}")
