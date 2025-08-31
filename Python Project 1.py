class Bus():
    def __init__(self,bus_no,destination,price,seat_no):
        self.bus_no = bus_no
        self.destination = destination
        self.price = price
        self.seat_no = seat_no
    def show_details(self):
        print(f"Bus No:{self.bus_no}")
        print(f"destination:{self.destination}")
        print(f"price:{self.price}")
        print(f"seat_no:{self.seat_no}")

class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Ticket:
    def __init__(self, passenger, bus, seat_no):
        self.passenger = passenger
        self.bus = bus
        self.seat_no = seat_no
    def show_ticket(self):
        print("----Ticket----")
        print(f"Passenger: {self.passenger.name}, Age: {self.passenger.age}")
        print(f"Bus No: {self.bus.bus_no}, Seat: {self.seat_no}")
        print(f"Destination: {self.bus.destination}, Price: {self.bus.price}")

class BusReservationSystem:
    def __init__(self):
        self.buses = []
        self.tickets = []
    def add_bus(self, bus):
        self.buses.append(bus)
    def show_buses(self):
        for bus in self.buses:
            bus.show_details()
    def book_ticket(self, passenger, bus_no):
        for bus in self.buses:
            if bus.bus_no == bus_no and bus.seat_no > 0:
                seat_no = bus.seat_no
                bus.seat_no -= 1
                ticket = Ticket(passenger, bus, seat_no)
                self.tickets.append(ticket)
                print("Ticket booked successfully!")
                return ticket
        print("Bus not found or no seats available.")
        return None

if __name__ == "__main__":
    system = BusReservationSystem()

    # Add buses
    b1 = Bus(101, "Delhi", 500, 3)
    b2 = Bus(202, "Mumbai", 300, 2)
    system.add_bus(b1)
    system.add_bus(b2)

    # Show available buses
    system.show_buses()

    # Book tickets
    p1 = Passenger("Aditya", 22)
    ticket1 = system.book_ticket(p1, 101)
    if ticket1:
        ticket1.show_ticket()


