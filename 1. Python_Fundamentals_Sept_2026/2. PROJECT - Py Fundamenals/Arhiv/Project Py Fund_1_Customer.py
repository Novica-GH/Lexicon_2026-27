#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 28 - Oktober 2 2026                                                            *
#                              P R O J E C T - Python Fundamentals                          *
#                                                                                           *
#            Python Fundamentals - slut PROJECT - Option 3 - Booking System (HOTEL)         *
#                       
#          PART II -  Module solution - CLASS CUSTOMER                                      *
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
#*******************************************************************************************

        

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