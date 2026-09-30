#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 28 2026 -                                                                      *
#                              P R O J E C T - Python Fundamentals                          *
#                                                                                           *
#            Python Fundamentals - slut PROJECT - Option 3 - Booking System (HOTEL)         *
#                                                                                           *
#                                                                                           *
#********************************************************************************************


#********************************************************************************************
# 
#   OPTION 3 - Booking System
# 
#    -  Build a Python program for managing bookings.
#    -  You decide what kind of booking system you want to create. 
#    -  It could be used for (hotel rooms), sports facilities, meeting rooms, activities, 
#       appointments or another type of resource or service. 
#    -  The system should contain different types of objects that interact with each other
#    -  For example, a booking could connect a customer with something that can be bokat.
#    -  Bookings should have meaningful behaviour. They might be created, cancelled, changed
#       or checked in different ways. 
#    -  The system should keep track of its current state while the program is running. 
#    -  You decide how bookings, customers, resources and other parts of your system 
#       should be represented and how they relate to each other.
#
#    -  No database or permanent data storage is required. The data only needs to exists  
#       while program is running.
#
#       Possible ideas
#
#       - diferent types of bookable resources or services
#       - customers
#       - availability
#       - booking status
#       - cancellation
#       - preventing conflicting bookings
#       - prices or costs
#       - different booking rules
#       - searching and filtering bookings
#       - statistics
#       - summaries of available and booked resources
#
#
#*******************************************************************************************



#***********************************************************************************************
#
#                                   CORE EXPECTATIONS
#
#   1.  Build a Complete and Connected Program  
#   2.  Use Object-Oriented Programming 
#   3.  Create Relationships and Interactions Between Objects  
#   4.  Actions Should Affect the State of Your System  
#   5.  Work With Collections of Data or Objects
#   6.  Include Meaningful Program Logic
#   7.  Handle Invalid or Unreasonable Actions   
#   8.  Organize the Project Into Multiple Python Modules    
#   9.  Make the Program Runnable and Demonstrable   
#   10. Use Git Throughout the Project 
#
#       -   Add basic booking functionality
#       -   Prevent conflicting bookings  
#       -   Add visitor interactions  
#       -   Implement character  health system          
#       -   Refactor shared behaviour       
#       -   Fix negative enery bug   
#
#***********************************************************************************************

         

#************************************************************************************************
#                                  HOTEL - ASTORIA - Managing booking Project (Reception++)
#************************************************************************************************

# For the begining I need just: 
#
#   -   Customer (Standard/VIP or [Business/Leisure (Turists) or Tour Groups/Leisure Groups/Transit guests)]
#   -   Room (Standard room/Suite )
#   -   Booking ()
#   -   Hotel Manager (the connection between the previous 3 classes)
#   -   Main part - Interactive part - with demonstration all we have for Hotel Managing - 
# 


#               +++++++++++++++++++++   CLASSES   ++++++++++++++++++++++

class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name  
        self.email = email

    def get_discount_rate(self):
        return 0.0  # For standard customers there isn't any discount

    def __str__(self):
        return f"Customer: [ID: {self.customer_id}], name: {self.name}, e-mail: ({self.email})"


class VIPCustomer(Customer):  # subclass/child
    def __init__(self, customer_id: int, name: str, email: str, discount_rate: float = 0.15):
        super().__init__(customer_id, name, email)
        self.discount_rate = discount_rate

    def get_discount_rate(self):
        return self.discount_rate

    def __str__(self):
        base_info = super().__str__()
        return f"[VIP] {base_info}, Discount: {int(self.discount_rate * 100)}%"



class CustomerNotFoundError(Exception):   # Reserved for the time been - #7 from the Project.
    """Raised when a specified customer ID is not found."""      # Classic docstring for Python...
    pass


# customer1 = Customer(1212, "Ada","ada.ericsson@az.se")
# customer2 = Customer(1313, "Bob", "bob@bob.se") 
# customer3 = Customer(1414, "Grace", "grace@grace.net")

# customerV = VIPCustomer(5155, "Mr.Been", "rowanatkinson@mr_been.com",0.15)
# customerV_2 = VIPCustomer(5255, "Mrs Foley", "mf@foley.org")

# print()
# print(customer1)   # Customer [ID: 1212] Ada (ada.ericsson@az.com)
# print(customerV)   # [VIP] Customer: [ID: 5155], name: Mr.Been, e-mail: (rowanatkinson@mr_been.com), Discount: 15% 
# print()

#------------------------------------------------





class Room:
    def __init__(self, room_number: int, base_price_per_night: float):
        self.room_number = room_number
        self.base_price_per_night = base_price_per_night
        self.is_clean = True

    def calculate_price(self, nights: int):  #float
        return self.base_price_per_night * nights

    def get_room_type(self):
        return " Room in Hotel Astoria"

    def __str__(self):   # def for print / method - return always string
        return f"Room {self.room_number} ({self.get_room_type()}) - {self.base_price_per_night:.2f} kr/night "

# print()
# room1 = Room(1004,2000)
# room2 = Room(1005, 2200)
# room3 = Room(1006,2400)

# price_room1 = room1.calculate_price(5)
# print(price_room1)               # 10000  (for 5 nights)
# print(room1)                     # Room 4 ( Room in Hotel Astoria) - 2000.00 kr/night
# print()



class StandardRoom(Room):       # subclass/child
    def __init__(self, room_number: int, base_price_per_night: float, sea_view: bool = False):
        super().__init__(room_number, base_price_per_night)
        self.sea_view = sea_view

    def get_room_type(self):
        return "Standard Room"

    def __str__(self):
        sea_view_str = "with Sea view" if self.sea_view else "Park view"
        return f"{super().__str__()} [{self.sea_view}]"


# room_standard_1 = StandardRoom(1007, 1000)
# room_standard_2 = StandardRoom(1008, 1200)
# room_standard_3 = StandardRoom(1009, 1300)

# price_room_standard_1 = room_standard_1.calculate_price(11)
# print(price_room_standard_1)         # 11000  ( 11 nights x 1000 kr)
# print(room_standard_1)               # Room 7 (Standard Room) - 1000.00 kr/night  [False]
# print()


class SuiteRoom(Room):      # subclass/child
    def __init__(self, room_number: int, base_price_per_night: float, includes_jacuzzi: bool = True):
        super().__init__(room_number, base_price_per_night)
        self.includes_jacuzzi = includes_jacuzzi

    def get_room_type(self):
        return "Suite Room"

    def calculate_price(self, nights: int):
        luxury_tax = 1000.0   # Suites include a luxury charge
        return (self.base_price_per_night + luxury_tax) * nights

    def __str__(self):
        jacuzzi_str = "with Jacuzzi" if self.includes_jacuzzi else "no Jacuzzi"
        return f"{super().__str__()} [{jacuzzi_str}]"


class RoomNotFoundError(Exception):      # Reserved for the time been - #7 from the Project.
    """Raised when a specified room number is not found."""    # Classic docstring for Python...
    pass



# suite_1 = SuiteRoom(1001, 5000)
# suite_2 = SuiteRoom(1002, 6000)
# suite_3 = SuiteRoom(1003, 7000)

# price_suite_1 = suite_1.calculate_price(7) # 7 nights
# print(price_suite_1)            # 42000.0   [7 nights * (price+lux_tax)]
# print(suite_1)                  # Room 1 (Suite Room) - 5000.00 kr/night  [with Jacuzzi]
# print()
#-----------------------------------------





class Booking:
    STATUS_CONFIRMED = "Confirmed"
    STATUS_CHECKED_IN = "Checked In"
    STATUS_CANCELLED = "Cancelled"

    def __init__(self, booking_id: int, customer: Customer, room: Room, nights: int):
        if nights <= 0:
            raise ValueError("Booking nights must be greater than zero.")  # Varning - ValueError

        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.nights = nights
        self.status = self.STATUS_CONFIRMED
        self.total_cost = self._calculate_total()

    def _calculate_total(self):   # internal/Protected method (begining with _) and it is used just by this Class. We don't call it outside of this Class. 
        raw_price = self.room.calculate_price(self.nights)                  # Standard convetion in Python
        discount = self.customer.get_discount_rate()            # This method uses constructor __init__ like help method (not by user)
        return raw_price * (1.0 - discount)

    def check_in(self):
        if self.status != self.STATUS_CONFIRMED:
            raise ValueError(f"Cannot check in a booking with status '{self.status}'.")
        self.status = self.STATUS_CHECKED_IN

    def cancel(self):
        if self.status == self.STATUS_CHECKED_IN:
            raise ValueError("Cannot cancel a booking that is already checked in.")
        self.status = self.STATUS_CANCELLED

    def __str__(self):
        return (
            f"Booking #{self.booking_id} [{self.status}] | "
            f"{self.customer.name} -> Room {self.room.room_number} | "
            f"Nights: {self.nights} | Total: {self.total_cost:.2f} kr"
        )


class BookingConflictError(Exception):       # Reserved for the time been - #7 from the Project.
    """Raised when attempting to book an already occupied or reserved room."""  # Classic docstring for Python...
    pass


booking1 = Booking(2609291, customer1, rum1, 3)             # Booking #2609291 [Confirmed] | Ada -> Room 4 | Nights: 3 | Total: 6000.00 kr
booking2 = Booking(2609292, customerV, suite_1, 7 )         # Booking #2609292 [Confirmed] | Mr.Been -> Room 1 | Nights: 7 | Total: 35700.00 kr
booking3 = Booking(2609293, customer2, rum_standard_2, 4)   # Booking #2609293 [Confirmed] | Bob -> Room 8 | Nights: 4 | Total: 4800.00 kr
booking4 = Booking(2609294, customerV_2, suite_3, 21)       # Booking #2609294 [Confirmed] | Mrs Foley -> Room 3 | Nights: 21 | Total: 142800.00 kr

bookings = [booking1,booking2, booking3, booking4]


# for boking in bookings:
#     print(boking)

# print()

#--------------------------------------------------------------


#   -   Hotel Manager (the connection between the previous 3 classes)


class HotelManager:
    def __init__(self, hotel_name: str):   # I can add Hotel Astoria, but this is more flexibile way
        self.hotel_name = hotel_name
        self.rooms: List[Room] = []             # I make lists for rooms, customers and bookings here
        self.customers: List[Customer] = []
        self.bookings: List[Booking] = []
        self._next_booking_id = 10001        # default booking id number (think: 260928001 - start with date and 001-999 per day max)

    def add_room(self, room: Room):         
        self.rooms.append(room)

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def find_room(self, room_number: int):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        raise RoomNotFoundError(f"Room {room_number} does not exist.")

    def find_customer(self, customer_id: int):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        raise CustomerNotFoundError(f"Customer with ID {customer_id} does not exist.")

    def is_room_available(self, room_number: int):     # yes/no True/Fales -> boolean
        for booking in self.bookings:
            if booking.room.room_number == room_number and booking.status in [Booking.STATUS_CONFIRMED, Booking.STATUS_CHECKED_IN]:
                return False
        return True

    def create_booking(self, customer_id: int, room_number: int, nights: int):      # returns booking
        customer = self.find_customer(customer_id)   # 2 objects of classes Customer and Room are created here
        room = self.find_room(room_number)

        if not self.is_room_available(room_number):   # Prevent conflicting bookings and givs ConflictError
            raise BookingConflictError(f"Room {room_number} is currently occupied or already reserved.")

        booking = Booking(self._next_booking_id, customer, room, nights)   # creates one object from class Booking
        self.bookings.append(booking)
        self._next_booking_id += 1          # think about ... date001 in form int
        return booking

    def get_available_rooms(self):     # returns a list of available rooms
        return [room for room in self.rooms if self.is_room_available(room.room_number)]

    def generate_summary(self):             # returns a dictionary here with info about bookings...
        active_bookings = [b for b in self.bookings if b.status != Booking.STATUS_CANCELLED]
        total_revenue = sum(b.total_cost for b in active_bookings)
        return {
            "total_rooms": len(self.rooms),
            "available_rooms": len(self.get_available_rooms()),
            "total_active_bookings": len(active_bookings),
            "total_revenue": total_revenue
        }


#----------------------------------------------------------------------------------
#***********************************************************************************


# Main part - Interactive part - with demonstration all we have for Hotel Managing - 


def start_sample_data(manager: HotelManager):    
    # Adding rooms
    manager.add_room(SuiteRoom(1001, 9000.0, includes_jacuzzi=True))
    manager.add_room(SuiteRoom(1002, 7000.0, includes_jacuzzi=True))
    manager.add_room(SuiteRoom(1003, 5000.0, includes_jacuzzi=False))

    manager.add_room(Room(1004, 1000.0, has_balcony=False))
    manager.add_room(Room(1005, 1100.0, has_balcony=False))
    manager.add_room(Room(1006, 1700.0, has_balcony=True))

    manager.add_room(StandardRoom(1007, 1000.0, has_balcony=False))
    manager.add_room(StandardRoom(1008, 1300.0, has_balcony=True))
    manager.add_room(StandardRoom(1009, 1500.0, has_balcony=True))
    
    #   suite_1 = SuiteRoom(1001, 5000)
    #   suite_2 = SuiteRoom(1002, 6000)
    #   suite_3 = SuiteRoom(1003, 7000)

    #   room1 = Room(1004,2000)
    #   room2 = Room(1005, 2200)
    #   room3 = Room(1006,2400)

    #   room_standard_1 = StandardRoom(1007, 1000)
    #   room_standard_2 = StandardRoom(1008, 1200)
    #   room_standard_3 = StandardRoom(1009, 1300)


    # Adding customers
    manager.add_customer(Customer(1, "Ada Ericsson", "ada@ericsson.se"))
    manager.add_customer(Customer(2, "Bob Smith", "bob@smith.com"))
    manager.add_customer(Customer(3, "Grace Wourth", "gracee@wourth.com"))
      
    manager.add_customer(VIPCustomer(4, "Mr.Been", "rowanatkinson@mr_been.com", discount_rate=0.20))

    #   customer1 = Customer(1212, "Ada","ada.ericsson@az.se")
    #   customer2 = Customer(1313, "Bob", "bob@bob.se") 
    #   customer3 = Customer(1414, "Grace", "grace@grace.net")

    #   customerV = VIPCustomer(5155, "Mr.Been", "rowanatkinson@mr_been.com",0.15)
    #   customerV_2 = VIPCustomer(5255, "Mrs Foley", "mf@foley.org")


def run_project():
    manager = HotelManager("Hotel Astoria")
    start_sample_data(manager)

    print(f"=== Welcome to {manager.hotel_name} Management System ===")

    while True:
        print("\n   --- Main Menu ---\n")
        print("1. View All Rooms")
        print("2. View Available Rooms")
        print("3. Create New Booking")
        print("4. View All Bookings")
        print("5. View System Statistics")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            print("\n-- All Rooms --")
            for room in manager.rooms:
                print(room)

        elif choice == "2":
            print("\n-- Available Rooms --")
            avail = manager.get_available_rooms()
            if not avail:
                print("No rooms currently available.")
            else:
                for room in avail:
                    print(room)

        elif choice == "3":
            try:
                c_id = int(input("Enter Customer ID: "))
                r_num = int(input("Enter Room Number: "))
                nights = int(input("Enter Number of Nights: "))

                booking = manager.create_booking(c_id, r_num, nights)
                print(f"\n[SUCCESS] Booking Created Successfully!\n{booking}")
            except (ValueError, BookingConflictError, RoomNotFoundError, CustomerNotFoundError) as e:
                print(f"\n[ERROR] Failed to create booking: {e}")

        elif choice == "4":
            print("\n-- All Bookings --")
            if not manager.bookings:
                print("No bookings found.")
            else:
                for b in manager.bookings:
                    print(b)

        elif choice == "5":
            stats = manager.generate_summary()
            print("\n-- System Summary --")
            print(f"Total Rooms:          {stats['total_rooms']}")
            print(f"Available Rooms:      {stats['available_rooms']}")
            print(f"Active Bookings:      {stats['total_active_bookings']}")
            print(f"Total Active Revenue: ${stats['total_revenue']:.2f}")

        elif choice == "6":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    run_project()


















#****************************************************************************************************
#  
#   FURTHER DEVELOPMENT
# 
#   ..........
# 
# 
# 
# f
#****************************************************************************************************



#************************************************************************************************
#                                  HOTEL - ASTORIA - parts - all att one place:
#************************************************************************************************


#*************************************
#     PART 1 - PERSONS: - for Very, very big PROJECT... but I need now just a part of all this to begin...
#**********************************

#    1. Employies:  Reception / Manager / Stuff / Service / Waiter / Lichen-chef / Lift boy / Garage personal

#    2. Users:      Simple / Pairs / Groups ( business groups, athletes and coaches, students (with techers or without)

#    3. Places by level of impotance: 1. Reception/Room(floor);  2. Apartman/ Restaurang  3. Kitchen/Elevator/Pool/Gym/Pool/Garage
 
#   4. states and behaviors:    


#PART 3 - Places   - for VERY VERY BIG PROJECT.....
#*******************************************************************************************************

# Reception     - base level
# Room          - base level
# Floor         - base level

# Apartman      - level 2
# Restaurang    - level 2

# Elevator(Hiss)- level 3
# Pool          - level 3
# Jim           - level 3
# Garage        - level 3
# Kitchen       - level 3


# **********************************  END of PROJECT ********************************************************