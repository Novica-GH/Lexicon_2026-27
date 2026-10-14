Markdown

# Hotel Booking Management System

A modular, CLI-based Python application designed to manage hotel room reservations, track customer records, and summarize operational metrics following Object-Oriented Programming (OOP) principles.

## Features & Main Functionality

* **Room Management:** Supports multiple room types (`StandardRoom`, `Executive/FamilyRoom`, `SuiteRoom`) with dynamic pricing and sea-view surcharges, as well as supplements for luxury suites and suites with Jacuzzis.
* **Customer Management:** Tracks standard and `VIPCustomer` accounts with automatic discount application.
* **Booking Operations:** Create, manage, check-in, and cancel bookings while ensuring room availability.
* **Custom Exception Handling:** Prevents invalid operational states (`RoomNotFoundError`, `CustomerNotFoundError`, `BookingConflictError`).
* **System Analytics:** Generates real-time financial summaries, total active bookings, and room occupancy status.

## How to Run the Program

1. **Copy or Download** a part of repository: Lexicon_2026-27/Python Fundamentals/2. PROJECT - Py Fundamenals/MODUL_hotel_booking_system  to your local machine.
2. Ensure you have at least **Python 3.14** installed.
3. Open your terminal or command prompt in the root project folder (`MODUL_hotel_booking_syste`).
4. Run the application  - using the terminal (Ctrl+ö)
```bash
   python main/main.py