from uuid import uuid5, NAMESPACE_OID
from enum import Enum

class UserType(Enum):
    Staff   = 0
    Visitor = 1
class User:
    
    def __init__(self, email, password, f_name, l_name, address, user_type):
        self._id        = uuid5(NAMESPACE_OID,
                                f"{self._email}|{self._password}")
        self._email     = email
        self._password  = password
        self._f_name    = f_name
        self._l_name    = l_name
        self._address   = address
        self._user_type = user_type

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

    def get_user_type(self):
        return self._user_type

    def print_details(self):
        print(f"Id: {self._id}")
        print(f"Email: {self._email}")
        print(f"Password: {self._password}")
        print(f"First Name: {self._f_name}")
        print(f"Last Name: {self._l_name}")
        print(f"Address: {self._address}")
        
        if self._user_type == UserType.Staff:
            print("Staff Member")
        elif self._user_type == UserType.Visitor:
            print("User is a visitor")

    def to_json(self):

        user_type = "Staff" if self._user_type == UserType.Staff else "Visitor"

        return {

            "Id": self._id,
            "Email": self._email,
            "Password": self._password,
            "First Name": self._f_name,
            "Last Name": self._l_name,
            "Address": self._address,
            "User Type": user_type
        }