#დავალება1
class Celsius:
    def __init__(self, temperature):
        self.__temperature = temperature
    def get_temp(self):
        return self.__temperature
    def set_temp(self, new_temperature):
        self.__temperature = new_temperature
    def del_temp(self):
        del self.__temperature
    temperature_property = property(get_temp, set_temp, del_temp)

t1 = Celsius(10)
t2 = Celsius(30)
print(t1.temperature_property)
print(t2.temperature_property)

#დავალება2
class Bank_Account:
    def __init__(self, account_name, balance=0):
        self.__account_name = account_name
        self.__balance = balance
    def __str__(self):
        return f"გამარჯობა {self.__account_name}, თქვენ ბალანსზე გაქვთ: {self.__balance} ლარი"
    def get_accountname(self):
        return self.__account_name
    def set_accountname(self, account_name):
        self.__account_name = account_name
    def deposit(self, amount):
        self.__balance += amount
        print(f"ბალანსზე თნხის შეტანა წარმატებით დასრულდა! ბალანსზე გაქვთ {self.__balance} ლარი")
    def withdraw(self,amount1):
        self.__balance -= amount1
        print(f"თანხის გამოტანა შესრულებულია, ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი")


bank1 = Bank_Account("ნინი", 500)
print(bank1)
bank1.deposit(int(input("ნინი შემოიტანე თანხა, რომლის დამატებაც გსურს ანგარიშზე:")))
bank1.withdraw(int(input("ნინი შეიყვანეთ თანხა, რომლის გამოტანაც გსურთ ანგარიშიდან:")))
#დავალება3
from math import sqrt

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distanc(self):
        return sqrt(self.x ** 2 + self.y ** 2)
point1 = Point(3,5)
point2 = Point(6,9)
print(point1.distanc())
print(point2.distanc())
#ბონუსი
class Faction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def __str__(self):
        return f"{self.top} / {self.bottom}"
    def __add__(self, otherr):
        f = self.top + otherr.top
        e = self.bottom + otherr.bottom
        return Faction(f , e)
    def inverse(self):
        return f"{self.bottom} / {self.top}"
wiladi1 = Faction(3, 3)
wiladi2 = Faction(3,3)
print(wiladi1.__add__(wiladi2))
print(wiladi1.inverse())







