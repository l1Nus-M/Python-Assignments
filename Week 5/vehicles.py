from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_moving = False

    @abstractmethod
    def move(self):
        pass

    def stop(self):
        self.is_moving = False
        return f"{self.name} has stopped."

    def get_speed(self):
        return f"Current speed: {self.speed} km/h"

    def __str__(self):
        return f"{self.name} (Speed: {self.speed} km/h)"


class Car(Vehicle):
    def move(self):
        self.is_moving = True
        return f"🚗 {self.name} is driving on the road at {self.speed} km/h"


class Plane(Vehicle):
    def move(self):
        self.is_moving = True
        return f"✈️ {self.name} is flying through the sky at {self.speed} km/h"


class Boat(Vehicle):
    def move(self):
        self.is_moving = True
        return f"⛵ {self.name} is sailing on the water at {self.speed} km/h"


class Bicycle(Vehicle):
    def move(self):
        self.is_moving = True
        return f"🚲 {self.name} is pedaling on the path at {self.speed} km/h"


class Train(Vehicle):
    def move(self):
        self.is_moving = True
        return f"🚂 {self.name} is chugging along the tracks at {self.speed} km/h"


# Example usage
if __name__ == "__main__":
    # Create different vehicles
    vehicles = [
        Car("Tesla Model S", 120),
        Plane("Boeing 747", 900),
        Boat("Sailboat", 15),
        Bicycle("Mountain Bike", 25),
        Train("Express Train", 200)
    ]

    # Demonstrate polymorphism
    print("Let's see how different vehicles move:")
    print("-" * 50)
    
    for vehicle in vehicles:
        print(vehicle.move())
        print(vehicle.stop())
        print(vehicle.get_speed())
        print("-" * 50)

    # Demonstrate string representation
    print("\nVehicle Information:")
    for vehicle in vehicles:
        print(vehicle) 
