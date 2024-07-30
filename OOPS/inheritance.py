                   # inheritance and polymorphisam


import datetime
today= datetime.date.today()
year=today.year

class Company:
    area="sipcot, siruseri"
    __city="chennai"

    def __init__(self,cname):
        self._cname=cname

    def displayCname(self):
        print("company name : ",self._cname)
        
    def address(self):
        return self.area + " ,"+ self.__city+", Tamilnadu"
    

class Employee(Company):
    empcount=0
    isMarried=False
    def __init__(self,fname,lname,yob,address):
        self._address=address
        self._fname=fname
        self._lname=lname
        self.__age=year-yob
        Employee.empcount +=1
        self.__id=self.empcount

    def getEmpDetails(self):
        print("employee id: ",self.__id)
        print("full name: ",self._fname," ",self._lname)
        print('age: ',self.__age," years")
        print("marital status : ",self.isMarried)
    def address(self):
        print('company address: ',super().address())
        return self._address

# c1=Company("changepond technologies")
# c1.displayCname()
# c1.__city="kerala"
# print("address: ",c1.address())

print("*" * 70)

e1 = Employee("vijay","kumar",2000,"marthandam, Kerala")
e1.isMarried=True
e1.getEmpDetails()
print('employee address : ',e1.address())

print("*" * 70)

e2 = Employee("prasanth","mani",2001,"avadi, Tiruthani")
e2.isMarried=True
e2.getEmpDetails()
print('employee address : ',e2.address())

print("*" * 70)

e3 = Employee("ajith","kumar",2002,"chennai, Tamil nadu")
e3.isMarried=True
e3.getEmpDetails()
print('employee address : ',e3.address())

print("*" * 70)

    

    