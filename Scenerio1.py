#4. Mobile Store Management System
#Develop a Python application to maintain mobile phone details
#Requirements
#Create a Mobile class with:
#Brand
#Model
#Price
#Categorize mobiles as:
#Premium
#Mid-range
#Budget
#Create a Store class.
#Add mobiles.
#Display all mobiles.
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = float(price)
        self.category = self._categorize()

    def _categorize(self):
        """Categorize the mobile based on its price."""
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 15000:
            return "Mid-range"
        else:
            return "Budget"

    def __str__(self):
        return f"{self.brand} {self.model} | Price: ₹{self.price:,.2f} | Category: {self.category}"


class Store:
    def __init__(self):
        self.inventory = []

    def add_mobile(self, mobile):
        """Add a new mobile to the store's inventory."""
        self.inventory.append(mobile)
        print(f"\nSuccess: '{mobile.brand} {mobile.model}' has been added to the store.")

    def display_mobiles(self):
        """Display all mobiles currently in the store."""
        if not self.inventory:
            print("\nThe store inventory is currently empty.")
            return
        
        print("\n" + "="*50)
        print("CURRENT MOBILE INVENTORY")
        print("="*50)
        for index, mobile in enumerate(self.inventory, start=1):
            print(f"{index}. {mobile}")
        print("="*50)


# ==========================================
# Driver Code / Interactive Menu
# ==========================================
if __name__ == "__main__":
    my_store = Store()
    
    while True:
        print("\n____________Mobile Store Management System ________________")
        print("1. Add a new mobile")
        print("2. Display all mobiles")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            try:
                brand = input("Enter Brand (e.g., Samsung, Apple): ")
                model = input("Enter Model (e.g., Galaxy S23): ")
                price = float(input("Enter Price: "))
                
                new_mobile = Mobile(brand, model, price)
                my_store.add_mobile(new_mobile)
            except ValueError:
                print("\nError: Please enter a valid number for the price.")
                
        elif choice == '2':
            my_store.display_mobiles()
            
        elif choice == '3':
            print("Exiting the Mobile Store Management System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
