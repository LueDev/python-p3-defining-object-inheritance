from vehicle import Vehicle

class Car(Vehicle):
    def go(self) -> str:
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

if __name__ == "__main__":
    fiat = Car(24, 4)
    print(fiat.fill_up_tank())
    print(fiat.go())
    print(Car.__bases__)