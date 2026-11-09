#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 28 - Oktober 2 2026                                                            *
#                              P R O J E C T - Python Fundamentals                          *
#                                                                                           *
#            Python Fundamentals - slut PROJECT - Option 3 - Booking System (HOTEL)         *
#                       
#          PART II -  Module solution - CLASS ROOM                                          *
#                                                                                           *
#********************************************************************************************



class Room:
    def __init__(self, room_number: int, base_price_per_night: float):
        self.room_number = room_number
        self.base_price_per_night = base_price_per_night
        self.is_clean = True

    def calculate_price(self, nights: int):  #float
        return self.base_price_per_night * nights

    def get_room_type(self):
        return "Executive/Family Room"

    def __str__(self):   # def for print / method - return always string   
        return f"Room {self.room_number} - {self.get_room_type().ljust(21)} - {self.base_price_per_night:.2f} kr/night "
#                                        # fine print adjustments methods: .ljust(n), .rjust(n) and .center(n)
# print()
# room1 = Room(1004,2000)
# room2 = Room(1005, 2200)
# room3 = Room(1006,2400)

# price_room1 = room1.calculate_price(5)
# print(price_room1)               # 10000  (for 5 nights)
# print(room1)                     # Room 4 ( Room in Hotel Astoria) - 2000.00 kr/night
# print()



class StandardRoom(Room):       # subclass/child
    def __init__(self, room_number: int, base_price_per_night: float, has_sea_view: bool = False):
        super().__init__(room_number, base_price_per_night)
        self.sea_view = has_sea_view

    def get_room_type(self):
        return "Standard Room"

    def __str__(self):
        self.has_sea_view = "With sea view" if self.sea_view else "Park view"
        return f"{super().__str__()} [{self.has_sea_view}]"


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
