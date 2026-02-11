#Importing Computer class 
from Computer import Computer
from typing import Dict, Optional
class ResaleShop:

    # What attributes will it need?
    inventory: list = []
    computer: Dict = ""
    new_price: int = 0
    new_os: Optional[str] = None

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    def buy(self, computer):
        self.inventory.append(computer)
    
    def update_price(self, computer, new_price):
        if computer in inventory:
            self.computer["price"] = new_price
        else:
            print("Computer not found. Cannot update price.")

    def sell(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
        else: 
            print("Computer not found. Please select another item to sell.")

    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'{item["description"]} -- Processor Type: {item["processor_type"]} Hard Drive Capacity: {item["hard_drive_capacity"]} Memory: {item["memory"]} Operating System: {item["operating_system"]} Year Made: {item["year_made"]} Price:  {item["price"]}')
        else:
            print("No inventory to display.")

    def refurbish(self, computer, new_os = None):
        if computer in self.inventory:
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Computer not found. Please select another item to refurbish.")
