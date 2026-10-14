#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 28 - Oktober 2 2026                                                            *
#                              P R O J E C T - Python Fundamentals                          *
#                                                                                           *
#            Python Fundamentals - slut PROJECT - Option 3 - Booking System (HOTEL)         *
#                       
#                   PART II -  Module solution -   M A I N  -  P A R T                      *
# simbioza                                                                                   *
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
#----------------------------------------------------------------------------------


# Main part - Interactive part - with demonstration:


import sys
import os

# Add rooh folder (MODUL_hotel_booking_system) to Python 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from services.hotel_manager import HotelManager
from models.customer import Customer, VIPCustomer, CustomerNotFoundError
from models.room import StandardRoom, Room, SuiteRoom, RoomNotFoundError
from models.booking import BookingConflictError



def start_initial_data(manager: HotelManager):    
    # Adding rooms
    manager.add_room(SuiteRoom(1001, 9000.0, includes_jacuzzi=True))
    manager.add_room(SuiteRoom(1002, 7000.0, includes_jacuzzi=True))
    manager.add_room(SuiteRoom(1003, 5000.0, includes_jacuzzi=False))

    manager.add_room(Room(1004, 1000.0))
    manager.add_room(Room(1005, 1100.0))
    manager.add_room(Room(1006, 1700.0))

    manager.add_room(StandardRoom(1007, 1000.0, has_sea_view=False))
    manager.add_room(StandardRoom(1008, 1300.0, has_sea_view=True))
    manager.add_room(StandardRoom(1009, 1500.0, has_sea_view=True))
    
  
    # Adding customers ()
    manager.add_customer(Customer(1, "Ada Ericsson", "ada@ericsson.se"))1
    manager.add_customer(Customer(2, "Bob Smith", "bob@smith.com"))
    manager.add_customer(Customer(3, "Grace Wourth", "gracee@wourth.com"))
      
    manager.add_customer(VIPCustomer(4, "Mr.Been", "rowanatkinson@mr_been.com", discount_rate=0.20))

 

def main():
    manager = HotelManager("Hotel Astoria")
    start_initial_data(manager)

    print()
    print("============================================================")
    print(f"\n    ===   Welcome to {manager.hotel_name} Management System   ===\n")

    while True:
        print("============================================================")
        print("\n                    --- Main Menu ---\n")
        print("                 1. View All Rooms")
        print("                 2. View Available Rooms")
        print("                 3. Create New Booking")
        print("                 4. View All Bookings")
        print("                 5. View System Statistics")
        print("                 6. Exit")
        print("_____________________________________________________________")
        choice = input(f"\nSelect an option (1-6): ").strip()
      

        if choice == "1":           #  1. View All Rooms
            print("============================================================")
            print(f"\n              --- All Rooms in {manager.hotel_name}  ---\n")
            for room in manager.rooms:
                print(room)

        elif choice == "2":     #  2. View Available Rooms
            print("============================================================")
            print(f"\n              --- Available Rooms in {manager.hotel_name} ---\n")
            avail = manager.get_available_rooms()
            if not avail:
                print(f"\nSorry, no rooms currently available in {manager.hotel_name}.\n")
            else:
                for room in avail:
                    print(room)

        elif choice == "3":         # 3. Create New Booking
            try:
                c_id = int(input("Enter Customer ID: "))
                r_num = int(input("Enter Room Number: "))
                nights = int(input("Enter Number of Nights: "))

                booking = manager.create_booking(c_id, r_num, nights)
                print("============================================================")
                print(f"\n[SUCCESS] Booking Created Successfully!\n{booking}")
            except (ValueError, BookingConflictError, RoomNotFoundError, CustomerNotFoundError) as e:
                print("============================================================")
                print(f"\n[ERROR] Failed to create booking: {e}")

 

        elif choice == "4":         #  5. View All Bookings
            print("============================================================")
            print(f"\n  --- All Bookings in {manager.hotel_name}  ---\n")
            if not manager.bookings:
                print(f"No bookings found!\n")
            else:
                for b in manager.bookings:
                    print(b)

        elif choice == "5":         #  6. View System Statistics
            print("============================================================")
            stats = manager.generate_summary()
            print(f"\n   --- System Summary in {manager.hotel_name}  ---\n")
            print(f"Total Rooms:          {stats['total_rooms']}")
            print(f"Available Rooms:      {stats['available_rooms']}")
            print(f"Active Bookings:      {stats['total_active_bookings']}")
            print(f"Total Active Revenue: {stats['total_revenue']:.2f} kr")

        elif choice == "6":         # 7. Exit
            print("======================================================================================================")
            print(f"\n ... Exiting program. Thank you for your visit. Goodbye and welcome again to {manager.hotel_name}!\n")
            print(f"======================================================================================================\n")
            break
        else:
            print("============================================================")
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
