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