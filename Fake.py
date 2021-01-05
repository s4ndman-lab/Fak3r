import pyfiglet
out = pyfiglet.figlet_format("S4NDMAN-LAB", font="slant")
print(out)
from faker import Faker
fake = Faker()
print (fake.email())
print(fake.country())
print(fake.name())
print(fake.text())
print(fake.latitude(),
      fake.longitude())
print(fake.url())

