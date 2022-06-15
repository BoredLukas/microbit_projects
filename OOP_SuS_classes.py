from datetime import date

class Person:
    def __init__(self, _name, _birthday, _adress, _type, _klass, _position):
        self.name = _name
        self.birthday = _birthday
        self.adress = _adress
        self.type = _type
        self.klass = _klass
        self.position = _position

    def get_info(self):
        if f"{self.type}" == "LP":
            return f"Name: {self.name}, Geburtstag: {self.birthday}, Adresse: {self.address}, Typ: {self.type}, Standort: {self.position}"
        elif f"{self.type}" == "STU":
            return f"Name: {self.name}, Geburtstag: {self.birthday}, Adresse: {self.address}, Typ: {self.type}, Klasse: {self.klass}"
    
    def get_age(self): #not done
        today = date.today()
        year = date.strftime("%Y")
        b_year = self.birthday[5:]
        age = year - b_year
        if 
        return(age)

    def change_klass(self,x=1):
        self.klass += 1
        if self.type == "STU":
            return self.klass
        else:
            return "fehler"
    
print(change_klass(sca))