class car:
    def __int__(self, name, price):
        self.name = name
        self.price = price
        self.status = False  # Defult

        def start(self):
            if self.status == False:
                self.status = True
            print(f"{self.name} is starting")

    else:
    print("Your car is already started")

    def off(self):
        if self.status:
            self.status = False
        print(f"{self.name} is off now")

        else:
        print("your car is off plz start first")

        car1 = car("BMW", "12000000")

        car1.start()
        car1.start()

        car1.off()
        car1.off()
