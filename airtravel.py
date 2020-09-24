"""Model for aircraft flights"""
from pprint import pprint as pp

class Flight:
    """A flight with particular passenger aircraft"""

    def __init__(self,number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()
        
    def number1(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        row, letter = self._parse_seat(seat)
        # rows, seat_letters = self._aircraft.seating_plan()

##        letter = seat[-1]
##        if letter not in seat_letters:
##            raise ValueError(f"Invalid seat letter {letter}")
##
##        row_text = seat[:-1]
##        try:
##            row = int(row_text)

##        except ValueError:
##            raise ValueError(f"Invalid seat row {row_text}")
##
##        if row not in rows:
##            raise ValueError(f"Invalid row number {row}")
##
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")
        
        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat."""

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat{from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)
        # Adds 1 for each None found[Uses Generator]

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number1(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating loacations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")

##class Aircraft:
##
##    def __init__(self, registration, model, num_rows, num_seats_per_row):
##        self._registration = registration
##        self._model = model
##        self._num_rows = num_rows
##        self._num_seats_per_row = num_seats_per_row
##
##    def registration(self):
##        return self._registration
##
##    def model(self):
##        return self._model
##
##    def seating_plan(self):
##        return (range(1, self._num_rows+1),
##                "ABCDEFGHJK"[:self._num_seats_per_row])

class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration
    
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

    
class AirbusA319(Aircraft): # Inheritance
    
##    def __init__(self, registration):
##        self._registration = registration
##
##    def registration(self):
##        return self._registration

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"

##    def num_seats(self):
##        rows, row_seats = self.seating_plan()
##        return len(rows) * len(row_seats)

class Boeing777(Aircraft):
    
##    def __init__(self, registration):
##        self._registration = registration
##
##    def registration(self):
##        return self._registration

    def model(self):
        return "Boeing 777"
    
    def seating_plan(self):
        # seting arrangement for first class
        return range(1, 56), "ABCDEFGHJK"

##    def num_seats(self):
##        rows, row_seats = self.seating_plan()
##        return len(rows) * len(row_seats)

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}"       \
             f"  Flight: {flight_number}" \
             f"  Seat: {seat}"            \
             f"  Aircraft: {aircraft}"    \
             "|"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()

def make_flights():
    # f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22,num_seats_per_row=6))
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A","Guido van Rossum")
    f.allocate_seat("15F","Bjarne Stroustrup")
    f.allocate_seat("15E","Anders Hejlsberg")
    f.allocate_seat("1C","John McCarthy")
    f.allocate_seat("1D","Rich Hickey")

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat("55K","Larry Wall")
    g.allocate_seat("33G","Yukihiro Matsumoto")
    g.allocate_seat("4B","Brian Kernighan")
    g.allocate_seat("4A","Dennis Ritchie")
    
    return f, g
    
    
    
# f = Flight('SN060')
# print(f.number1())
# print(f._number)
# a = Aircraft("G-EUPT", "Airbus A319", num_rows=22,num_seats_per_row=6)
# print(a.registration())
# print(a.model())
# print(a.seating_plan())
# f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22,num_seats_per_row=6))
# print(f.aircraft_model())
# print(pp(f._seating))
# print(f.allocate_seat("12A","Guido van Rossum"))
# print(f.allocate_seat("12A", "Rasmus Lerdorf"))
# print(f.allocate_seat("E27:, "Yukihiro Mastumuto")
# print(f.allocate_seat("DD", "Baby Penguin"))
# print(f._seating)
# from airtravel import make_flight
# print(f = make_flight())
# print(f)
# print(f.relocate_passenger("12A", "15D"))
# print(pp(f._seating))
# print(f.num_available_seats)
# print(f.make_boarding_cards(console_card_printer))
# print(f, g = make_flights())
# print(f.aircraft_model())
# print(g.aircraft_model())
# print(f.num_available_seats)
# print(g.num_available_seats)
# print(g.relocate_passenger("55K", "13G"))
# print(g.make_boarding_cards(console_card_printer))
# a = AirbusA319("G-EZBT")
# print(a.num_seats())
# b = Boeing777("N717AN")
# print(b.num_seats())
