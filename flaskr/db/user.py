from uuid import uuid4
class User:
    
    def __init__(self, email, password, f_name, l_name, address):
        self._id        = uuid4()
        self._email     = email
        self._password  = password
        self._f_name    = f_name
        self._l_name    = l_name
        self._address   = address

    def get_id(self):
        return self._id

    def get_email(self):
        return self._email
    
    def get_password(self):
        return self._password

    def get_f_name(self):
        return self._f_name

    def get_l_name(self):
        return self._l_name

    def get_address(self):
        return self._address

    def print_details(self):
        print(f"Id: {self._id}")
        print(f"Email: {self._email}")
        print(f"Password: {self._password}")
        print(f"First Name: {self._f_name}")
        print(f"Last Name: {self._l_name}")
        print(f"Address: {self._address}")

    def to_json(self):
        return {
            "Id": str(self._id),
            "Email": self._email,
            "Password": self._password,
            "First Name": self._f_name,
            "Last Name": self._l_name,
            "Address": self._address
        }