# define new classes

# class myClassName

'''

    Model for aircraft flights.

'''

class Flight:
    """ A flight with a particular passenger aircraft"""

    #__init__ is not a constructor but an initializer
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number

        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating_plan = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seat_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def num_rows(self):
        return self._num_rows

    def num_seats_per_row(self):
        return self._num_seat_per_row

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seat_per_row])