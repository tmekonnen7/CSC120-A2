#Imports
from typing import Optional
class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)   
    # description : str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: float = 0.0
    new_os: Optional[str] = None
    # new_price: int = 0

    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int, new_os: str ):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        self.new_os = new_os


    def update_price(self, new_price: int):
        if computer in inventory:
            self.price = new_price
        else:
            print("Computer not found. Cannot update price.")

    def update_os(self, new_os):
        self.operating_system = new_os
        
        return self 

    

    

    
    # What methods will you need?