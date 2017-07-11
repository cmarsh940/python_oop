class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12

    def displayAll(self):
        print "Price:", self.price
        print "Speed:", str(self.speed)
        print "Fuel:", str(self.fuel)
        print "Mileage:", str(self.mileage)
        print "Tax:", self.tax
        return self


car1 = Car(19000, "70mph", "Full", "43mpg")
car2 = Car(80000, "43mph", "Half Full", "35mpg")
car3 = Car(30000, "80mph", "Full", "50mpg")
car4 = Car(12000, "100mph", "Empty", "55mpg")
car5 = Car(3000000, "120mph", "Half Full", "160mpg")
car6 = Car(100000, "55mph", "Quarter Tank", "35mpg")


print car1.displayAll()
print car2.displayAll()
print car3.displayAll()
print car4.displayAll()
print car5.displayAll()
print car6.displayAll()
