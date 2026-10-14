#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 28 - Oktober 2 2026                                                            *
#                              P R O J E C T - Python Fundamentals                          *
#                                                                                           *
#            Python Fundamentals - slut PROJECT - Option 3 - Booking System (HOTEL)         *
#                       
#                   PART II -  Module solution - CLASS BOOKING  )                           *
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
#------------------------------------------------------------------------------------------------------


from models.customer import Customer
from models.room import Room


class Booking:                          # Create next 4 lists down for better statistics... More oporynity in MENY:   (DONE):
    STATUS_CONFIRMED  = "Confirmed"        # Save all confirmed bookings in one separat list:    confirmed_bookings      NO
    STATUS_CHECKED_IN = "Checked In"       # Save all checked in bookings in one separat list:   checked_in_bookings     NO
    STATUS_CANCELLED  = "Cancelled"        # Save all canceled bookings in one separat list:     canceled_bookings       NO
    STATUS_DELETED    = "Deleted"          # Save all deleted bookings in one separat list:      deleted_bookings        NO

    def __init__(self, booking_id: int, customer: Customer, room: Room, nights: int):
        if nights <= 0:
            raise ValueError("Booking nights must be greater than zero.")  # Varning for invalid nights number - ValueError

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

    def deleted(self):                              # Both canceled and deleted should be deleted from booking, but it happends in defferent situations...
        if self.status == self.STATUS_CHECKED_IN:
            raise ValueError("Cannot delete a booking that is checked in and not payed.")
        self.status = self.STATUS_DELETED

    def __str__(self):
        return (
            f"Booking #{self.booking_id} [{self.status}] | "
            f"{self.customer.name.ljust(15)} -> Room {self.room.room_number} | "
            f"Nights: {self.nights} | Total: {self.total_cost:.2f} kr"
        )


class BookingConflictError(Exception):       # Reserved for the time been - #7 from the Project.
    """Raised when attempting to book an already occupied or reserved room."""  # Classic docstring for Python...
    pass

