class Vehicle:
    CATEGORIES = ("Luxury", "Economy")

    def __init__(self, vehicle_number, brand, price, category):
        if category not in self.CATEGORIES:
            raise ValueError(f"Category must be one of: {', '.join(self.CATEGORIES)}")
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price
        self.category = category

    def __str__(self):
        return (
            f"Vehicle Number: {self.vehicle_number} | Brand: {self.brand} | "
            f"Price: {self.price:.2f} | Category: {self.category}"
        )


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles have been added.")
            return

        for vehicle in self.vehicles:
            print(vehicle)


def main():
    showroom = Showroom()
    categories = {"1": "Luxury", "2": "Economy"}

    while True:
        print("\nVehicle Showroom Management")
        print("1. Add vehicle")
        print("2. Display all vehicles")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            vehicle_number = input("Vehicle number: ").strip()
            brand = input("Brand: ").strip()
            try:
                price = float(input("Price: "))
                if price < 0:
                    raise ValueError
            except ValueError:
                print("Please enter a valid non-negative price.")
                continue

            print("1. Luxury\n2. Economy")
            category = categoriesget(input("Choose a category: ").strip())
            if category is None:
                print("Invalid category.")
                continue

            showroom.add_vehicle(Vehicle(vehicle_number, brand, price, category))
            print("Vehicle added.")
        elif choice == "2":
            showroom.display_vehicles()
        elif choice == "3":
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
