#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 28 - Oktober 2 2026                                                            *
#                              P R O J E C T - Python Fundamentals                          *
#                                                                                           *
#            Python Fundamentals - slut PROJECT - Option 3 - Booking System (HOTEL)         *
#                       
#                   PART II -  Module solution - CLASS HotelManager                         *
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
#------------------------------------------------------------------------------------------------



from typing import List, Optional
from models.customer import Customer
from models.room import Room
from models.booking import Booking
from utils.exceptions import BookingConflictError, RoomNotFoundError, CustomerNotFoundError



class HotelManager:
    def __init__(self, hotel_name: str):   # I can add Hotel Astoria here now, but this is more flexibile way
        self.hotel_name = hotel_name
        self.rooms:     List[Room] = []             # I make lists for rooms, customers and bookings here
        self.customers: List[Customer] = []
        self.bookings:  List[Booking] = []
        self.confirmed_bookings:  List[Booking] = []    # More oporynity in new extra MENY: for extra statistics
        self.checked_in_bookings: List[Booking] = []    #               -   ||  -
        self.canceled_bookings:   List[Booking] = []    #               -   ||  -
        self.deleted_bookings:    List[Booking] = []    #               -   ||  -
        self._next_booking_id = 10001        # default booking id number (idea:260928001 - start with date and 001-999 per day max) for Next version 2.0

    def add_room(self, room: Room):             # This method DO something (adds room in the room list) - not return something...
        self.rooms.append(room)                 # This is Action method (if i even write return - it is going to be returned None, that means that action is completed!)

    def add_customer(self, customer: Customer):  # Also Action method thad adds customers in the list of customers
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
    

    def find_booking(self, booking_id: int):            # Find booking
            for booking in self.bookings:
                if booking.booking_id == booking_id:
                    return True
            raise BookingConflictError(f"Booking {booking_id} does not exist.")
    

    def find_nights(self, nights: int):            # Find nights
            for night in self.bookings:
                if night.nights == nights:
                    return True
            raise BookingConflictError(f"Booking for {nights} nights does not exist.")
    

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
        self.bookings.append(booking)       # Action - adds one new booking in the booking list
        self._next_booking_id += 1          # think about ... date001 in form int/
        return booking

    #---------------------------------------DELETE
    
    def delete_booking(self, booking_id: int, customer: Customer, room: Room, nights: int):      # deletes boking if is not checkedIn.
        booking_ok = self.find_booking(booking_id)
        customer_d = self.find_customer(customer)   # 2 objects of classes Customer and Room are created here
        room_d = self.find_room(room)
        nights_ok = self.find_nights(nights)

        booking = Booking(booking_id, customer, room, nights) 

        if booking_ok and (customer == customer_d) and (room == room_d) and nights_ok:
            self.bookings 
            raise BookingConflictError(f"Room {room_number} is avalilable!")
        elif not self.find_customer(customer_id):
            raise CustomerNotFoundError(f"Customer with ID {customer_id} does not exist.")
        else:
            if booking in self.bookings:
                self.bookings.remove(booking)   # delete one object from class Booking
                return booking

    #----------------------------------    

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