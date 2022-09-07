from faker import Faker
fake = Faker(["pl_PL"])

class BaseContact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"{self.name} {self.phone} {self.email} {self.company} {self.job}"
    def contact(self):
        return f"Wybieram numer prywatny: {self.phone} i dzwonię do {self.name}."
    def business_contact(self):
       return f"Wybieram numer służbowy: {self.business_phone} i dzwonię do {self.name}."
    @property
    def label_length(self):
        return len(self.name) - self.name.count(' ')

class BusinessContact(BaseContact):
    def __init__(self, name, phone, email, company, job, business_phone):
        super().__init__(name, phone, email)
        self.company = company
        self.job = job
        self.business_phone = business_phone

person = BusinessContact(name=fake.name(), phone=fake.phone_number(), email=fake.email(), company=fake.company(), job=fake.job(), business_phone=fake.phone_number())

print(person)
print(person.contact())
print(person.business_contact())
print(person.label_length)

