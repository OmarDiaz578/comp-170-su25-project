from Birthday import Birthday


class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the
        form (month, day), and a city they live in. Additional fields may
        be added here later. A new object requires only a first and last
        name to instatiate. The remaining fields can be set later using
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.email_address = None
        self.nickname = None
        self.street_address = None
        self.city = None
        self.state = None
        self.zip = None
        self.phone = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def set_city(self, city):
        """Mutator for city."""
        self.city = city
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email_address(self, email_address):
        self.email_address = email_address

    def set_nickname(self, nickname):
        self.nickname = nickname

    def set_street_address(self, street_address):
        self.street_address = street_address

    def set_state(self, state):
        self.state = state

    def set_zip(self, zip):
        self.zip = zip

    def set_phone(self, phone):
        self.phone = phone






    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name
    
    def get_email_address(self):
        return self.email_address
    
    def get_nickname(self):
        return self.nickname 
    
    def get_street_address(self):
        return self.street_address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state
    
    def get_zip(self):
        return self.zip
    
    def get_phone(self):
        return self.phone

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"
