"""
   Filename: Computer.py
Description: This contains the computer class, and is used in the resale shop inventory. 
     Author: Tensae Mekonnen
       Date: 10 February 2026
       
       Note: Worked on sorting methods and attributes with Elizabeth Sarpong and Jode Redding in discussion.
"""
from typing import Optional
#Computer class
class Computer:
    #Attributes
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: float = 0.0
    new_os: Optional[str] = None

    #Initialization method makes sure all the attributes are set up
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int, new_os: str ):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        self.new_os = new_os

    #Update_price method  to update the price of a computer
    def update_price(self, new_price: int):
        if computer in inventory:
            self.price = new_price
        else:
            print("Computer not found. Cannot update price.")

    #Update_os updates the operating system to whichever one we put in new_os 
    def update_os(self, new_os):
        self.operating_system = new_os
        
        return self 
