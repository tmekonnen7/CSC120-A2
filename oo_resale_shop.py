"""
   Filename: oo_resale_shop.py
Description: This contains the ResaleShop class, and is used to manage the inventory of computer objects.
     Author: Tensae Mekonnen
       Date: 10 February 2026
       
       Note: Worked on sorting methods and attributes with Elizabeth Sarpong and Jode Redding in discussion.
"""
#Importing Computer class 
from Computer import Computer
from typing import Dict, Optional
class ResaleShop:

    #Attributes
    inventory: list = []
    computer: Dict = ""
    new_price: int = 0
    new_os: Optional[str] = None

    #Constructor creating an empty inventory for this first round 
    def __init__(self):
        self.inventory = []

    #Method for adding a computer to the shop inventory, taking in computer object to add
    def buy(self, computer):
        self.inventory.append(computer)
    
    #Method for updating the price of a computer if it's in the inventory given computer object, and new price
    def update_price(self, computer, new_price):
        if computer in inventory:
            self.computer["price"] = new_price
        else:
            print("Computer not found. Cannot update price.")

    #Method for removing a computer object from the inventory 
    def sell(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
        else: 
            print("Computer not found. Please select another item to sell.")

    #Prints the details of every computer object in the inventory
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'{item["description"]} -- Processor Type: {item["processor_type"]} Hard Drive Capacity: {item["hard_drive_capacity"]} Memory: {item["memory"]} Operating System: {item["operating_system"]} Year Made: {item["year_made"]} Price:  {item["price"]}')
        else:
            print("No inventory to display.")

    #Adjusting price of computer objects depending on year made, and installs new_os, if it is provided.
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
