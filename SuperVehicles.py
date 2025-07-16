# Original vehicle classes 
class Vehicle:
    def __init__(self, name: str, mpg: float):
        self.name = name        # Vehicle type name, e.g., "Car"
        self.mpg = mpg          # Fuel efficiency in miles per gallon

    def fuel_needed(self, distance: float) -> float:
        # Calculate gallons of fuel- what is needed to travel distance
        return distance / self.mpg

    def description(self) -> str:
        # Return a string describing the vehicle's fuel efficiency
        return f"{self.name} gets {self.mpg} miles per gallon."

# vehicle subclass inherits from Vehicle but we set mpg + name
class Car(Vehicle):
    def __init__(self):
        super().__init__("Car", 30)

# Truck subclass  from Vehicle, mpg and name
class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck", 15)

# Motorcycle subclass  from Vehicle, mpg and name
class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("Motorcycle", 50)

# Bus subclass from Vehicle mpg and name
class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", 8)


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#

if __name__ == "__main__":

    # Create a Car object and print its description and fuel needed for 120 miles
    car = Car()
    print(car.description())                 # Prints: Car gets 30 miles per gallon.
    print(car.fuel_needed(120))              # Prints: 4.0 (120 miles / 30 mpg)
    
    # Create a Truck object and print its description and fuel needed for 120 miles
    truck = Truck()
    print(truck.description())               # Prints: Truck gets 15 miles per gallon.
    print(truck.fuel_needed(120))            # Prints: 8.0 (120 miles / 15 mpg)